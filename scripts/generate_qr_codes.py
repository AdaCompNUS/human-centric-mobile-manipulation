#!/usr/bin/env python3
"""Generate one QR code PNG per account in a JSON file of account/password pairs.

Usage:
    pip install qrcode[pil]
    python generate_qr_codes.py _accounts.json -o qr_codes/

The JSON file is a list of objects, each with at least:
    {"username": ..., "email": ..., "password": ...}

Each QR encodes a single line of plain text:
    Username: <username> Password: <password>

PNG files are named qr_<username>.png (username sanitized for filesystem).
"""

import argparse
import json
import re
import sys
from pathlib import Path

import qrcode


def sanitize_filename(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_") or "account"


def read_accounts(json_path: Path):
    with json_path.open(encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError(f"{json_path} must contain a JSON list of account objects")

    for entry in data:
        if not isinstance(entry, dict):
            continue
        # Prefer the login identifier the user authenticates with.
        account = entry.get("username") or entry.get("email")
        password = entry.get("password")
        if account is None or password is None:
            continue
        account = str(account).strip()
        password = str(password).strip()
        if not account or not password:
            continue
        yield account, password


def make_qr(payload: str, out_path: Path) -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(payload)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(out_path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("accounts", type=Path, help="Path to the accounts JSON file")
    parser.add_argument(
        "-o", "--out-dir", type=Path, default=Path("qr_codes"),
        help="Output directory for PNGs (default: ./qr_codes)",
    )
    args = parser.parse_args()

    if not args.accounts.exists():
        print(f"error: {args.accounts} not found", file=sys.stderr)
        return 1

    args.out_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    seen = set()
    for account, password in read_accounts(args.accounts):
        base = sanitize_filename(account)
        filename = f"qr_{base}.png"
        if filename in seen:
            suffix = 2
            while f"qr_{base}_{suffix}.png" in seen:
                suffix += 1
            filename = f"qr_{base}_{suffix}.png"
        seen.add(filename)

        payload = f"Username: {account} Password: {password}"
        make_qr(payload, args.out_dir / filename)
        count += 1

    print(f"Wrote {count} QR code(s) to {args.out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
