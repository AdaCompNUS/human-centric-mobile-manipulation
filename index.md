---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

permalink: /
title:
layout: home
---

## <center><span style="color:#2F5597">Open World Navigation</span> in Human-centric Environments</center>
##### <center>IROS 2025, Hangzhou, China</center>
##### <center>20th Oct 2025, Monday, 1:15pm - 6:00pm (UTC +8)</center>
##### <center>Grand Ballroom A, Hangzhou International Expo Center</center>


<video controls="" width="100%" muted="" loop="" autoplay="">
<source src="assets/img/own_banner_cropped.mp4" type="video/mp4">
</video>

Can a robot be deployed anywhere in the world, then navigate its surroundings zero-shot to reach a goal? Navigation in the open world remains an elusive grail of robotics, owing to the sheer diversity of environments, agents and scenarios a robot can encounter. With the rise of foundation models, robots have attained unprecedented levels of generalization, enabling progress toward open world navigation. Yet training data is bounded, making it almost certain robots will encounter unexpected, out-of-distribution scenarios. Thus achieving open world navigation requires taking a path that balances improving generalization with out-of-distribution handling. Recent workshops have focused on individual elements of this, such as applications of LLMs/VLMs to navigation or robot failure management. In contrast, this workshop seeks to provide a timely and unique perspective on system design for open world navigation, that unites the application of increasingly powerful and general foundation models with explicit consideration of failures and out-of-distribution scenarios.

In particular, this workshop aims to answer the questions:

* How do we build generalizable systems for open world navigation with foundation models?
* How do we detect failures of such systems, particularly for scenarios that are out-of-distribution for learned/foundation models?
* What strategies can be employed to mitigate failures or recover from them?
* What are suitable benchmarks to gauge progress in open world navigation?
<br>

### <center>Speakers and Panelists</center>

{% assign speakers_and_panelists = site.speakers | concat: site.panelists %}
{% include people_grid.html people=speakers_and_panelists image_subdir="speakers" %}
<br>

### <center>Call for Videos</center>

We are accepting short videos related to the challenges or failure modes of robot navigation systems in the open world, which we will screen during the workshop. Please refer to the [Call for Videos](/callforvideos/) for more details.

🏆 **Best Video Award**: FrodoBot Mini+ Robot

### <center>Call for Papers</center>

<!-- We are excited to announce that Best Paper and Best Paper Runner-Up awards will be given at the workshop! -->

<!-- 🏆 Best Paper Award: $300 -->
<!-- 🥈 Best Paper Runner-Up: $100 -->

We are accepting paper submissions related to generalization and failure handling in robot navigation. Please refer to the [Call for Papers](/callforpapers/) for more details.

🏆 **Best Paper Award**: FrodoBot Mini+ Robot

<p style="text-align: center;">
<em>Time to 1st call for papers deadline</em> (15 Aug 2025):
</p>

<center>
<div id="countdown1" style="font-size: 1.5rem; font-weight: bold;"></div>
<script>
  // Countdown 1
  const countdownDate1 = new Date("2025-08-16T00:00:00").getTime();
  const countdownElement1 = document.getElementById("countdown1");

  const updateCountdown1 = () => {
    const now = new Date().getTime();
    const distance = countdownDate1 - now;

    if (distance < 0) {
      countdownElement1.innerHTML = "0d 0h 0m 0s";
      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    countdownElement1.innerHTML =
      days + "d " + hours + "h " + minutes + "m " + seconds + "s";
  };

  updateCountdown1();
  setInterval(updateCountdown1, 1000);
</script>
</center>

<br>
<p style="text-align: center;">
<em>Time to 2nd call for papers deadline</em> (19 Sep 2025):
</p>

<center>
<div id="countdown2" style="font-size: 1.5rem; font-weight: bold;"></div>
<script>
  // Countdown 2
  const countdownDate2 = new Date("2025-09-20T00:00:00").getTime();
  const countdownElement2 = document.getElementById("countdown2");

  const updateCountdown2 = () => {
    const now = new Date().getTime();
    const distance = countdownDate2 - now;

    if (distance < 0) {
      countdownElement2.innerHTML = "The second event has started!";
      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    countdownElement2.innerHTML =
      days + "d " + hours + "h " + minutes + "m " + seconds + "s";
  };

  updateCountdown2();
  setInterval(updateCountdown2, 1000);
</script>
</center>


### <center>Organizers</center>

{% include people_grid.html people=site.organizers image_subdir="organizers" %}

<br>
### <center>Sponsors</center>

<center><img src="assets/img/frodobots.png" alt="drawing" width="400"/></center>

### <center>