---
title: "Probabilistic Inference of the Structure and Orbit of Milky Way Satellites with Semi-Analytic Modeling"
layout: post
categories:
  - Research
tags:
  - Papers
  - Research
  - Semianalytics
permalink: /:categories/semianalytic_modeling
excerpt: It can be difficult to extrapolate from observed properties of dwarf galaxies to properties of their dark matter halos. I propose a procedure to do this using the <code>SatGen</code> semi-analytic model, which efficiently samples over astrophysical uncertainties such as the stellar mass&ndash;halo mass relation and baryonic feedback perscriptions. This approach provides realistic correlated uncertainties and aids interpretability beyond simple empirical scaling relations. The method is easily extensible and my code is publicly available.
comments: false
# thumbnail: "/assets/research/2311_thumb.png"
---

<div style="color:#767676; display: flex; flex-flow: row wrap; gap: 1em; margin: 1em;">
<a href="https://arxiv.org/abs/2311.05676" aria-label='arXiv link' style="color: inherit;">
<span class="fa-stack" style="width: 2em;">
  <i class="fa-solid fa-circle fa-stack-2x"></i>
  <i class="ai ai-arxiv ai-lg ai-stack-1x" style="color:#b31b1b;"></i>
  <i class="ai ai-arxiv ai-lg ai-stack-1x" style="color:#BDB9B4; transform:scale(-1)"></i>
</span>
&nbsp;&nbsp;<b>arXiv:2311.05676</b>
</a>
<a href="https://doi.org/10.1093/mnras/stae2736" aria-label='Journal link' style="color: inherit;">
<i class="ai ai-doi ai-2x" style='vertical-align: middle;'></i>
&nbsp;&nbsp;<b>Mon. Not. R. Astron. Soc.</b>
</a>
<a href="https://github.com/folsomde/Semianalytic_Inference" aria-label='GitHub link' style="color: inherit;">
<i class="fa-brands fa-github fa-2x" style='vertical-align: middle;'></i>
&nbsp;&nbsp;<b>GitHub</b>
</a>
</div>

Semi-analytic modelling furnishes an efficient avenue for characterizing dark matter haloes associated with satellites of Milky Way&ndash;like systems, as it easily accounts for uncertainties arising from halo-to-halo variance, the orbital disruption of satellites, baryonic feedback, and the stellar-to-halo mass (SMHM) relation. We use the SatGen semi-analytic satellite generator, which incorporates both empirical models of the galaxy&ndash;halo connection as well as analytic prescriptions for the orbital evolution of these satellites after accretion onto a host to create large samples of Milky Way&ndash;like systems and their satellites. By selecting satellites in the sample that match observed properties of a particular dwarf galaxy, we can infer arbitrary properties of the satellite galaxy within the cold dark matter paradigm. For the Milky Way's classical dwarfs, we provide inferred values (with associated uncertainties) for the maximum circular velocity <i>v</i><sub>max</sub> and the radius <i>r</i><sub>max</sub> at which it occurs, varying over two choices of baryonic feedback model and two prescriptions for the SMHM relation. While simple empirical scaling relations can recover the median inferred value for <i>v</i><sub>max</sub> and <i>r</i><sub>max</sub>, this approach provides realistic correlated uncertainties and aids interpretability. We also demonstrate how the internal properties of a satellite's dark matter profile correlate with its orbit, and we show that it is difficult to reproduce observations of the Fornax dwarf without strong baryonic feedback. The technique developed in this work is flexible in its application of observational data and can leverage arbitrary information about the satellite galaxies to make inferences about their dark matter haloes and population statistics.

<figure>
  <img src="/assets/research/2311_thumb.png" alt="The inferred v max and r max for the Fornax dwarf spheroidal, in two different feedback models.">
  <figcaption class='message'>The inferred <i>v</i><sub>max</sub> and <i>r</i><sub>max</sub> for the Fornax dwarf spheroidal, in two different feedback models. Without strong feedback, the only way to generate a Fornax-like stellar mass and velocity dispersion simultaneously is via extreme tidal stripping. With the cores provided by strong feedback, Fornax-like galaxies are more consistent with larger <i>v</i><sub>max</sub> halos.</figcaption>
</figure>