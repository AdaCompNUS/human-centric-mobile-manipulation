---
layout: page
title: Call for Demos
permalink: /callforvideos/
---

<div style="border-left: 4px solid #1e8449; background: #edf7f0; padding: 0.9rem 1.1rem; border-radius: 6px; margin-bottom: 1.8rem; color:#555;">
  <strong style="color:#1e8449;">We continuously welcome contributions to RoboMesh!</strong> Although the RSS&nbsp;2026 workshop demo submission window has closed, the platform behind the demos, <a href="https://robomesh.ssilabs.org"><strong>RoboMesh</strong></a>, stays open. We warmly welcome new demos and users all year round.
</div>

## Demos at the Workshop

The following live, interactive demos will run on RoboMesh during the workshop:

{% assign workshop_demos = site.speakers | where: "type", "demo" | sort: "sequence_id" %}
<div style="display:flex; flex-direction:column; gap:0.8rem; margin:1.2rem 0;">
{% for d in workshop_demos %}
  <div style="background:#fff; border:1px solid #e7e0e0; border-radius:10px; padding:0.9rem 1.1rem;">
    <div style="font-weight:600; color:#2a7ae2; font-size:1.05rem;">{{ d.demo_name }}</div>
    <div style="margin-top:0.25rem; color:#333;">
      {% if d.webpage %}<a href="{{ d.webpage }}" target="_blank">{{ d.name }}</a>{% else %}{{ d.name }}{% endif %}{% if d.pi_name %} &middot; PI:
      {% if d.pi_webpage %}<a href="{{ d.pi_webpage }}" target="_blank">{{ d.pi_name }}</a>{% else %}{{ d.pi_name }}{% endif %}{% endif %}
    </div>
    <div style="color:#777; font-size:0.9rem; margin-top:0.15rem;">{% if d.affil_link %}<a href="{{ d.affil_link }}" target="_blank" style="color:#777;">{{ d.affil }}</a>{% else %}{{ d.affil }}{% endif %}{% if d.lab %} &middot; {{ d.lab }}{% endif %}</div>
  </div>
{% endfor %}
</div>

## Introducing RoboMesh

<p style="font-size: 1.2rem; font-weight: 500; color:#333; line-height: 1.5;">
What if a robot "demo" wasn't just a video to watch, but a real demonstration you could <em>interact with</em> and <em>probe</em>?
</p>

We are excited to introduce **RoboMesh**, a web-based platform that connects people to real robots through online interaction.

<div style="display: flex; justify-content: center; margin: 1.6rem 0;">
  <div style="flex: 1 1 300px; max-width: 70%;">
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px;">
      <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://www.youtube.com/embed/wEbUjZfUTqU" title="RoboMesh demo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
  </div>
</div>

## We are calling for users

<div style="display: flex; flex-wrap: wrap; gap: 1rem; margin: 1.3rem 0;">
  <div style="flex: 1 1 220px; border-radius: 10px; padding: 1.1rem 1.2rem; background:#f0f4fb; border:1px solid #d8e2f3;">
    <strong>For developers</strong><br>
    <span style="color:#444;">Answer key failure-analysis and HRI questions with real interaction data.</span>
  </div>
  <div style="flex: 1 1 220px; border-radius: 10px; padding: 1.1rem 1.2rem; background:#f0f4fb; border:1px solid #d8e2f3;">
    <strong>For reviewers</strong><br>
    <span style="color:#444;">Failed executions can be replayed, inspected, and exported, for transparency.</span>
  </div>
  <div style="flex: 1 1 220px; border-radius: 10px; padding: 1.1rem 1.2rem; background:#f0f4fb; border:1px solid #d8e2f3;">
    <strong>For labs</strong><br>
    <span style="color:#444;">User commands, robot observations, system responses, and recovery behaviors can be collected as valuable data.</span>
  </div>
</div>

<div style="text-align: center; margin: 2.2rem 0 0.6rem;">
  <a href="https://robomesh.ssilabs.org" target="_blank" style="display: inline-block; background: #2a7ae2; color: #fff; font-weight: 600; padding: 0.8rem 2rem; border-radius: 8px; text-decoration: none; font-size: 1.1rem; box-shadow: 0 2px 6px rgba(42,122,226,0.3);">Try RoboMesh &rarr;</a>
</div>

<p style="text-align: center; color:#555; margin-top: 1.4rem;">
Want to host your own robot on RoboMesh? We welcome new demos on a rolling basis:
<a href="https://forms.gle/36C7Df2bRE72mDC2A">submit a proposal</a>.
</p>

---

## About the Demo Track

We invite **live, interactive demos** showcasing human-centric mobile manipulation systems. All demos will be deployed and demonstrated through **[RoboMesh](https://robomesh.ssilabs.org)**, a web-based platform that enables **online interaction with robots**.

Submitted demos should support real-time human-robot interaction via one or more of the following modalities:
- Text or language-based commands
- Voice interaction
- Web-based gestures such as clicking, dragging, and pointing

Demos are expected to illustrate human-robot interaction, shared autonomy, human-aware planning, or human intervention and failure recovery in realistic mobile manipulation scenarios. **For accepted demos, at least one author is required to attend RSS 2026 in person to host the demonstration**.

We welcome contributions in areas including, but not limited to, the following topics:

* Human-Robot Interaction and Collaboration
* Cognitive Architectures for Robots in Human Environments
* Foundation Models for Mobile Manipulation
* Safe Whole Body Motion Planning & Control
* Planning Under Uncertainty and Risk
* Shared Autonomy & Responsibility Allocation
* Failure Prediction & Recovery
* Socially Aware Navigation and Manipulation

## Demo Submission Instructions

**Live Demo Submission Instructions**:
If you are interested in submitting a live demo, please submit a one-page proposal and your demo video through the [Google Form](https://forms.gle/36C7Df2bRE72mDC2A). The demo video should be **less than 5 minutes**.

We will send invitations to selected demos, granting access to our RoboMesh platform. After acceptance, demo presenters will integrate their demos into the RoboMesh platform.

## Important Dates

*(All deadlines are Anywhere on Earth, AoE)*

- <span style="color:#999;">Submission portal opens: <strong>May 8, 2026</strong></span>
- <span style="color:#999;">Live demo proposal submission deadline: <strong>June 19, 2026</strong></span>
- <span style="color:#999;">Notification of acceptance: <strong>June 26, 2026</strong></span>
- <span style="color:#999;">Demo integration and submission deadline: <strong>July 1, 2026</strong></span>
- **Workshop date**: **July 17, 2026**
