---
title: "Goldstein Notes"
layout: post
categories:
  - Notes
tags:
  - Classical Mechanics
  - Graduate Physics
comments: false
---
(under construction)
<a name="toc"></a>

## Table of Contents 
1. [Survey of the Elementary Principles](#chapter1)
2. [Variational Principles and Lagrange's Equations](#chapter2)
3. [The Central Force Problem](#chapter3)
4. [The Kinematics of Rigid Body Motion](#chapter4)
5. [The Rigid Body Equations of Motion](#chapter5)
6. [Oscillations](#chapter6)
7. [The Classical Mechanics of the Special Theory of Relativity](#chapter7)
8. [The Hamilton Equations of Motion](#chapter8)
9. [Canonical Transformations](#chapter9)
10. [Hamilton-Jacobi Theory and Action-Angle Variables](#chapter10)
11. [Classical Chaos](#chapter11)
12. [Canonical Perturbation Theory](#chapter12)
13. [Introduction to the Lagrangian and Hamiltonian Formulations for Continuous Systems and Fields](#chapter13)

---

## 1. Survey of the Elementary Principles <a name="chapter1"></a>

### Constraints
<div class = "message"><strong>Def.&ensp;</strong> A <em>holonomic constraint</em> is one that can be written $$f(\vb{r}_1,\, \vb{r}_2,\,\dots;\;t) = 0$$</div>
* e.g. rigid body motion, $$ (\vb{r}_i - \vb{r}_j)^2 - c_{ij}^2 = 0$$
* inequalities, differentials, derivatives are nonholonomic

<div class = "message"><strong>Def.&ensp;</strong> A <em>rheonomous constraint</em> is one that contains a dependence on time. Otherwise, the constraint is called <em>scleronomous</em>.</div>

### Lagrange's equation
<em>N.B.: There's a really nice derivation of the Euler-Lagrange equations in this section.</em>


As a condition for equilibrium, we have the principle of virtual work:
\begin{equation}
	\sum \vb{F}_ i^{(a)} \cdot \delta \vb{r}_ i = 0
\end{equation}
This condition is sufficient whenever the virtual work of the constraint forces vanishes; however, the $\delta \vb{r}_ i$ are still related by the constraints, and it deals only with statics. To include dynamics, we use D'Alembert's condition, 
\begin{equation}
	\sum (\vb{F}_ i^{(a)} - \vb{p}_ i)\cdot \delta \vb{r}_ i = 0
\end{equation}
In generalizing D'Alembert's condition to unconstrained degrees of freedom, we arrive at
\begin{equation}
	\dv{t}\pdv{T}{\dot{q}_ j} - \pdv{T}{q_ j} = Q_j = \vb{F}_ i\cdot \pdv{\vb{r}_ i}{q_j}
\end{equation}
Assuming that the forces $\vb{F}_ i$ are derivable from a velocity-independent scalar potential, we arrive at the usual expression of the Euler-Lagrange equations:
\begin{equation}
\dv{t}\pdv{L}{\dot{q}_ j} - \pdv{L}{q_ j} = 0
\end{equation}

### Velocity-dependent potentials
Instead of taking $Q_i = -\pdv{V}{q_i}$, we can also say 
\begin{equation}
Q_i = -\pdv{U}{q_i} + \dv{t}\qty(\pdv{U}{\dot{q}_ i})
\end{equation}
and the Euler-Lagrange equations retain the same form.

If there are forces $Q_i$ which are _not_ derivable from potentials, we can still solve the Euler-Lagrange equations, though now in a nonhomogeneous form; we set the left-hand-side equal to the $Q_i$. An example is the Rayleigh dissipation function 
\begin{equation}
\mathcal{F} = \frac{1}{2}\sum(k_x v_{ix}^2 + k_y v_{iy}^2 + k_z v_{iz}^2)
\end{equation}
for which the force is given by 
\begin{equation}
Q_j = -\pdv{\mathcal{F}}{\dot{q}_ j}
\end{equation}

[Return to Table of Contents](#toc)
## 2. Variational Principles and Lagrange's Equations <a name="chapter2"></a> 
This section has the standard variational derivation of the Euler-Lagrange equations.

### Hamilton's principle for nonholononmic systems
<div class = "message"><strong>Def.&ensp;</strong> A <em>semiholonomic constraint</em> is one that can be written in the form
\begin{equation}
	f(q,\, \dot{q}) = 0.
\end{equation}
Such constraints are often restricted to the form 
\begin{equation}
a_{i} \dd{q_i} + a_{t} \dd{t} = 0
\end{equation}
</div> 
We include these constraints using Lagrange multipliers. The sketch is as follows:
1. Since the constraint equations $f_\alpha$ are identically zero, we can say
\begin{equation}
\delta\int(L-\lambda^\alpha f_\alpha) \dd{t} = 0
\end{equation}
2. Solving the variation gives the nonhomogeneous Euler-Lagrange equations for forces of constraint
\begin{equation}
Q_j = \sum \lambda^\alpha \qty[\pdv{f_\alpha}{q_j} - \dv{t}\pdv{f_\alpha}{\dot{q}_j}] - \dv{\lambda^\alpha}{t} \pdv{f\scriptsize\alpha}{\dot{q}_j}
\end{equation}

Note that this method requires that the constraint forces do no work in virtual displacements.

### Jacobi's integral and dissipation
This chapter also defines Jacobi's integral $h$ as numerically equivalent to the Hamiltonian (though still written in terms of $\dot{q}$). The standard "time-dependent Lagrangian leads to time-dependent $h$" argument is carried out, and it is also noted that if there is a dissipation function $\mathcal{F}$, we have
\begin{equation}
	\dv{h}{t} = - 2\mathcal{F} - \pdv{L}{t}
\end{equation} 
giving the rate of energy loss.

[Return to Table of Contents](#toc)
## 3. The Central Force Problem <a name="chapter3"></a>
### Effective potential
Written in terms of plane-polar coordinates and the conserved angular momentum $\ell = mr^2\dot{\theta}$, we have
\begin{equation}
\frac{1}{2}m\dot{r}^2 + \frac{1}{2}\frac{\ell}{mr^2} + V = E
\end{equation}
from which we can define the effective potential including the angular momentum term. The force due to the effective potential includes an additional centrifugal force $\frac{\ell^2}{mr^3}$.

### The Laplace-Runge-Lenz vector
For a general central force, where $\dot{\vb{p}} = f(r)\frac{\vb{r}}{r}$, we can show
\begin{equation}
\dv{t}\qty(\vb{p}\times\vb{L}) = -mr^2\,f(r) \dv{t}(\frac{\vb{r}}{r})
\end{equation}
in the Kepler problem, where $f(r) = -\frac{k}{r^2}$, this ensures the conservation of the vector
\begin{equation}
\vb{A} = \vb{p}\times\vb{L} -mk\frac{\vb{r}}{r}
\end{equation}
This vector lies in the plane of orbit, and $A^2 = m^2k^2 + 2mE\ell^2$.

[Return to Table of Contents](#toc)
## 4. The Kinematics of Rigid Body Motion <a name="chapter4"></a>
### Euler angles
We can parameterize $SO(3)$ by the Euler angles $\theta$, $\phi$, and $\psi$, though Euler's theorem ensures we can fix the axis of rotation $\vu{n}$ and rotate by an angle $\Phi$ around this axis. The rotated vector is given by
\begin{equation}
\vb{r}' = \vb{r}\cos\Phi + \vu{n}(\vu{n}\cdot\vb{r})(1-\cos\Phi) + (\vb{r}\times\vu{n})\sin\Phi
\end{equation}
with $\Phi$ determined by
\begin{equation}
\cos\frac{\Phi}{2} = \cos(\frac{\phi+\psi}{2})\cos\frac{\theta}{2}
\end{equation}

### Infinitesimal rotations
Writing an infinitesimal rotation by Euler angles gives the antisymmetric matrix
\begin{equation}
A = \mqty(1 & \dd{\phi} + \dd{\psi} & 0\newline
	-\dd{\phi} -\dd{\psi} & 1 & \dd{\theta}\newline
	0 & -\dd{\theta} & 1) \qquad \dd{\vb{r}} = (A - 1)\vb{r}
\end{equation}
which we can also represent as a vector: 
\begin{equation}
\dd{\Omega} = \dd{\theta}\vu{i} + (\dd{\phi} + \dd{\psi})\vu{k}\qquad \dd{\vb{r}} = \vb{r}\times\dd{\Omega}
\end{equation}
These two formulations are related by noting $A = 1 + \delta$, where $\delta = \epsilon_{ijk}\dd{\Omega}^k$

We can decompose an infinitesimal transformation $\dd{\vb{r}}$ into a translational and rotational component, the latter of which is given above. Dividing by $\dd{t}$, we can decompose
\begin{equation}
\qty(\dv{\bullet}{t})_ {\text{external frame}} = \qty(\dv{\bullet}{t})_ \text{rotating frame} + \dv{\Omega}{t}\times\bullet
\end{equation}
where the first term encapsulates the translational change and the second the rotational. We often denote $\dot{\Omega}$ by $\omega$. Taking the second derivative of position, we find
\begin{equation}
\vb{a}_ {\text{ext}} = \vb{a}_ \text{rot} + 2(\omega\times \vb{v}_ \text{rot}) + \omega\times(\omega\times \vb{r})
\end{equation}
with the acceleration relative to the rotating coordinates, a Coriolis term, and a centrifugal term.


[Return to Table of Contents](#toc)
## 5. The Rigid Body Equations of Motion <a name="chapter5"></a>
### Inertia tensor
We define the inertia tensor by
\begin{equation}
	I_{jk} = \int \rho(\vb{r})\,(r^2\delta_{ij} - x_ix_j)\dd{V}
\end{equation}
with rotating principle axes, the typical $N = I\dot{\omega}$ equation becomes, relative to the body axes,
\begin{equation}
N_ i = I_ i \dot{\omega}_ i + \epsilon_{ijk} \omega_ j \omega_ k I_ k
\end{equation}
where the last term will contribute two nonzero summands.

An interesting discussion on Pointsot's construction follows in the text.

[Return to Table of Contents](#toc)
## 6. Oscillations <a name="chapter6"></a>
Standard treatment of oscillations: diagonalize the matrix representing the ODE to find normal modes.


[Return to Table of Contents](#toc)
## 7. The Classical Mechanics of the Special Theory of Relativity <a name="chapter7"></a>
### Velocity addition
\begin{equation}
	v_{31} = \frac{v_{32} + v_{21}}{1 + v_{32}v_{21}}
\end{equation}
where $v_{ij}$ is the velocity of $i$ as observed by $j$.
### Thomas precession and rotational motion
Two noncoaxial boosts are equivalent to a rotation and a boost, a phenomenon called Thomas precession. For a particle with nonconstant velocity, we consider a series of instantaneous rest frames along the curve of motion. The precession of the particle's frame can be given by
\begin{equation}
\omega = -(\gamma-1)\frac{\vb{v}\times\vb{a}}{v^2} \stackrel{v\ll c}{\approx}\frac{1}{2c^2}\vb{a}\times\vb{v}
\end{equation}

We define angular momentum as a two-tensor $m = x\wedge p$. If the force is $K^\mu = \dv{p^\mu}{\tau}$, the torque $N = x\wedge K = \dv{m}{\tau}$.

### Relativistic Lagrangians
In this setting, we define the Lagrangian by
\begin{equation}
L = -mc^2\sqrt{1-\beta^2} - V
\end{equation}
with conjugate momenta
\begin{equation}
\mathcal{P} = \pdv{L}{v} = \frac{mv}{\sqrt{1-\beta^2}}
\end{equation}
and equations of motion
\begin{equation}
\dv{t}\frac{mv}{\sqrt{1-\beta^2}} = -\pdv{V}{x} = F
\end{equation}
This works, but it isn't covariant. The action $\int \dd{s}$ is generally nicer.

[Return to Table of Contents](#toc)
## 8. The Hamilton Equations of Motion <a name="chapter8"></a>
### Legendre transformations and Hamilton's equations
For a function $f(x, y)$, we have 
\begin{equation}
\dd{f} = \pdv{f}{x}\dd{x} + \pdv{f}{y}\dd{y} = u\dd{x} + v\dd{y} 
\end{equation}
with $u$ and $v$ functions of $x$ and $y$. Defining $g = f - ux$, we can compute
\begin{equation}
\dd{g} = \dd{f} - u\dd{x} - x\dd{u} = v\dd{y} - x\dd{u} 
\end{equation}
and we have effectively swapped $x$ and $u$. Using $g$, we find
\begin{equation}
x = -\pdv{g}{u}\qq{and} v = \pdv{g}{y}
\end{equation}
i.e., $x$ and $v$ are now given as functions of $u$ and $y$.

As an example, we consider an application to thermodynamics: we have the energy $U(S,\, V)$ as 
\begin{equation}
\dd{U} = \dd{Q} - \dd{W} = T\dd{S} - P\dd{V}
\end{equation}
where the entropy and pressure are the partial derivatives of $U$. Given our variables, there are a number of Legendre transformations we can make:
  * Swapping $P$ and $V$ in the energy gives the enthalpy 
  \begin{equation}
  H = U + PV
\end{equation}

  * Swapping $T$ and $S$ in the energy gives the Helmholtz free energy 
  \begin{equation}
  F = U - TS
\end{equation}
  
  * Swapping both gives the Gibbs free energy 
  \begin{equation}
  G = H - TS
\end{equation}

### Symplectic formalism

### The Routhian

[Return to Table of Contents](#toc)
## 9. Canonical Transformations <a name="chapter9"></a>


[Return to Table of Contents](#toc)
## 10. Hamilton-Jacobi Theory and Action-Angle Variables <a name="chapter10"></a>

[Return to Table of Contents](#toc)
## 11. Classical Chaos <a name="chapter11"></a>


[Return to Table of Contents](#toc)
## 12. Canonical Perturbation Theory <a name="chapter12"></a>

[Return to Table of Contents](#toc)
## 13. Introduction to the Lagrangian and Hamiltonian Formulations for Continuous Systems and Fields <a name="chapter13"></a>

[Return to Table of Contents](#toc)