---
title: "Semi-analytic Inference of Satellite Densities in the Cold Dark Matter Model"
layout: post
categories:
  - Research
tags:
  - Papers
  - Research
  - Semianalytics
permalink: /:categories/dwarf_densities
excerpt: In Part I of this series, we show a discrepancy between UFD velocity dispersions and expectations for these kinematics from their luminosities. In Part II, we explore the implications of this for the indirect detection of dark matter, showing that it results in a factor of 2&ndash;4 uncertainty in the upper limits for the annihilation cross section.
comments: false
---

---
<div style="color:#767676; display: flex; flex-flow: row wrap; gap: 1em; margin: 1em;">
<a href="https://arxiv.org/abs/2607.27316" aria-label='arXiv link' style="color: inherit;">
<span class="fa-stack" style="width: 2em;">
  <i class="fa-solid fa-circle fa-stack-2x"></i>
  <i class="ai ai-arxiv ai-lg ai-stack-1x" style="color:#b31b1b;"></i>
  <i class="ai ai-arxiv ai-lg ai-stack-1x" style="color:#BDB9B4; transform:scale(-1)"></i>
</span>
&nbsp;&nbsp;<b>arXiv:2607.27316</b>
</a>
{% comment %}
<a href="https://doi.org/10.1103/wmpq-mw4h" aria-label='Journal link' style="color: inherit;">
<i class="ai ai-doi ai-2x" style='vertical-align: middle;'></i>
&nbsp;&nbsp;<b>Phys. Rev. Lett.</b>
</a>
{% endcomment %}
<a href="https://github.com/kailashraman/SatelliteDensityInference" aria-label='GitHub link' style="color: inherit;">
<i class="fa-brands fa-github fa-2x" style='vertical-align: middle;'></i>
&nbsp;&nbsp;<b>GitHub</b>
</a>
</div>

## Part I
 Ultra-faint dwarf galaxies are critical testing grounds for probing the limits of galaxy formation in the cold dark matter (CDM) paradigm. Employing a semi-analytic cosmological satellite generator that captures the expected CDM halo population, we estimate Milky Way dwarf density profiles through two methods: a kinematic approach using stellar velocity dispersions and a separate method based on dwarf stellar masses. The kinematic approach yields a larger diversity in central dark matter densities than expected from the CDM population, as inferred from the stellar-to-halo mass relation, with compact ultra-faints appearing overdense and larger systems appearing underdense. For the ultra-faint dwarfs with at least 10 stars with spectroscopic measurements, this discrepancy persists at the ~2.4&#963; level across all considered systematic variations on the semi-analytic modeling. Our framework introduces a novel, robust procedure for testing the consistency of the observed population of Milky Way satellites with cosmological expectations. As future surveys discover new dwarf satellites and refine stellar velocity measurements, updating this analysis will provide an increasingly stringent test of the CDM paradigm. 

<figure>
  <img src="/assets/research/2607_thumb_I.png" alt="Discrepancy between the observed kinematics and the kinematics predicted by the UFD luminosities">
  <figcaption class='message'>The discrepancy between ultra-faint dwarf observed kinematics (scatterpoints, with best-fit power law in tan) and the expectations for those kinematics from the dwarf luminosities (following two different stellar mass&ndash;halo mass relations, in blue and green). In general, the smaller-sized galaxies at the left of the figure appear more dense than expected given their low luminosities, and the larger galaxies at the right of the figure tend not to be as massive as expected, regardless of the stellar mass&ndash;halo mass relation used.</figcaption>
</figure>

---

<div style="color:#767676; display: flex; flex-flow: row wrap; gap: 1em; margin: 1em;">
<a href="https://arxiv.org/abs/2607.27326" aria-label='arXiv link' style="color: inherit;">
<span class="fa-stack" style="width: 2em;">
  <i class="fa-solid fa-circle fa-stack-2x"></i>
  <i class="ai ai-arxiv ai-lg ai-stack-1x" style="color:#b31b1b;"></i>
  <i class="ai ai-arxiv ai-lg ai-stack-1x" style="color:#BDB9B4; transform:scale(-1)"></i>
</span>
&nbsp;&nbsp;<b>arXiv:2607.27326</b>
</a>
{% comment %}
<a href="xxx" aria-label='Journal link' style="color: inherit;">
<i class="ai ai-doi ai-2x" style='vertical-align: middle;'></i>
&nbsp;&nbsp;<b>Journal Name</b>
</a>
{% endcomment %}
<a href="https://github.com/kailashraman/DwarfJeansAnalysis" aria-label='GitHub link' style="color: inherit;">
<i class="fa-brands fa-github fa-2x" style='vertical-align: middle;'></i>
&nbsp;&nbsp;<b>GitHub</b>
</a>
</div>

## Part II
Dwarf galaxies provide excellent targets to search for signals of dark matter annihilation or decay. Using a calibrated semi-analytic model and the latest stellar kinematic data (presented in Part I), this paper updates the astrophysical <i>J</i>-factors for the Milky Way’s dwarf spheroidal galaxies. We infer the probability distributions for the <i>J</i>-factors of 39 dwarfs by conditioning a population of subhalos, generated with the SatGen semi-analytic satellite model, on either a dwarf’s kinematically determined dynamical mass or its stellar mass. We also compute the <i>J</i>-factors using the Jeans equation with updated stellar kinematics and priors that incorporate varying degrees of SatGen information. We use the computed <i>J</i>-factors to recast existing limits from Fermi-LAT data on the annihilation cross section. Our main result is that variations in the <i>J</i>-factors computed using the Jeans analysis introduce a factor of 2&ndash;4 uncertainty into the inferred limits on the cross section. We argue that a cosmologically informed prior is a motivated choice that excludes thermal relic annihilation cross sections to <i>b</i><i style="text-decoration: overline;">b</i> below about 70 GeV. For comparison, the more commonly used priors, which can lead to unphysical halo parameters, exclude masses below 130 GeV at 95% confidence level. We also show that the highest&ndash;<i>J</i>-factor dwarfs are spatially extended, approximately one degree on the sky, which challenges the validity of the point-source approximation adopted in many analyses of Fermi data. Finally, based on the semi-analytic model and the kinematic data, the highest <i>J</i>-factor halos have already been discovered, suggesting future ultra-faint discoveries are unlikely to substantially strengthen limits on annihilating dark matter.

<figure>
  <img src="/assets/research/2607_thumb_II.png" alt="Prior-dependence of the dark matter annihilation upper limits">
  <figcaption class='message'>The prior-dependence of dark matter annihilation upper limits from the Milky Way's satellites. Standard Jeans analyses set very wide priors that permit unreasonably massive halos for the dwarf galaxies, which in tern set overly strong limits (dashed black). With cosmologically-informed priors, the limits may be set much weaker (e.g., dotted black).</figcaption>
</figure>