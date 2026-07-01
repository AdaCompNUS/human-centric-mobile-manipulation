#!/usr/bin/env python3
"""Scan QR codes and verify the encoded credentials against an accounts JSON file.

The QR payloads are produced by generate_qr_codes.py in the form:
    Username: <username> Password: <password>

Two modes:

  Image mode -- decode every PNG in a directory (or specific files) and check
  each against the accounts file. Good for verifying the generated batch:
      python scan_qr_codes.py _accounts.json --images qr_codes/

  Camera mode -- live webcam scan; each detected code is validated and the
  result is overlaid on the video. Press 'q' to quit:
      python scan_qr_codes.py _accounts.json --camera

Exit code is 0 only when every scanned code is valid (image mode).

    pip install opencv-python
"""

import argparse
import json
import re
import sys
from pathlib import Path

import cv2

PAYLOAD_RE = re.compile(r"^Username:\s*(?P<user>.+?)\s+Password:\s*(?P<pw>.+)$")

# Validation outcomes.
OK = "OK"
WRONG_PASSWORD = "WRONG_PASSWORD"
UNKNOWN_USER = "UNKNOWN_USER"
UNPARSEABLE = "UNPARSEABLE"

# ANSI colors for terminal output.
GREEN, RED, YELLOW, RESET = "\033[32m", "\033[31m", "\033[33m", "\033[0m"
STATUS_COLOR = {OK: GREEN, WRONG_PASSWORD: RED, UNKNOWN_USER: RED, UNPARSEABLE: YELLOW}


def load_accounts(json_path: Path) -> dict:
    """Return {identifier: password}, keyed by both username and email."""
    with json_path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"{json_path} must contain a JSON list of account objects")

    creds = {}
    for entry in data:
        if not isinstance(entry, dict):
            continue
        password = entry.get("password")
        if password is None:
            continue
        password = str(password).strip()
        for key in ("username", "email"):
            ident = entry.get(key)
            if ident:
                creds[str(ident).strip()] = password
    return creds


def validate(payload: str, creds: dict):
    """Return (status, username) for a decoded QR payload."""
    m = PAYLOAD_RE.match(payload.strip())
    if not m:
        return UNPARSEABLE, None
    user = m.group("user").strip()
    pw = m.group("pw").strip()
    if user not in creds:
        return UNKNOWN_USER, user
    if creds[user] != pw:
        return WRONG_PASSWORD, user
    return OK, user


def scan_images(creds: dict, paths) -> int:
    detector = cv2.QRCodeDetector()

    files = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            files.extend(sorted(p.glob("*.png")))
        elif p.exists():
            files.append(p)
        else:
            print(f"{YELLOW}skip{RESET}: {p} not found", file=sys.stderr)

    if not files:
        print("error: no image files to scan", file=sys.stderr)
        return 1

    counts = {OK: 0, WRONG_PASSWORD: 0, UNKNOWN_USER: 0, UNPARSEABLE: 0}
    no_code = 0
    seen_users = set()

    for f in files:
        img = cv2.imread(str(f))
        if img is None:
            print(f"{YELLOW}skip{RESET}: cannot read {f.name}", file=sys.stderr)
            continue
        payload, _, _ = detector.detectAndDecode(img)
        if not payload:
            no_code += 1
            print(f"{YELLOW}NO QR  {RESET} {f.name}: no code detected")
            continue
        status, user = validate(payload, creds)
        counts[status] += 1
        if status == OK:
            seen_users.add(user)
        color = STATUS_COLOR[status]
        label = user if user else payload[:40]
        print(f"{color}{status:<14}{RESET} {f.name}: {label}")

    print("\n--- summary ---")
    print(f"  files scanned : {len(files)}")
    print(f"  {GREEN}valid         : {counts[OK]}{RESET}")
    if counts[WRONG_PASSWORD]:
        print(f"  {RED}wrong password: {counts[WRONG_PASSWORD]}{RESET}")
    if counts[UNKNOWN_USER]:
        print(f"  {RED}unknown user  : {counts[UNKNOWN_USER]}{RESET}")
    if counts[UNPARSEABLE]:
        print(f"  {YELLOW}unparseable   : {counts[UNPARSEABLE]}{RESET}")
    if no_code:
        print(f"  {YELLOW}no code found : {no_code}{RESET}")

    # Accounts that never produced a matching QR.
    usernames = {u for u in creds if not u.count("@")}  # username keys, not emails
    missing = sorted(usernames - seen_users)
    if missing:
        print(f"  {YELLOW}accounts without a valid QR: {len(missing)}{RESET}")
        print("    " + ", ".join(missing))

    all_ok = (
        counts[WRONG_PASSWORD] == 0
        and counts[UNKNOWN_USER] == 0
        and counts[UNPARSEABLE] == 0
        and no_code == 0
    )
    return 0 if all_ok else 2


def scan_camera(creds: dict, cam_index: int) -> int:
    detector = cv2.QRCodeDetector()
    cap = cv2.VideoCapture(cam_index)
    if not cap.isOpened():
        print(f"error: cannot open camera index {cam_index}", file=sys.stderr)
        return 1

    print("Camera scanning. Hold a QR code to the lens; press 'q' to quit.")
    last_payload = None
    bgr = {OK: (0, 180, 0), WRONG_PASSWORD: (0, 0, 220),
           UNKNOWN_USER: (0, 0, 220), UNPARSEABLE: (0, 180, 220)}

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            payload, points, _ = detector.detectAndDecode(frame)
            if payload:
                status, user = validate(payload, creds)
                color = bgr[status]
                if points is not None:
                    pts = points.astype(int).reshape(-1, 2)
                    cv2.polylines(frame, [pts], True, color, 3)
                text = f"{status}: {user or payload[:24]}"
                cv2.putText(frame, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                            0.8, color, 2, cv2.LINE_AA)
                if payload != last_payload:
                    last_payload = payload
                    tag = STATUS_COLOR[status]
                    print(f"{tag}{status:<14}{RESET} {user or payload}")
            cv2.imshow("QR scanner (press q to quit)", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("accounts", type=Path, help="Path to the accounts JSON file")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--images", nargs="+", metavar="PATH",
                       help="Image files and/or directories of PNGs to verify")
    group.add_argument("--camera", action="store_true", help="Live webcam scan")
    parser.add_argument("--cam-index", type=int, default=0,
                        help="Camera device index for --camera (default: 0)")
    args = parser.parse_args()

    if not args.accounts.exists():
        print(f"error: {args.accounts} not found", file=sys.stderr)
        return 1
    creds = load_accounts(args.accounts)
    if not creds:
        print(f"error: no credentials loaded from {args.accounts}", file=sys.stderr)
        return 1

    if args.camera:
        return scan_camera(creds, args.cam_index)
    if args.images:
        return scan_images(creds, args.images)

    # Default: verify the standard qr_codes/ output directory.
    default_dir = Path("qr_codes")
    if default_dir.is_dir():
        print(f"No mode given; verifying {default_dir}/ "
              f"(use --camera for live scan)\n")
        return scan_images(creds, [default_dir])
    parser.error("specify --images <paths> or --camera")


if __name__ == "__main__":
    sys.exit(main())
