---
permalink: /
title:
layout: home
---

## <center><span style="color:#2F5597">Human-centric Mobile Manipulation Workshop</span></center>
##### <center>RSS 2026 Workshop</center>
##### <center>Date & Time: TBD</center>
##### <center>Location: TBD</center>

Can a robot effectively perform mobile manipulation tasks in real-world environments with humans? As mobile manipulators transition from controlled lab settings into human-centered environments such as homes, hospitals, and workplaces, they must not only navigate and manipulate objects, but also communicate and collaborate with humans in a safe, intuitive, and efficient manner. Despite recent advances in autonomous mobile manipulation, robots continue to struggle with two fundamental challenges. First, establishing intuitive and reliable human–robot interaction that allows humans to convey intent, provide feedback, and intervene when necessary. Second, planning and executing human-aware motion and manipulation behaviors that explicitly account for human presence, safety, comfort, and collaborative dynamics. Addressing these challenges is essential for enabling robots to operate as effective partners rather than isolated autonomous agents in real-world, human-centric environments. This workshop aims to bring together researchers and practitioners to develop a shared understanding of these challenges, explore emerging solutions, and identify promising research directions in human-centric mobile manipulation.

In particular, this workshop aims to address the following questions:

* How should tasks, goals, constraints, and preferences be specified for mobile manipulation in human environments?
* How can robots plan and act in ways that are explicitly aware of human presence, safety, and comfort?

<br>

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem; margin-top: 1rem;">
  <div style="flex: 1 1 300px; max-width: 33%;">
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px;">
      <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://www.youtube.com/embed/r5yw3hcRvxQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  </div>
  <div style="flex: 1 1 300px; max-width: 33%;">
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px;">
      <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  </div>
  <div style="flex: 1 1 300px; max-width: 33%;">
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px;">
      <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  </div>
</div>

<br>

### <center>Discussion Topics</center>

We invite submissions of papers and live demos, including, but not limited to, the following related topics:

* Human-Robot Interaction Interface Design
* Human-Aware Whole Body Motion Planning & Control
* Foundation Models for Mobile Manipulation
* Uncertainty and Risk-Aware Decision Making
* Shared Autonomy & Responsibility Allocation
* Failure Prediction & Recovery
* Benchmarks & Evaluation for Human-Centered Manipulation

<br>

### <center>Call for Papers</center>

<p style="text-align: left;">
We invite paper submissions on <strong>human-centric mobile manipulation</strong>. The submission deadline is TBD. Please see the
<a href="{{ '/callforpapers/' | relative_url }}">Call for Papers</a> for topics and submission guidelines. 
</p>

<br>

### <center>Call for Demos</center>

<p style="text-align: left;">
We invite <strong>live, interactive demos</strong> (and also <strong>video demos</strong>) on human-centric mobile manipulation.
All live demos will be deployed and demonstrated via <a href="https://tom-bridge.nusssi.com/robomesh/">RoboMesh</a>.
<strong>Deadlines:</strong> TBD (AoE). See the <a href="{{ '/callforvideos/' | relative_url }}">Call for Demos</a> page for submission instructions.
</p>

<br>

### <center>Keynote Speakers</center>

{% assign keynotes = site.speakers | where: "type", "keynote" %}
{% include people_grid.html people=keynotes image_subdir="speakers" %}

<br>

### <center>Live Demo Speakers</center>

{% assign demos = site.speakers | where: "type", "demo" %}
{% include people_grid.html people=demos image_subdir="speakers" %}

### <center>Organizers</center>

{% include people_grid.html people=site.organizers image_subdir="organizers" %}

<br>
