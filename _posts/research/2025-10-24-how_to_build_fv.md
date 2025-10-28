---
title: "How to Build an Empirical Speed Distribution for Dark Matter in the Solar Neighborhood"
layout: post
categories:
  - Research
tags:
  - Papers
  - Research
permalink: /:categories/how_to_build_fv
excerpt: This paper shows how to leverage <i>ex situ</i> stellar kinematics as tracers for the speed distribution of accreted dark matter. This allows us to go beyond the simple Maxwell&ndash;Boltzmann approximation by folding in knowledge about a galaxy's assembly history. We apply this to the Milky Way itself, using <i>Gaia</i> data to quantify how modeling the dark matter from the GSE merger impacts the inferred speed distribution. 
comments: false
---

<a href="https://ui.adsabs.harvard.edu/abs/2025arXiv251021914S/abstract">arXiv:2510.21914</a>, to submit to Astrophys. J.  
Data available <a href='https://github.com/Tal-Shpigel/stellar-dm-velocity-distributions'>on GitHub</a>

---
The dark matter flux in a direct detection experiment depends on its local speed distribution. This distribution has been inferred from simulations of Milky Way&ndash;like galaxies, but such models serve only as proxies given that no simulation directly captures the detailed evolution of our own Galaxy. This motivates alternative approaches which obtain this distribution directly from observations. In this work, we utilize 98 Milky Way analogues from the <code>TNG50</code> simulation to develop and validate a procedure for inferring the dark matter speed distribution using the kinematics of nearby stars. We find that the dark matter that originated from old mergers, plus that from recent non-luminous accretions, is well described by a Maxwell&ndash;Boltzmann speed distribution centered at the local standard-of-rest velocity. Meanwhile, recently accreted dark matter from massive mergers has speeds that can be traced from the associated stellar debris of these events. The stellar populations systematically underestimate the velocity dispersion of their dark matter counterparts, but a simple kinematic boost brings the two into good alignment. Using the <code>TNG50</code> host galaxies, we demonstrate that combining these two contributions provides an accurate reconstruction of the local dark matter speeds. As  an application of the procedure to our own Galaxy, we utilize stellar kinematic data from _Gaia_ to quantify how the dark matter remnants from the Milky Way's last major merger impact its speed distribution in the Solar neighborhood.

<figure>
  <img src="/assets/research/2510_thumb.png" alt="Local dark matter speed distribution reconstruction">
  <figcaption class='message'>Our reconstruction of the dark matter speed distribution around the Sun. We use <i>Gaia</i> stellar data (solid orange) to model the dark matter contributed by the GSE merger (dashed orange). This is added to a Maxwell&ndash;Boltzmann distribution (black) to yield the full model, sampling over our reconstruction uncertainties (green band). </figcaption>
</figure>