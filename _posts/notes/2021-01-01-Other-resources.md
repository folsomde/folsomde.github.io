---
title: "Other Resources"
layout: post
categories:
  - Notes
tags:
  - Prelim Notes
permalink: /:categories/other-resources:output_ext
excerpt: "Some mathematical facts that are good to know."
comments: false
---

## The Golden Rule
<div class='message'><b>if you dont know how to do an integral, 

adimensionalize it to pull out all the physics 

and just turn it into a number</b></div>
## Other math facts!
vector calc thing i always forget:
\begin{equation}
	\nabla\times(\nabla\times \vb{A}) = \nabla(\nabla\cdot\vb{A}) - \nabla^2\vb{A}
\end{equation}

a tricky taylor expansion:
\begin{equation}
	\frac{1}{|a-r|} = \frac{1}{\sqrt{a^2-2a\cdot r+r^2}} = \frac{1}{|a|}\frac{1}{\sqrt{12-2a\cdot r/a^2+r^2/a^2}} \approx \frac{1}{|a|}\qty(1+\frac{r\cdot a}{a^2})
\end{equation}

common integral:
\begin{equation}
	\int_0^{\infty}\dd{x}x^ne^{-x} = n!
\end{equation}

Stirling's approximation:
\begin{equation}
	\log N! \approx N\log N - N
\end{equation}

Laplace's method/ saddle point integration:
\begin{equation}
	\int h(x) e^{Mg(x)} \approx \sqrt{\frac{2\pi}{M|g''(x_0)|}}h(x_0)e^{Mg(x_0)}
\end{equation}
for $M$ large and $x_0$ the location of the maximum of $g$

Spherical coordinates
\begin{equation}
	\nabla^2 f = \frac{1}{r^2}\pdv{r}\qty(r^2\pdv{f}{r}) + \frac{1}{r^2\sin\theta}\pdv{\theta}\qty(\sin\theta\pdv{f}{\theta}) + \frac{1}{r^2\sin^2\theta}\pdv[2]{f}{\phi}
\end{equation}

&#127345;aussian
\begin{equation}
	\int\dd[n]{x} \exp\Big(- \frac{1}{2}\vb{x}\cdot\mathbb{A}\cdot\vb{x} + \vb{v}\cdot\vb{x}\Big) = \sqrt{\frac{(2\pi)^n}{\det\mathbb{A}}}\exp\Big(\frac{1}{2}\vb{v}\cdot\mathbb{A}^{-1}\cdot\vb{v}\Big)
\end{equation}
