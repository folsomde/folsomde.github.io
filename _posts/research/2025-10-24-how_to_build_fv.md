---
title: "How to Build an Empirical Speed Distribution for Dark Matter in the Solar Neighborhood"
layout: post
categories:
  - Research
tags:
  - Papers
  - Research
  - Simulations
permalink: /:categories/how_to_build_fv
excerpt: Accreted stellar populations carry information about the mergers that contributed them. This allows us to go beyond the simple Maxwell&ndash;Boltzmann approximation for dark matter speeds by folding in knowledge about a galaxy's assembly history. We quantify the relationship between accreted stellar and dark matter velocities, then apply this to the Milky Way itself, using <i>Gaia</i> data to determine how modeling the dark matter from the GSE merger impacts the inferred speed distribution. 
comments: false
---
{% comment %}
<div style="justify-content: space-evenly;display: flex;flex-flow: row wrap;">
<a class='button' href="https://arxiv.org/abs/2510.21914" aria-label='arXiv link' style="line-height: 1.5">
  <i class="ai ai-arxiv ai-lg" style="color:#b31b1b"></i>&nbsp;&nbsp;<b>arXiv:2510.21914</b>
</a>

<a class='button' href="https://doi.org/10.3847/1538-4357/ae60fd" aria-label='Journal link' style="line-height: 1.5">
  <i class="ai ai-doi fa-lg"></i>&nbsp;&nbsp;<b>Astrophys. J.</b>
</a>

<a class='button' href="https://github.com/Tal-Shpigel/stellar-dm-velocity-distributions" aria-label='GitHub link' style="line-height: 1.5;">
  <i class="fa-brands fa-github fa-lg"></i>&nbsp;&nbsp;<b>GitHub</b>
</a>
</div>
<br>
{% endcomment %}

<div style="color:#767676; display: flex; flex-flow: row wrap; gap: 1em; margin: 1em;">
<a href="https://arxiv.org/abs/2510.21914" aria-label='arXiv link' style="color: inherit;">
<span class="fa-stack" style="width: 2em;">
  <i class="fa-solid fa-circle fa-stack-2x"></i>
  <i class="ai ai-arxiv ai-lg ai-stack-1x" style="color:#b31b1b;"></i>
  <i class="ai ai-arxiv ai-lg ai-stack-1x" style="color:#BDB9B4; transform:scale(-1)"></i>
</span>
&nbsp;&nbsp;<b>arXiv:2510.21914</b>
</a>
<a href="https://doi.org/10.3847/1538-4357/ae60fd" aria-label='Journal link' style="color: inherit;">
<i class="ai ai-doi ai-2x" style='vertical-align: middle;'></i>
&nbsp;&nbsp;<b>Astrophys. J.</b>
</a>
<a href="https://github.com/Tal-Shpigel/stellar-dm-velocity-distributions" aria-label='GitHub link' style="color: inherit;">
<i class="fa-brands fa-github fa-2x" style='vertical-align: middle;'></i>
&nbsp;&nbsp;<b>GitHub</b>
</a>
</div>


The dark matter flux in a direct detection experiment depends on its local speed distribution. This distribution has been inferred from simulations of Milky Way&ndash;like galaxies, but such models serve only as proxies given that no simulation directly captures the detailed evolution of our own Galaxy. This motivates alternative approaches which obtain this distribution directly from observations. In this work, we utilize 98 Milky Way analogues from the <code>TNG50</code> simulation to develop and validate a procedure for inferring the dark matter speed distribution using the kinematics of nearby stars. We find that the dark matter that originated from old mergers, plus that from recent non-luminous accretions, is well described by a Maxwell&ndash;Boltzmann speed distribution centered at the local standard-of-rest velocity. Meanwhile, recently accreted dark matter from massive mergers has speeds that can be traced from the associated stellar debris of these events. The stellar populations systematically underestimate the velocity dispersion of their dark matter counterparts, but a simple kinematic boost brings the two into good alignment. Using the <code>TNG50</code> host galaxies, we demonstrate that combining these two contributions provides an accurate reconstruction of the local dark matter speeds. As  an application of the procedure to our own Galaxy, we utilize stellar kinematic data from _Gaia_ to quantify how the dark matter remnants from the Milky Way's last major merger impact its speed distribution in the Solar neighborhood.

<figure>
  <img src="/assets/research/2510_thumb.png" alt="Local dark matter speed distribution reconstruction">
  <figcaption class='message'>Our reconstruction of the dark matter speed distribution around the Sun. We use the kinematics of observed GSE stars (solid orange) to model the dark matter contributed by the GSE merger (dashed orange). This is added to a Maxwell&ndash;Boltzmann distribution (black) to yield the full model, sampling over our reconstruction uncertainties (green band). </figcaption>
</figure>