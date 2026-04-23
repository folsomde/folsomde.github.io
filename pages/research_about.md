---
layout: page
title: About my research
permalink: /research/about
---

<div class = "message">
<h3 style='margin-top:0.25rem'><i class="fa-duotone fa-solid fa-triangle-exclamation"></i> Warning!</h3> This page is still under construction. Feel free to read what's here now, but check back soon to see it all polished up.
</div>

The fundamental aim of my research is to better understand the Universe around us. In particular, we think that everything we can see, all the "normal stuff," (what astrophysicists call "baryonic matter") is only a small fraction of what's actually present around us. The rest of the matter in the Universe is given the label "dark matter." I study dark matter in and around the Milky Way galaxy&mdash;where we live&mdash;and the satellite galaxies that are in orbit around the Milky Way.

<div class = "message" style="color:#313131">
<a name="toc"></a>
<h3 style='margin-top:0.25rem'><i class="fa-solid fa-list"></i>&nbsp; Contents</h3> 
<b>Background questions:</b>
<ul>
  <li><a href='#MW'>What is the Milky Way?</a></li>
  <li><a href='#DM'>What is dark matter?</a></li>
  <li><a href='#detection'>Can we detect dark matter?</a></li>
</ul>
<b>My research:</b>
<ul>
  <li><a href='#local'>What can we learn about the dark matter in the Milky Way?</a></li>
  <li><a href='#satellites'>and in its satellites?</a></li>
</ul>
</div>

## First, some background:
### What is the Milky Way? <a name="MW"></a>
{: style='margin-top: 0'}
The Milky Way is a galaxy, a collection of gas and dust and stars. The Sun is one of the stars in the Milky Way's disk. There are around a hundred billion other stars in the Milky Way galaxy: when you look up at the night sky, most of what you see are these stars, our neighbors in the Milky Way. We're located near the outskirts of the Galaxy,[^gal] around 25 thousand light years from the center.

[^gal]: A weird astronomer quirk is that "the Galaxy" with a capital G refers to the Milky Way in particular, while galaxy with a lowercase G can be any galaxy. The same thing goes for Universe; the real-life universe we live in is "the Universe" with a capital U, while the idea of "a universe" in the abstract (or a simulated universe) gets a lowercase U.

<figure>
  <iframe width="100%" src="https://player.vimeo.com/video/370153200" frameborder="0" allowfullscreen="" style="aspect-ratio: 16/9;"></iframe>
  <figcaption class='message'>This video starts at the location of the Sun inside the Milky Way, looking toward the Galactic center. The camera then moves outward to show the Galaxy as a whole, and includes some of the neighboring dwarf galaxies! In the video, you can see the Galaxy's disk, which is made up of gas and dust and stars.<br><small><i>Animation by Stefan Payne-Wardenaar</i></small></figcaption>
</figure>

The Milky Way hosts a system of satellite galaxies, smaller objects that have been caught in its gravitational pull. Some of these, like [the Large Magellanic Cloud](https://apod.nasa.gov/apod/ap170821.html), are visible with the naked eye (in the southern hemisphere, at least). We have directly seen around 60 of these satellite galaxies, and with new telescopes like [the Rubin Observatory](https://en.wikipedia.org/wiki/Vera_C._Rubin_Observatory), we expect to find hundreds more. Even though they're in orbit around the Milky Way, they are still pretty far out: the closest ones we know of are about 65 thousand light years away. 

Going farther out from us, the Milky Way itself is caught in the gravitational pull of a bigger neighboring galaxy, Andromeda, about 2.5 million light years away. It's thought[^mw-andromeda] that the Milky Way and Andromeda will eventually collide in about 5 billion years. These collisions are how galaxies grow: smaller galaxies merge with bigger ones, slowly feeding the bigger galaxy new material. Sometimes, the galaxies can be of comparable size (like the Milky Way and Andromeda), where instead of a slow growth process, the merger is much more violent and can radically reshape the original galaxy. 

[^mw-andromeda]: For a long time, people have assumed that the Milky Way and Andromeda would crash into each other, but with recent data this is has been called into question! Here's a semi-technical article describing that recent paper: [Nature Astronomy **9**, p. 1107–1108 (2025)](https://www.nature.com/articles/s41550-025-02629-0)

<figure>
<video width="100%" controls>
  <source  src="https://www.tng-project.org/movies/tng/tng50_single_galaxy_formation_g1_1080p_clean_stars.mp4">
    Video not supported.
</video>
<figcaption class='message'>A simulation of a galaxy forming. I've set the video to start pretty late into the simulation (feel free to rewind to check out the beginning, though!) when the stars have settled into a disk. You can occasionally see this galaxy accrete satellites; at around 1:03 one of its satellites makes a flyby before coming back to finally merge around 1:12&ndash;1:20<br><small><i>Video by the TNG Collaboration: see more <a href="https://www.tng-project.org/media/">here</a></i></small></figcaption>
</figure>

### What is dark matter? <a name="DM"></a>
By the 1970s, we had telescopes that were good enough to measure how fast stars move in galaxies like the Milky Way. An influential paper by [Vera Rubin](https://en.wikipedia.org/wiki/Vera_Rubin) showed that these stars are moving faster than expected, which means that they are experiencing a stronger gravitational pull than they should&mdash;there's more stuff in a galaxy than what we can see. Since this extra stuff is invisible (it gives off no light), it was given the name "dark matter." The dark matter provides the extra gravitational pull that moves these stars around. This is pretty much all we know must be true of dark matter; it has to be dark, and it has to have a gravitational pull. There also needs to be enough of it to explain the excess gravitational force we see: there is about five times as much dark matter as normal matter.

The current understanding is that in the very early Universe, dark matter started to clump together through its gravitational pull. These clumps, or "halos," then pulled in gas, which eventually formed the galaxies that we see today. This means every galaxy sits in the middle of one of these dark matter halos. The Milky Way's halo is about ten times the size of the galaxy itself!

<figure style='margin-top: 2rem;'>
<img src='/assets/research/Stellar-density.png' onmouseover="this.src='/assets/research/DM-density.png';" onmouseout="this.src='/assets/research/Stellar-density.png';" />
  <figcaption class='message'>Simulation of a galaxy similar to the Milky Way. By default, the image shows the location of the galaxy's stars, but if you hover over the image, you will see the dark matter distribution. The dark matter "halo" is much larger than the galaxy! Furthermore, there are some satellite galaxies around the central host: there's one currently merging with the host, very close to the disk, and another in the top right of the image. There are many more clumps of dark matter though; these clumps either host very faint galaxies or are too small to have formed stars at all<br>
  <small><i>Data from the <code>TNG50</code> simulation</i></small></figcaption>
</figure>

#### Disambiguation: What *isn't* dark matter?
{: style='color:#515151'}
Scientists aren't great at naming things, and the terminology can get a little confusing. In particular, dark matter often gets confused with

**Dark energy:**{: style='color:#515151'} From Einstein's theory of gravity, we know that almost all kinds of matter cause the Universe to expand, but different types of matter do this at different rates -- they cause different ["accelerations" in a sense](https://en.wikipedia.org/wiki/Deceleration_parameter). For example, radiation (like light) causes the Universe to expand differently than "cold" matter (like galaxies and their dark matter). In both cases, the Universe will always expand, but matter causes a faster expansion than radiation does. In these universes, the rate of expansion would eventually slow to a crawl.[^accel] We observe an expansion pattern that is different from both of those, where the expansion is accelerating faster and faster: we call whatever is driving this "dark energy." The simplest explanation for this accelerated expansion is called "cosmological constant" dark energy, where space itself has an energy intrinsic to it. As the Universe expands, there is more space with more cosmological constant energy, which pushes the expansion even faster. We don't know if a cosmological constant is the best explanation, but it's what's most commonly accepted right now.[^cosmo]

**Black holes:**{: style='color:#515151'} Okay, *technically* black holes can be dark matter, more on that in the next paragraph. Black holes can be caused by perfectly normal-matter processes, though, and are known to happen to normal material: whenever too much mass is packed into too small a space, a black hole will form. This can happen to very massive stars at the end of their lifetimes. When these stars run out of fuel, they are no longer able to support themselves, and they collapse. If this collapse progresses far enough, all the star's leftover material can get packed into a tight enough space to form a black hole. 

Black holes don't give off light,[^hawking] and they do exert a gravitational pull, which are the two things we know should be true of dark matter, so they are interesting candidate explanations for what dark matter could be! From observations of the very early Universe, we know that dark matter should have been around even then, before stars could have formed, so if black holes are dark matter, they must be "[primordial](https://en.wikipedia.org/wiki/Primordial_black_hole)," originating very early in the history of the Universe, rather than being from collapsing stars. These black holes would have other observable signatures (e.g., if they start accreting material, we could see signs of that, or they might [cause distortions](https://en.wikipedia.org/wiki/Gravitational_microlensing) in starlight that we could detect). The constraints placed on this really restrict the possibilities for primordial black hole dark matter, to the point that if they truly are (all of) the dark matter, they have to be in a particular mass range, \\(10^{17}-10^{22}\\) grams, called the "astroid mass window"

[^accel]: Specifically, the relative size of the Universe is described by the "scale factor" \\(a(t)\\). In a radiation-only universe, \\(a\propto t^{1/2}\\), while matter gives an expansion \\(a \propto t^{2/3}\\). In both cases, the first derivative is positive (the size always increases), but the second derivative is negative (the expansion is decelerating). A universe with "cosmological constant" dark energy has \\(a \propto \exp(t)\\), which has positive second derivative -- the expansion accelerates. 
[^cosmo]: This is another topic of active debate: in 2025, the Dark Energy Spectroscopic Instrument (DESI) released data that suggest the actual nature of dark energy doesn't quite agree with the cosmological constant model. Cosmologists are trying to figure out what models best describe these data.
[^hawking]: Black holes do glow *super* faintly (too faintly to actually be visible) through a process called [Hawking radiation](https://en.wikipedia.org/wiki/Hawking_radiation), and if the black hole is surrounded by an [accretion disk](https://en.wikipedia.org/wiki/Accretion_disk) of gas and dust, that material can give off light too. This is actually quite common in galaxies, where a central black hole causes a ton of energy to be emitted: we call these [active galactic nuclei](https://en.wikipedia.org/wiki/Active_galactic_nucleus).

### Can we detect dark matter? <a name="detection"></a>

The precise properties of dark matter are still undetermined. It doesn't seem to interact through any of the forces except gravity. This means we haven't seen light from it or touched it directly; we can only tell it's there because of its gravitational pull. Even then, it takes a lot of dark matter before we start to notice, and we have only seen its effects on very large structures in the Universe like galaxies. If dark matter does ever interact with normal matter, it must do so very rarely, since we haven't noticed any concrete evidence of this yet. 

We're still trying to make sure of this, though: the theory behind particle physics tells us it's pretty strange for something to be *completely* noninteracting. There are good reasons from the theory to expect that it does still interact with normal matter, just very weakly. For this reason, scientists are trying to detect these interactions. 

There are three main ways we could notice interactions between dark matter and normal matter:
  1. We could **produce** it in a lab by smashing together normal stuff at very high energies. There's a chance we could convert the normal matter into a little bit of dark matter at a collider like the LHC.
  2. We might **directly detect** dark matter by setting up a big tank in a lab with a high concentration of normal matter. Even though it's unlikely for dark matter to interact with any individual atom, we can cram a bunch of normal matter into a detector to maximize the chances for an interaction. We can then look for signs that dark matter bumped into one of the atoms in the detector.
  3. We can also **indirectly detect** dark matter "decay" or "annihilation." Just like how normal matter might convert into dark matter in a collider, it's possible for dark matter to convert into normal stuff, especially if there's a lot of dark matter around, like there is surrounding galaxies. The dark matter around the Milky Way might give off a faint glow of visible light through these processes.

## What is my contribution to this?


My research has applications to direct and indirect detection, which I'll explain  
I study dark matter through the evolution of galaxies and the halos they live in. The Milky Way, like all galaxies, assembled hierarchically. That means that it grows by accreting other, smaller galaxies; these "dwarf galaxies" get pulled in by the Milky Way's gravity until they eventually merge completely with it. These galaxies all live in their own dark matter halos, and so the Milky Way accretes their dark matter too.
<!-- <iframe width="100%" src="https://www.youtube.com/embed/O674AZ_UKZk" frameborder="0" allowfullscreen="" style="aspect-ratio: 16/9;"></iframe> -->

<figure>
<img src='/assets/research/stefan-dwarfs-unlabeled.jpg' onmouseover="this.src='/assets/research/stefan-dwarfs.jpg';" onmouseout="this.src='/assets/research/stefan-dwarfs-unlabeled.jpg';" />
  <figcaption class='message'>Rendering of some Local Group galaxies: the Milky Way in the center, the Magellanic Clouds to the right, and some other dwarfs (Sagittarius and Sculptor) faintly visible at the top and bottom. Hover to see the galaxies labeled!<br><small><i>Credit to Stefan Payne-Wardenaar</i></small></figcaption>
</figure>

<script>
  let video = document.getElementsByTagName('video')[0]
  video.currentTime = 60
</script>