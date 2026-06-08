---
permalink: /
title:
layout: home
image:
  path: /assets/img/Workshoplogo.png
  alt: Human-Centric Mobile Manipulation Workshop logo
---

<section class="home-hero" style="background-image: url('{{ '/assets/img/rss2026.png' | relative_url }}');" aria-label="Workshop banner">
  <div class="home-hero__overlay">
    <h1 class="home-hero__title">Human-Centric Mobile Manipulation Workshop</h1>
    <p class="home-hero__subtitle">Robotics Science and Systems Conference (RSS 2026)</p>
    <p class="home-hero__meta">Date &amp; time: July 17, 2026</p>
    <p class="home-hero__meta">Location: Sydney, Australia</p>
  </div>
</section>

Can a robot effectively perform mobile manipulation tasks in real-world environments with humans? As mobile manipulators transition from controlled lab settings into human-centered environments such as homes, hospitals, and workplaces, they must not only navigate and manipulate objects, but also communicate and collaborate with humans in a safe, intuitive, and efficient manner. Despite recent advances in autonomous mobile manipulation, robots continue to struggle with two fundamental challenges. First, establishing intuitive and reliable human–robot interaction that allows humans to convey intent, provide feedback, and intervene when necessary. Second, planning and executing human-aware motion and manipulation behaviors that explicitly account for human presence, safety, comfort, and collaborative dynamics. Addressing these challenges is essential for enabling robots to operate as effective partners rather than isolated autonomous agents in real-world, human-centric environments. This workshop aims to bring together researchers and practitioners to develop a shared understanding of these challenges, explore emerging solutions, and identify promising research directions in human-centric mobile manipulation.

In particular, this workshop aims to address the following questions:

* How should tasks, goals, constraints, and preferences be specified for mobile manipulation in human environments?
* How can robots plan and act in ways that are explicitly aware of human presence, safety, and comfort?

To support easy human-robot connections, we developed [RoboMesh](https://robomesh.ssilabs.org), which enables all participants to play with robots, and contribute their robot demos. 
<!-- We welcome any contributions to our [RoboMesh](https://robomesh.ssilabs.org)! -->

<!-- <div style="display: flex; justify-content: center; margin-top: 0.5rem;">
  <div style="flex: 1 1 300px; max-width: 70%;">
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px;">
      <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://www.youtube.com/embed/wEbUjZfUTqU" title="RoboMesh demo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
  </div>
</div> -->



### <center>Discussion Topics</center>

We invite submissions of papers and live demos, including, but not limited to, the following related topics:

* Human-Robot Interaction Interface Design
* Safe Whole Body Motion Planning & Control
* Foundation Models for Mobile Manipulation
* Uncertainty and Risk-Aware Decision Making
* Shared Autonomy & Responsibility Allocation
* Open-World Planning in Human-Centric Environments
* Failure Prediction & Recovery
* Benchmarks & Evaluation for Human-Centered Manipulation

<br>

### <center>Call for Papers</center>

<p style="text-align: left;">
We invite paper submissions on human-centric mobile manipulation. The submission deadline is <del><strong>June 12, 2026 (AoE)</strong></del> <span style="color: red;"><strong>June 22, 2026 (AoE)</strong></span>. Please see the
<a href="{{ '/callforpapers/' | relative_url }}">Call for Papers</a> for topics and submission guidelines. 
</p>

<br>

### <center>Call for Demos</center>

<p style="text-align: left;">
We invite <strong>live, interactive demos</strong> (and also <strong>video demos</strong>) on human-centric mobile manipulation.
All live demos will be deployed and demonstrated via <a href="https://robomesh.ssilabs.org">RoboMesh</a>.
Demo videos should be <strong>less than 5 minutes</strong>.
</p>

<ul>
  <li><strong>Proposal Submission Deadline:</strong> <del>June 5, 2026 (AoE)</del> <span style="color: red;">June 19, 2026 (AoE)</span></li>
  <li><strong>Demo Submission Deadline:</strong> <del>June 26, 2026 (AoE)</del> <span style="color: red;">July 1, 2026 (AoE)</span></li>
</ul>

<p style="text-align: left;">
See the <a href="{{ '/callforvideos/' | relative_url }}">Call for Demos</a> page for submission instructions.
</p>

<br>

### <center>Keynote Speakers</center>

{% assign keynotes = site.speakers | where: "type", "keynote" %}
{% include people_grid.html people=keynotes image_subdir="speakers" columns=5 inner_max_width="800px" %}

<br>

### <center>Demo Speakers</center>

{% assign demos = site.speakers | where: "type", "demo" %}
{% include people_grid.html people=demos image_subdir="speakers" columns=5 %}

<br>
### <center>Organizing Committee</center>

{% include people_grid.html people=site.organizers image_subdir="organizers" columns=5 %}

<br>
