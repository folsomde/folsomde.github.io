---
title: "Ubiquitous Corotation of Dark Matter Halos: Implications for Direct Detection"
layout: post
categories:
  - Research
tags:
  - Papers
  - Research
  - Simulations
permalink: /:categories/corotation
excerpt: "I show that the halo-to-halo variance that sets the astrophysical uncertainty in direct detection limits is not irreducible, but instead depends on a measurable property of the Milky Way: the rotational velocity of the dark halo. Dark matter halos generically rotate with the baryonic disk, and the degree of this rotation correlates strongly with the expected signal rates in terrestrial detectors."
comments: false
---

<div style="color:#767676; display: flex; flex-flow: row wrap; gap: 1em; margin: 1em;">
<a href="https://arxiv.org/abs/2608.00161" aria-label='arXiv link' style="color: inherit;">
<span class="fa-stack" style="width: 2em;">
  <i class="fa-solid fa-circle fa-stack-2x"></i>
  <i class="ai ai-arxiv ai-lg ai-stack-1x" style="color:#b31b1b;"></i>
  <i class="ai ai-arxiv ai-lg ai-stack-1x" style="color:#BDB9B4; transform:scale(-1)"></i>
</span>
&nbsp;&nbsp;<b>arXiv:2608.00161</b>
</a>
{% comment %}
<a href="https://doi.org/10.1103/wmpq-mw4h" aria-label='Journal link' style="color: inherit;">
<i class="ai ai-doi ai-2x" style='vertical-align: middle;'></i>
&nbsp;&nbsp;<b>Phys. Rev. Lett.</b>
</a>
<a href="https://github.com/folsomde/DM_velocity_distributions" aria-label='GitHub link' style="color: inherit;">
<i class="fa-brands fa-github fa-2x" style='vertical-align: middle;'></i>
&nbsp;&nbsp;<b>GitHub</b>
</a>
{% endcomment %}
</div>

Cosmological simulations have recently begun to quantify the halo-to-halo variance in the phase-space distribution of dark matter around the Sun.
We use a sample of nearly one hundred Milky Way&ndash;like galaxies from the `TNG50` simulation to determine what aspects of this variance control the predictions for dark matter direct detection. Contrary to the isotropy assumed in the standard halo model, we find the dark matter median azimuthal velocity is nonzero and preferentially *corotating,* i.e., in the direction of the baryonic disk's rotation, ranging from 6&ndash;70 km/s (16th&ndash;84th percentile). This corotation suppresses predicted scattering rates in laboratory experiments searching for dark matter lighter than 50 GeV and significantly affects the expected daily modulation amplitude for directional detectors. In particular, this induces a 21% uncertainty on the upper limit of the dark matter&ndash;nucleon interaction cross section at peak sensitivity for a typical isotropic ton-scale experiment.
This uncertainty is not irreducible, however: it is strongly correlated with the rotational velocity. If studies of the Milky Way's formation history determine the rotation speed, this astrophysical uncertainty is reduced to 7%.

<figure>
  <img src="/assets/research/2608_thumb.png" alt="Dark matter speed distributions, colored by the corotation speed">
  <figcaption class='message'>Geocentric speed distributions for dark matter in the solar neighborhood. The <code>TNG50</code> halos are colored by the median dark matter azimuthal velocity. Halos with stronger corotation (blue) exhibit slower geocentric speeds. Halos that rotate in the opposite direction from the baryonic disk (red) have a headwind from this rotation, boosting the geocentric speeds relative to the standard halo model (dashed black).</figcaption>
</figure>