---
title: "Probabilistic Inference of the Structure and Orbit of Milky Way Satellites with Semi-Analytic Modeling"
layout: post
categories:
  - Research
tags:
  - Papers
  - Research
permalink: /:categories/semianalytic_modeling
excerpt: It can be difficult to extrapolate from observed properties of dwarf galaxies to properties of their dark matter halos. In this work, I propose a procedure to do this using the <code>SatGen</code> semi-analytic model, which efficiently samples over astrophysical uncertainties such as the stellar mass&ndash;halo mass relation and baryonic feedback perscriptions. This approach provides realistic correlated uncertainties and aids interpretability beyond simple empirical scaling relations. The method is easily extensible and my code is publicly available.
comments: false
# thumbnail: "/assets/research/2311_thumb.png"
---
<a href="https://ui.adsabs.harvard.edu/abs/2025MNRAS.536.2891F/abstract">arXiv:2311.05676</a>, published in <a href="https://doi.org/10.1093/mnras/stae2736">MNRAS, <b>536</b>, 2891 (2025)</a>.  
Data available <a href='https://github.com/folsomde/Semianalytic_Inference'>on GitHub</a>

---
Semi-analytic modelling furnishes an efficient avenue for characterizing dark matter haloes associated with satellites of Milky Way&ndash;like systems, as it easily accounts for uncertainties arising from halo-to-halo variance, the orbital disruption of satellites, baryonic feedback, and the stellar-to-halo mass (SMHM) relation. We use the SatGen semi-analytic satellite generator, which incorporates both empirical models of the galaxy&ndash;halo connection as well as analytic prescriptions for the orbital evolution of these satellites after accretion onto a host to create large samples of Milky Way&ndash;like systems and their satellites. By selecting satellites in the sample that match observed properties of a particular dwarf galaxy, we can infer arbitrary properties of the satellite galaxy within the cold dark matter paradigm. For the Milky Way's classical dwarfs, we provide inferred values (with associated uncertainties) for the maximum circular velocity $v_\mathrm{max}$ and the radius $r_\mathrm{max}$ at which it occurs, varying over two choices of baryonic feedback model and two prescriptions for the SMHM relation. While simple empirical scaling relations can recover the median inferred value for $v_\mathrm{max}$ and $r_\mathrm{max}$, this approach provides realistic correlated uncertainties and aids interpretability. We also demonstrate how the internal properties of a satellite's dark matter profile correlate with its orbit, and we show that it is difficult to reproduce observations of the Fornax dwarf without strong baryonic feedback. The technique developed in this work is flexible in its application of observational data and can leverage arbitrary information about the satellite galaxies to make inferences about their dark matter haloes and population statistics.

<figure>
  <img src="/assets/research/2311_thumb.png" alt="The inferred v max and r max for the Fornax dwarf spheroidal, in two different feedback models.">
  <figcaption class='message'>The inferred $v_\mathrm{max}$ and $r_\mathrm{max}$ for the Fornax dwarf spheroidal, in two different feedback models. Without strong feedback, the only way to generate a Fornax-like stellar mass and velocity dispersion simultaneously is via extreme tidal stripping. With the cores provided by strong feedback, Fornax-like galaxies are more consistent with larger $v_\mathrm{max}$ halos.</figcaption>
</figure>