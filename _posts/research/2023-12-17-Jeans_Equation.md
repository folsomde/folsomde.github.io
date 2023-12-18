---
title: "The Jeans Equation"
layout: post
categories:
  - Research
tags:
  - Galactic Dynamics
permalink: /:categories/jeans:output_ext
excerpt: "Essentially a highlight reel of Binney & Tremaine Chapter 4"
comments: false
---

<a name="toc"></a>

## Table of Contents 
1. [The Distribution Function](#1)
2. [The Jeans Equations](#2)
3. [Virial Equations](#3)
4. [Further reading](#resources)

---

# The Distribution Function <a name="1"></a>
Let \\(f(\vb{x}, \vb{v}, t)\\) be the probability that something (a star, dark matter, a fluid element) is found at the phase-space coordinate \\((\vb{x},\vb{v})\\) at time \\(t\\). By Liouville's theorem, \\(f\\) has the same numerical value in any canonical coordinate system \\((\vb{q}, \vb{p})\\). 

Probability must be conserved, so we have a continuity equation for the distribution function \\(f(\vb{q}, \vb{p}, t)\\)
<div>\[
  \pdv{f}{t} + \pdv{\vb{q}}(f\dot{\vb{q}}) + \pdv{\vb{p}}(f\dot{\vb{p}}) = 0
\]</div>
which judicious application of Hamilton's equations allows us to write as
<div>\begin{align}
  0&=\pdv{f}{t} + \dot{\vb{q}}\cdot\pdv{f}{\vb{q}} + \dot{\vb{p}}\cdot\pdv{f}{\vb{p}}\\
  &= \pdv{f}{t} + \pdv{f}{\vb{q}}\pdv{H}{\vb{p}} - \pdv{f}{\vb{p}}\pdv{H}{\vb{q}}\\
  &=\pdv{f}{t} + [f,H].
\end{align}</div>

This is particularly nice when \\(H = \frac{1}{2}v^2 + \Phi(\vb{x},t)\\): 
<div class = "message">\[
  \pdv{f}{t} + \dot{\vb{v}}\cdot\pdv{f}{\vb{x}} - \pdv{\Phi}{\vb{x}}\cdot\pdv{f}{\vb{v}} = 0.
\]</div>

Note we have made the assumption that probability is conserved: this is not necessarily true for objects with finite lifetimes. It is still a decent approximation as long as the left hand side (which has characteristic scale \\(1/t_\mathrm{cross}\\)) is much greater than any source/sink rates.



## Moments of \\(f\\)
are particularly interesting quantities:
 - Position-space number density
 <div>\[
  n(\vb{x}) = \int \dd[3]{\vb{v}}f(\vb{x},\vb{v})
\]</div>
 - Mean velocities
 <div>\[
  \bar{\vb{v}}(\vb{x}) = \frac{1}{n(\vb{x})}\int \dd[3]{\vb{v}}\vb{v}\,f(\vb{x},\vb{v})
\]</div>
 - Velocity dispersions (a symmetric tensor)
 <div>\[
  \sigma_{ij}^2(\vb{x}) = \frac{1}{n(\vb{x})}\int \dd[3]{\vb{v}}\, (v_i-\ev*{v_i})(v_j-\ev*{v_j})\,f(\vb{x},\vb{v})
\]</div>

The quantity realistically probed by observation is \\(f\\) projected onto 3D coordinates: two on-sky directions \\(\vb{x}\_\bot\\) and the line-of-sight velocity \\(v\_\parallel\\). **There is a subtlety in B&T's notation here:** the 3D \\(F\\) is defined such that each \\(F(\vb{x}\_\bot)\\) is a PDF of \\(v_\parallel\\)s which integrates to 1. This leads to factors of \\(n\\) being easy to lose! In particular,
<div>\begin{align}
  F(\vb{x}_\bot, v_\parallel) &= \frac{1}{\int\dd{x_\parallel}n(\vb{x})} \int \dd{x_\parallel}\dd[2]{v_\bot}\,f(\vb{x},\vb{v})\\
  &= \frac{1}{\Sigma(\vb{x}_\bot)}\int \dd{x_\parallel}\dd[2]{v_\bot}\,f(\vb{x},\vb{v})
\end{align}</div>
which has an extra factor of the surface density relative to a pure marginal.

The line-of-sight dispersion \\(\sigma^2_\parallel = \mathbb{E}[(v\_\parallel - \bar{v}\_\parallel)^2]\\) will generally be greater than the average intrinsic dispersion along the line of sight:
<div>\begin{align}
  \sigma_\parallel^2(\vb{x}_\bot) &= \int \dd{v_\parallel} \,(v_\parallel - \ev*{v_\parallel})^2\, F(\vb{x}_\bot,v_\parallel)\\
  &= \frac{1}{\Sigma(\vb{x}_\bot)} \int \dd{x_\parallel}\dd[3]{\vb{v}}\, (\hat{\ell}\cdot \vb{v} - \ev*{v_\parallel})^2 f(\vb{x},\vb{v})\\
  &= \frac{1}{\Sigma(\vb{x}_\bot)} \int \dd{x_\parallel}n(\vb{x})\, \qty[\hat{\ell}\cdot \boldsymbol{\sigma}^2 \cdot\hat{\ell} + (\hat{\ell}\cdot\bar{\vb{v}} - \ev*{v_\parallel})^2]
\end{align}</div>
<blockquote>
This is dense. Breaking it down, we start with just a second moment of the 3D projected DF, $F$. Since $F$ is a marginalized version of $f$, reintroduce the $\dd{x_\parallel}\dd[2]{\vb{v}_\bot}$ integration, which brings in that tricky factor of the surface density! Next, rewrite

<div>\begin{align}
  (\hat{\ell}\cdot \vb{v} - \ev*{v_\parallel})^2 &= \qty(\hat{\ell}\cdot (\vb{v} - \bar{\vb{v}}) + (\hat{\ell} \cdot \bar{\vb{v}} - \ev*{v_\parallel}))^2\\
  &= \qty(\hat{\ell}\cdot (\vb{v} - \bar{\vb{v}}))^2 + 2\qty(\hat{\ell}\cdot (\vb{v} - \bar{\vb{v}})(\hat{\ell} \cdot \bar{\vb{v}} - \ev*{v_\parallel})) + (\hat{\ell} \cdot \bar{\vb{v}} - \ev*{v_\parallel})^2
\end{align}</div>
Since $\ev*{v_\parallel} = \mathbb{E}[\hat{\ell}\cdot\vb{v}]$, that middle term integrates to zero, and we're left with the first term, which is the line of sight component of the dispersion tensor (i.e., the intrinsic variance of velocities along the line of sight, which may be naively how one interprets $\sigma^2_\parallel$), plus the second term, which describes how the mean velocity itself varies along the line of sight. 
</blockquote>

Some terminology:
 - **Ergodic** DFs depend only on the energy
 - **Isotropic** systems have \\(\sigma^2\_{ij} = \sigma^2\delta\_{ij}\\). All ergodic systems are isotropic with zero mean velocity.
 - **Self-consistent** DFs are those where the density determines a gravitational potential which is consistent with the potential needed to solve the CBE

## Velocity anisotropy
The **velocity anisotropy** \\(\beta\\) describes the shape of the velocity distribution. 
<div>\[
  \beta(\vb{x}) = 1 - \frac{\sigma_\theta^2 + \sigma_\phi^2}{2\sigma_r^2}
\]</div>
 * If all orbits are circular, \\(\beta = - \infty\\)
 * If velocity distribution is isotropic, \\(\beta = 0\\)
 * If all orbits are radial, \\(\beta = 1\\)

The orientation of the velocity distribution is important for observables: radial bias increases $\sigma_\parallel^2$ at small radii, while tangential bias increases it at large radii. Intuitively, looking at the center of a system means $v_\parallel = v_r$, while at the edges the component we see is $v_\parallel = v_\phi$

Typically, we expect DFs that are near-ergodic near the center (where gravitational interactions happen fast enough to thermalize the system) and which are more radially biased at large radii (stuff's falling in). A simple form for this is an **Osipkov--Merritt** model, with characteristic breaking scale radius $r_a$
<div>\[
  \beta(r) = \frac{1}{1 + (\frac{r_a}{r})^2}
\]</div>

[Return to Table of Contents](#toc)
# The Jeans Equations <a name="2"></a>
Integrating the CBE over all velocities gives what's essentially a continuity equation:
<div>\[
  \pdv{n}{t} + \partial_i(n\ev*{v_i}) = 0
\]</div>

Multiplying by $\vb{v}$ first is more interesting:
<div>\[
  \partial_t(n\ev*{v_i}) + \partial_j(n\ev*{v_iv_j}) + n\partial_i\Phi = 0
\]</div>
which combines with the continuity equation to give what's essentially Euler's equation/the Cauchy momentum equation
<div>\[
  \pdv{\ev*{v_i}}{t} + \ev*{v_j}\pdv{\bar{v_i}}{x_j} = -\pdv{\Phi}{x_i} - \frac{1}{n}\pdv{x_j}(n\sigma^2_{ij})
\]</div>
with a stress tensor \\(-n\sigma_{ij}^2\\) that acts like hydrostatic pressure. These equations are nice because they involve quantities that can reasonably be obtained observationally.

However, even knowing $n(\vb{x})$ and $\Phi$, we have nine unknowns (three mean velocities and six independent dispersions, including the off-diagonal terms) but only these four equations! Higher moments sometimes help furnish more equations, but in general this doesn't help (we need to know higher order correlators of velocities). 

## For spherical, time-independent systems
These assumptions let us drop a lot of derivatives!
Take a Hamiltonian
<div>\[
  H = \frac{1}{2}\qty[p_r^2 + \frac{p_\theta^2\sin^2\theta + p_\phi^2}{r^2\sin^2\theta}] + \Phi(r)
\]</div>
and chuck it into the CBE. Multiplying by $p_r$ and integrating over all momenta gives a Jeans equation
<div>\[
  \pdv{r}(r^2\sin\theta n \ev*{p_r^2})+\pdv{\theta}(\sin\theta n \ev*{p_rp_\theta}) + r^2\sin\theta n \qty(\dv{\Phi}{r} - \frac{\ev*{p_\theta^2}}{r^3} - \frac{\ev*{p_\phi^2}}{r^3\sin^2\theta}) = 0
\]</div>
(yikes). However, since this is a static spherical system the second term must vanish: we average over a single factor of $v_r$. Subbing out the momenta for velocities and using $\beta$ and $\sigma_r^2 = \ev*{v_r^2}$, we have the much nicer
<div class = "message">\[
  \frac{1}{n}\dv{r}(n\sigma_r^2) + 2\frac{\beta}{r}\sigma_r^2 = -\dv{\Phi}{r}
\]</div>

This allows us to map from observed $\sigma_r$s to a $\beta(r)$!

## Axisymmetric, time-independent systems
In short, each $p_i$ moment gives an interesting equation:
<div class = "message">\begin{align}
  r:& & \dv{r}(n\sigma^2_r) + \pdv{z}(n\sigma_{rz}) + n\qty(\frac{\sigma^2_r - \sigma^2_\phi}{r} + \pdv{\Phi}{r}) &= 0\\
  \phi:& & \frac{1}{r^2}\dv{r}(r^2n\sigma_{r\phi}) + \pdv{z}(n\sigma_{z\phi}) &= 0\\
  z:& & \frac{1}{r}\dv{r}(rn\sigma_{rz}) + \pdv{z}(n\sigma_z^2) + n\pdv{\Phi}{z}  &= 0
\end{align}</div>

with $\sigma_i^2 = \ev*{v_i^2}$ and $$\sigma_{ij} = \ev*{v_i v_j}$$ (we're assuming all means are zero).


## In practice
While everything we've thought of so far is in terms of the collisionless system described by $f$, the potential $\Phi$ that governs its motion is something external! Take $-\dv{\Phi}{r} = -\frac{GM(<r)}{r^2}$ and the spherical Jeans equation can be integrated to find a "velocity dispersion profile"
<div>\begin{gather}
  \sigma_r^2 = \frac{1}{n(r)g(r)}\int_r^\infty \frac{GM(\tilde{r})n(\tilde{r})}{\tilde{r}^2}g(\tilde{r})\dd{\tilde{r}} \\
  g(r) = \exp\qty(2\int\frac{\beta(r)}{r}\dd{r})
\end{gather}</div>
With $n$ and $\beta$ and everything describing the tracers of a total mass profile $M$. 
Already, the mass--anisotropy degeneracy is clear: if you see a high dispersion, it's impossible to tell if it's because of a lot of mass or if it's because of anisotropy.
Projecting this along the line of sight gives 
<div>\[
  \sigma^2_\parallel(R) = \frac{2}{\Sigma(R)}\int_R^\infty \qty(1-\beta\frac{R^2}{r^2})\frac{n(r)\sigma_r^2(r)r}{\sqrt{r^2-R^2}}\dd{r}
\]</div>
which is what people actually fit to. 

Further extensions to the Jeans analysis method may use higher-order moments of the velocity distribution via "virial shape parameters" (cf. <a href="https://ui.adsabs.harvard.edu/abs/1990AJ.....99.1548M">Merrifield & Kent (1990)</a>, <a href="https://ui.adsabs.harvard.edu/abs/2014MNRAS.441.1584R/abstract">Richardson & Fairbairn (2014)</a>)
<div>\begin{align}
  v_{s1} &= \frac{2}{5}\int_0^\infty GMn\,(5-2\beta)\sigma_r^2r\dd{r}\\
  &= \int_0^\infty \Sigma(R) \ev*{v_\parallel^4}R\dd{R}\\
  v_{s2} &= \frac{4}{35}\int_0^\infty GMn\,(7-6\beta)\sigma_r^2r^3\dd{r}\\
  &= \int_0^\infty \Sigma(R) \ev*{v_\parallel^4}R^3\dd{R}\\
\end{align}</div>
which help constrain $\beta$ through velocities alone, which breaks some of the mass--anisotropy degeneracy.

[Return to Table of Contents](#toc)
# Virial Equations <a name="3"></a>
What if we took position moments instead of momentum moments? 
_(coming soon)_

[Return to Table of Contents](#toc)
# Further reading <a name="resources"></a>
 - Binney & Tremaine of course. This is a lot of Chapter 4
 - <a href="https://ui.adsabs.harvard.edu/abs/2017MNRAS.471.4541R/abstract">Read & Steger (2017)</a>: nice mini-review
 - <a href="https://ui.adsabs.harvard.edu/abs/2014JPhG...41f3101R/abstract">Read (2014)</a>: other ways of doing mass modeling
 - <a href="https://galaxiesbook.org/chapters/I-04.-Equilibria-Spherical-Collisionless-Systems.html">Jo Bovy's book</a> which is basically this page but with code and greater depth/pedagogical utility