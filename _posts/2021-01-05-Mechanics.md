---
title: "Mechanics Notes"
layout: post
categories:
  - Prelims
  - Notes
tags:
  - Mechanics
permalink: /:categories/mechanics:output_ext
comments: false
---
(under construction)
<a name="toc"></a>

## Table of Contents 
1. [Lagrangians Overview](#chapter1)
2. [Hamiltonians](#chapter2)
3. [Oscillations](#chapter3)
4. [The Central Force Problem](#chapter4)
5. [Scattering Theory](#chapter5)
6. [Rigid Body Motion](#chapter6)
7. [Continuous Media](#chapter7)

---

## Lagrangians Overview <a name="chapter1"></a>

Assuming Newton's second, we derive the euler lagrange equations
<div><div>\begin{equation}
	m\ddot{\vb{r}}_\alpha = -\nabla V\eval{}_{\vb{r}_\alpha} + \vb{F}_\alpha^{\text{n-c}} \implies \dv{t}\pdv{L}{\dot{q}}-\pdv{L}{q} = \sum\pdv{\vb{r}_\alpha}{q}\cdot \vb{F}_\alpha^\text{n-c}
\end{equation}</div></div>
where we absorb the conservative forces into $L$. Some nonconservative forces can also be written as a velocity-dependent potential; an example is the Rayleigh dissipation function 
<div>\begin{equation}
\mathcal{F} = \frac{1}{2}\sum(k_x v_{ix}^2 + k_y v_{iy}^2 + k_z v_{iz}^2)
\end{equation}</div>
for which the force is given by 
<div>\begin{equation}
\pdv{\vb{r}_\alpha}{q}\cdot \vb{F}_\alpha^\text{n-c} = -\pdv{\mathcal{F}}{\dot{q}_j}
\end{equation}</div>
if there is a dissipation function $\mathcal{F}$, we have
<div>\begin{equation}
	\dv{h}{t} = - 2\mathcal{F} - \pdv{L}{t}
\end{equation}</div> 
as the rate of energy loss.

### Constraints and Lagrange Multipliers
Fun vocabulary:
<bl>
	<li> A <em>holonomic</em> constraint is one that can be written $f(\vb{r}_1,\, \vb{r}_2,\,\dots;\;t) = 0$</li>
	<li> A <em>rheonomous</em> constraint is one that contains a dependence on time. Otherwise, the constraint is called <em>scleronomous</em></li>
	<li> A <em>semiholonomic</em> constraint is one that can be written in the form $f(q,\, \dot{q}) = 0$ or, often, $a_{i} \dd{q_i} + a_{t} \dd{t} = 0$</li>
</bl>



<br>We include these constraints using Lagrange multipliers:
<ol>
	<li> Since the constraint equations $f_\alpha$ are identically zero, we can say
<div>\begin{equation}
\delta\int(L-\lambda^\alpha(t) f_\alpha) \dd{t} = 0
\end{equation}</div>
	</li>
	<li> Solving the variation gives the nonhomogeneous Euler-Lagrange equations for forces of constraint
<div>\begin{equation}
	\dv{t}\pdv{L}{\dot{q}}-\pdv{L}{q} = \sum \lambda^\alpha \qty[\pdv{f_\alpha}{q} - \dv{t}\pdv{f_\alpha}{\dot{q}}] - \dv{\lambda^\alpha}{t} \pdv{f_\alpha}{\dot{q}}
\end{equation}</div>
	Note that this right hand side simplifies a lot if the constraint is holonomic
	</li>
</ol>

### Conserved quantities
cyclic coords (lagrangian does not explictly depend on them) immediately give conserved quantities, and typically energy is conserved as well. 

Noethers theorem says if
<div>\begin{equation}
 q_i\to q_i+\delta q_i \implies \delta L = \dv{f}{t} 
\end{equation}</div>
for some $f(q,\,t)$, then $Q=p_i\delta q^i - f$ is constant when the EoM is followed


[Return to Table of Contents](#toc)
## Hamiltonians <a name="chapter2"></a> 
<div>\begin{equation}
	H(p,\,q) = p_i\dot{q}^i - L
\end{equation}</div>
with equations of motion
<div>\begin{equation}
	\pdv{H}{q}=-\dot{p}\qq{and}\pdv{H}{p}=\dot{q}
\end{equation}</div>

[Return to Table of Contents](#toc)
## Oscillations <a name="chapter3"></a>
### One dimension: driving and damping
Consider the EoM 
<div>\begin{equation}
	m\ddot{x} = -kx -\gamma\dot{x}+F_D(t)
\end{equation}</div>
define the undamped frequency and the quality factor
<div>\begin{equation}
	\omega_0 = \sqrt{\frac{k}{m}} \qquad Q = \frac{\sqrt{mk}}{\gamma} \implies \ddot{x} + \frac{\omega_0}{Q}\dot{x} + \omega_0^2x = \frac{1}{m}F_D
\end{equation}</div>
if we take $x\sim e^{rt}$ and solve the homogeneous, we get the characteristic equation
<div>\begin{equation}
	r^{2}+\frac{\omega_0}{Q}r + \omega_0^2 = 0\implies r_{\pm} = \frac{\omega_0}{2Q}\qty[-1\pm\sqrt{1-4Q^2}] 
\end{equation}</div>
which has three cases:
<bl>
	<li> $Q> 1/2$ "underdamped" &mdash; decaying packet times an oscillatory solution</li>
	<div>\begin{equation}
		x(t) = e^{-\omega_0t/2Q} \cos(\omega_0\sqrt{1-1/4Q^2} + \phi)
	\end{equation}</div>
	<li> $Q=1/2$ "critically damped"</li>
	<div>\begin{equation}
		x(t) = [x_0 + (v_0+x_0\omega_0)t]e^{-\omega_0t}
	\end{equation}</div>
	you can shove it hard enough to overshoot the equilibrium point but it'll approach it exponentially from there 
	<li> $Q> 1/2$ "overdamped" &mdash; real and distinct roots give a lincomb</li>
	<div>\begin{equation}
		x(t) = Ae^{r_+t} + Be^{r_-t}
	\end{equation}</div>
</bl>

<br>To get a particular solution in the case of a driving force, generally nice to solve in the complex plane. $x = \Re[z(t)]$ for $z(t) = Ae^{-i\omega t}$ where $\omega$ is the driving frequency and $A$ is in general complex. We can pull this out into a real amplitude and a phase lag. For a periodic driving force, we get resonance: $|A|$ is big when $\omega\sim\omega_0$ and $Q$ large. 
<div>\begin{equation}
	|A| \text{ maximized when }\omega = \omega_0\sqrt{1-1/2Q^2}
\end{equation}</div>
in $A-\omega$ space this gives a lorentzian with width $\Gamma = \omega/Q$ that looks like
<div>\begin{equation}
	A(\omega) \sim \frac{\Gamma^2/4}{(\omega-\omega_0)^2+\Gamma^2/4}E_\text{max}
\end{equation}</div>

### Higher dimensions
If we have a Lagrangian of the form
<div>\begin{equation}
	L = \frac{1}{2}T_{ij}\dot{q}_i\dot{q}_j - \frac{1}{2}V_{ij}q_iq_j + \mathcal{O}(q^3) = \frac{1}{2}\dot{\vb{q}}^T\mathbb{T}\dot{\vb{q}} - \frac{1}{2}\vb{q}^T\mathbb{V}\vb{q}
\end{equation}</div>
then the equations of motion read
<div>\begin{equation}
	T_{ij}\ddot{q}_j + V_{ij}q_j = 0 \implies q_j = v_je^{i\omega t} \implies (-\omega^2 \mathbb{T} + \mathbb{V})\vb{v} = 0
\end{equation}</div>
so we find valid $\omega^2$s by $\det(-\omega^2\mathbb{T}-\mathbb{V}) = 0$, and the sign determines the time dependence of $q$:
<bl>
	<li> if $\omega^2_\alpha > 0$, $\vb{q} = \vb{v}_\alpha\qty[A_\alpha\cos(\omega t) + B_\alpha\sin(\omega t)]$</li>
	<li> if $\omega^2_\alpha = 0$, $\vb{q} = \vb{v}_\alpha\qty[A_\alpha t + B_\alpha]$</li>
	<li> if $\omega^2_\alpha < 0$, $\vb{q} = \vb{v}_\alpha\qty[A_\alpha e^{|\omega_\alpha|t} + B_\alpha e^{-|\omega_\alpha|t}]$</li>
</bl>
and the different $\vb{v}_\alpha$ are $\mathbb{T}$-orthornomal, meaning
<div>\begin{equation}
	\vb{v}_\alpha^T\mathbb{T}\vb{v}_\beta = \delta_{\alpha\beta}
\end{equation}</div>
so in a 2D system knowing one determines the other

[Return to Table of Contents](#toc)
## The Central Force Problem <a name="chapter4"></a>
<div>\begin{equation}
	L = \frac{1}{2}m\dot{r}^2 + \frac{1}{2}m(r\dot{\phi})^2 - V(r)
\end{equation}</div>
can transform to the hammy or to the routhian ($R= p_\phi \dot{\phi}-L$, but we leave $r$ as in the lagrangian formalism)
<div>\begin{equation}
	H = \frac{p_r^2}{2m} + \underbrace{\frac{p_\phi^2}{2mr^2} + V(r)}_{V_\text{eff}}
\end{equation}</div>
we usually care about $r(\phi)$, so we convert the time derivatives to phi derivatives:
<div>\begin{equation}
	\dot{r} = \dv{r}{\phi}\dot{\phi}=r'\frac{p_\phi}{mr^2}\implies E = \frac{p_\phi^2}{2m}\frac{r'^2}{r^4} + V_\text{eff}
\end{equation}</div>
note it's also often nice to swap variables to $u = 1/r$

### The Kepler problem
<div>\begin{align}
	 E &= \frac{p_\phi^2}{2m}\frac{r'^2}{r^4} +\frac{p_\phi^2}{2mr^2} -\frac{k}{r} \\
	 &=  \frac{p_\phi^2}{2m}u'^2 +\frac{p_\phi^2}{2m}u^2 -ku\\
	 &= \frac{p_\phi^2}{2m}\qty[u'^2 + \qty(u- \frac{km}{p_\phi^2})^2] - \frac{mk^2}{2p_\phi^2}
\end{align}</div>
which is an offset SHO! customary names:
<div>\begin{gather}
	u_0 = \frac{km}{p_\phi^2} = \frac{1}{p} \qquad \varepsilon = Ap \implies r(\phi) = \frac{p}{1+\varepsilon\cos(\phi-\phi_0)}\\
	E = \frac{p_\phi^2}{2m}A^2 - \frac{mk^2}{2p_\phi^2} = \frac{k}{2p}(\varepsilon^2-1)
\end{gather}</div>

geometry of an ellipse:
<bl>
	<li> $a$: semimajor axis, $2a= r_\text{min} + r_\text{max} = 2p/(1-\epsilon^2)$</li>
	<li> $b$: semiminor axis, hard to find explicitly so use pythagorean thm</li>
	<li> $c$: focus to center distance: $2c=r_\text{max}-r_\text{min}=2p\varepsilon/(1-\epsilon^2)=2\varepsilon a$</li>
	<li> $r_\text{min} = p/(1+\varepsilon)$</li>
	<li> $r_\text{max} = p/(1-\varepsilon)$</li>
</bl>


### The Laplace-Runge-Lenz vector
For a general central force, where $\dot{\vb{p}} = f(r)\frac{\vb{r}}{r}$, we can show
<div>\begin{equation}
\dv{t}\qty(\vb{p}\times\vb{L}) = -mr^2\,f(r) \dv{t}(\frac{\vb{r}}{r})
\end{equation}</div>
in the Kepler problem, where $f(r) = -\frac{k}{r^2}$, this ensures the conservation of the vector
<div>\begin{equation}
\vb{A} = \vb{p}\times\vb{L} -mk\frac{\vb{r}}{r}
\end{equation}</div>
This vector lies in the plane of orbit, and $A^2 = m^2k^2 + 2mE\ell^2$.


[Return to Table of Contents](#toc)
## Scattering Theory <a name="chapter5"></a>
This is kinda a mess of angle names and things, but the crucial thing to remember is
<div>\begin{equation}
	\dv{\sigma}{\Omega} = \frac{2\pi b\dd{b}}{2\pi\sin\theta\dd{\theta}} = \frac{b}{\sin\theta}\dv{b}{\theta}
\end{equation}</div>

[Return to Table of Contents](#toc)
## Rigid Body Motion <a name="chapter6"></a>
tree main types of problems:
<bl>
	<li> torque free motion: can precess, rotation about intermediate axis unstable</li>
	<li> nonzero torque, eg weighted top: precession about vertical, axis of rotation can change (nutation)</li>
	<li> rolling without slipping</li>
</bl>
components of rotational motion:
<bl>
	<li> rotation about an axis</li>
	<li> precession of this axis (change in $\phi$)</li>
	<li> nutation (change in spherical $\theta$), bobbing as it precesses</li>
</bl>


basic strategy: decompose motion into CM + movement about the CM
<div>\begin{gather}
	\vb{F}_\text{ext} = M \vb{a}_\text{CM} \qquad \vb{r}_\text{CM}\times\vb{F}_\text{ext} = \dv{t}\vb{L}_\text{CM}=\vb{N}_\text{about CM}\\
	\vb{L}_\text{tot} = \underbrace{\vb{L}_\text{CM}}_{\mathclap{\vb{r}_\text{CM}\times M\vb{v}_\text{CM}}} + \vb{L}_\text{about CM} \qquad T = T_\text{CM} + T_\text{rot}
\end{gather}</div>

In general, if a vector $\vb{A}$ of fixed length rotates with an angular velocity $\vb*{\omega}$, then
<div>\begin{equation}
	\dv{\vb{A}}{t} = \vb*{\omega}\times\vb{A}
\end{equation}</div>
In particular, when measuring $\vb{r}$ from a point $\vb{R}$ on a rotating body,
<div>\begin{equation}
	\qty(\dv{\vb{r}}{t})_f = \qty(\dv{\vb{r}}{t})_r + \vb*{\omega}\times\vb{r}
\end{equation}</div>
and we typically take $p$ to be the CM. Taking the second derivative,
<div>\begin{equation}
	\vb{a}_f = \vb{a}_r + \underbrace{\ddot{\vb{R}}_f}_{\mathclap{\text{translation}}} + \underbrace{\dot{\omega}\times\vb{r}}_{\mathclap{\text{rotation}}} + \underbrace{2\omega\times\vb{v}_r}_{\mathclap{\text{coriolis}}} +\underbrace{\omega\times(\omega\times \vb{r})}_{\mathclap{\text{centrifugal}}}
\end{equation}</div>
Note that if we have angular momentum in a fixed frame, we can look at the torque in the fixed frame by considering $\dv{L}{t}$ in the body frame; this gives us Euler's equations

### Inertia tensor
We define the inertia tensor by
<div>\begin{equation}
	I_{jk} = \int \rho(\vb{r})\,(r^2\delta_{ij} - x_ix_j)\dd{V}
\end{equation}</div>


With $\vb{L} = \mathbb{I}\cdot\vb*{\omega}$, kinetic energy is given by
<div>\begin{equation}
	T = \frac{1}{2}\vb*{\omega}\cdot\mathbb{I}\cdot\vb*{\omega} = \frac{1}{2}\vb{L}\cdot\mathbb{I}^{-1}\cdot\vb{L}
\end{equation}</div>
We can diagonalize $\mathbb{I}$ using principle axes, which in general are time-dependent. 


Forget about the parallel axis theorem, but it's good to know the 

**perpendicular axis theorem:** For a planar object, the sum of the moments of inertia in the plane equals the moment of inertia perpendicular to the plane
<div>\begin{equation}
	I_{1,\,\parallel} + I_{2,\,\parallel} = I_\bot 
\end{equation}</div>


Table of $I$s for basic shapes (memorize these):
<table>
	<tr>
    <th>Shape</th>
    <th>Rotation</th>
    <th>Moment of Inertia</th>
  </tr>
  <tr>
    <td>Thin Ring<br>(radius $R$)</td>
    <td>About center</td>
    <td>$MR^2$</td>
  </tr>
  <tr>
    <td>Ring of Ribbon<br>(radius $R$, width $w$)</td>
    <td>About central diameter</td>
    <td>$\frac{1}{2}MR^2 + \frac{1}{12}Mw^2$</td>
  </tr>
  <tr>
    <td>Solid cylinder<br>(radius $R$)</td>
    <td>About center</td>
    <td>$\frac{1}{2}MR^2$</td>
  </tr>
  <tr>
    <td>Hollow cylinder<br>(outer radius $R$, inner radius $r$)</td>
    <td>About center</td>
    <td>$\frac{1}{2}M(R^2 + r^2)$</td>
  </tr>
  <tr>
    <td>Solid ball<br>(radius $R$)</td>
    <td>About center</td>
    <td>$\frac{2}{5}MR^2$</td>
  </tr>
  <tr>
    <td>Solid rod<br>(length $\ell$)</td>
    <td>About center</td>
    <td>$\frac{1}{12}M\ell^2$</td>
  </tr>
  <tr>
    <td>Solid rod<br>(length $\ell$)</td>
    <td>About end</td>
    <td>$\frac{1}{3}M\ell^2$</td>
  </tr>
  <tr>
    <td>Thin rectangular plate<br>(length $\ell$, width $w$)</td>
    <td>About center</td>
    <td>$\frac{1}{12}M(\ell^2 + w^2)$</td>
  </tr>
</table>

### Rotation under torque: the massive top
This is fairly straightforward: construct the lagrangian in terms of three angles: a rotation of the top itself, the precession of the top around in a circle, and a nutation angle that allows the top to bob up and down under the influence of gravity. Introduce the conserved quantities (energy and two conjugate momenta to the rotation and precession angles) and make the substitution $u = -\sin\theta$ for $\theta$ the nutation angle, with $\theta=0$ taken to be horizontal. Then $u=1$ means the top is upright, $u=0$ means it's horizontal, and $u=-1$ means it's upside down. We get an equation that looks like $\dot{u} = $ a cubic polynomial, so we have 3 cases for where the roots lie: 3 distinct real roots, a double root and a crossing point, or only one real root.  

### Rolling without slipping
The rolling without slipping constraint is that <em>the velocity of the point of contact has to be equal to the velocity of the surface</em>, where the contact point has motion due to the center of mass and its rotation about the CM, and the surface is usually (but not always!) stationary. 

Use Newton's 2nd and the torque equation $r\times F = N = \dv{L}{t}$. For the torque equation, we can choose torque wrt center of mass, the contact point, or about some arbitrary point (the most useful is usually CM though). You can also solve this with Lagrangians, so long as you can integrate the semiholonomic constraint into one that doesnt depend on the velocities or include it with lagrange multipliers.

Note that the angular momentum can often be weird! For the right hand side, you don't necessarily want to rely on the parallel axis theorem to get $I$ so that you can just use $I\omega$; you should directly find $$\vb{L} = \vb{L}_\text{CM} + \vb{L}_\text{rot}$$ and take its derivative. (In particular $$\vb{L}_\text{CM}$$ is the weird one; the momentum about the CM is typically fine to think of as $I\omega$)


[Return to Table of Contents](#toc)
## Continuous Media <a name="chapter7"></a>
### Strings and surfaces
Can solve these using forces: consider a $\dd{\ell}$ or $\dd{A}$ and look at the forces, including tension

Or can solve them variationally, by minimizing the potential energy with a fixed boundary and length and stuff. To include the length constraint, do it with a multiplier. You can often find ``energy'' conserved by legendre transforming. 

It's good to know that waves on strings follow the wave equation with a velocity
<div>\begin{equation}
	v = \sqrt{\frac{T\ell}{m}}
\end{equation}</div>

### Fluids
Generally done by looking at forces and energy in a small part of the fluid. 

Pressure $p$ is such that $-\nabla p$ acts as a force per unit volume: it's the force on a $\dd{V}$ due to the rest of the fluid. Thus there is a potential energy associated to being surrounded by fluid. 

In static fluids, the potential energy is constant, since there is no energy cost to slow mixing. Typically see things like
<div>\begin{equation}
	U = p + \psi = \text{const}
\end{equation}</div>
with $\psi$ the potential energy per unit volume due to external forces (e.g. $\psi = \rho g h$ for gravity, but we can also have centrifugal energy $-\frac{1}{2}\rho\Omega^2r^2$ or something)

In a flowing fluid with no viscosity, we have a similar energy conservation:
<div>\begin{equation}
	p + \psi + \frac{1}{2}\rho u^2 = \text{const} \qq{and}\nabla\cdot(\rho \vb{u}) = -\pdv{\rho}{t}
\end{equation}</div>
for an incompressible fluid, the density never changes, so we have that the divergence of the velocity field is zero. 

If the velocity field is rotationless, we can write it as the gradient of some potential $\vb{u} = \nabla\phi$, and incompressibility makes that potential satisfy laplace's equation $\nabla^2\phi=0$

Viscosity makes it so that layers of fluid will try to pull on the surrounding layers; say we look at $u_x(z)$ for some fluid flowing in the $x$ direction where lower layers move slower than higher layers. We have
<div>\begin{equation}
	F_x/A = \eta\dv{u_x}{z}\qq{for some constant $\eta$}
\end{equation}</div>

[Return to Table of Contents](#toc)
