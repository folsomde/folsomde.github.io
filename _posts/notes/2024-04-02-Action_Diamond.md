---
title: "Action Spaces"
layout: post
categories:
  - Notes
tags:
  - Galactic Dynamics
  - Research
  - Notes
permalink: /:categories/action_diamond
excerpt: "An explanation of that weird plot"
comments: false
published: false
---

# Action -- Angle variables

# The Action Diamond
## Definitions
The horizontal axis here is taken to be \\(J_\phi/J_\mathrm{tot}\\), a scaled version of good ol' angular momentum (at least in an axisymmetric potential). To the right are prograde orbits, to the left are retrograde orbits, and in the center are radial orbits which do not have any \\(L_z\\). The left- and rightmost points have \\(|J_\phi| = J_\mathrm{tot}\\), and therefore correspond to orbits with no vertical or radial oscillation, i.e. perfectly circular, perfectly in-plane orbits. 

The vertical axis is trickier: it's taken to be \\((J_z - J_r)/J_\mathrm{tot}\\). The intuition for \\(J_z\\) and \\(J_r\\) is that they're related to the maximum spatial extent of oscillations in these directions. Large \\(J_z\\) means that the orbit oscillates over a large range of height, and large \\(J_r\\) means that the orbit oscillates over a large range of cylindrical radius. Therefore, points higher on the vertical axis have small radial oscillations relative to their height oscillations, i.e., they are more circular when viewed top-down. On the other hand, points lower on the vertical axis have smaller height oscillations relative to their radial oscillations, i.e., these orbits are more fixed in-plane. The top corner of the diamond corresponds to a radial orbit passing directly from pole to pole, and the bottom corner corresponds to a radial orbit lying in-plane. 

The choice of \\(J_\mathrm{tot} = J_r + J_z + |J_\phi|\\) leads to the characteristic diamond shape; normalizing by the sum of components in quadrature would form a circle. Note that this normalization means populations with different total action may land in the same region of the plot despite being physically distinct! Care should be taken not to directly compare populations with wildly different \\(J_\mathrm{tot}\\) without this caveat in mind.

## Interpretation
As stated above, the corners have straightforward interpretations:
 - Left corner: perfectly circular, in-plane, retrograde orbit
 - Right corner: perfectly circular, in-plane, prograde orbit
 - Top corner: perfectly radial, out-of-plane, polar orbit
 - Bottom corner: perfectly radial, in-plane orbit

And the edges also are clear:
 - Top edges: \\(J_r = 0\\), fixed to one cylindrical radius (circular)
 - Bottom edges: \\(J_z = 0\\), fixed to one height (in-plane)

The horizontal axis roughly corresponds to orbital inclination, and the vertical to the eccentricity (?)

# Further reading <a name="resources"></a>
This summary is cobbled together from a handful of resources:
 - Binney & Tremaine 3.5
 - <a href="https://ui.adsabs.harvard.edu/abs/2022MNRAS.510.5119L/abstract">Lane et al. (2022)</a>

binney 2012 has a mini speedrun of the classmech invovled