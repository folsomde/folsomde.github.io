---
title: "Compact Extra Dimensions"
layout: post
categories:
  - Expository
tags:
  - Quantum Mechancis
  - Undergraduate Physics
comments: false
---

Most theories predict new fundamental particles as part of their phenomenology, which is great; this means that the theories have testable predictions, so we can go out and look for these particles! The only problem is that we haven't yet seen any particles beyond those in the Standard Model. One possible explanation is that the particles are very heavy and as such are not discoverable with our current experiments. How might this happen theoretically? One way is with additional spatial dimensions, "curled up" into a small volume.

## What is a compact dimension?
Consider an infinite line, a 1D world. Let $x$ be the coordinate defining this line. Suppose you live in this 1D world, and as you walk along the line, you notice that the scenery repeats each time you move a distance $2\pi R$ for some $R$. If you walk by a tree, you see that there are identical copies of that tree at distances $2\pi R$, $4\pi R$, $6\pi R$, and so on. Mathematically, your world can be explained placing it on a circle; there aren't different copies of the tree, you're seeing the same tree again and again as you go around a circle. How can we express this mathematically?


We can think of the circle as a line that has the property where any function evaluated at point $x$ gives the same result as the same function at $x + 2\pi R\,n$, where $n$ is an integer.
\begin{equation}
f(x) = f(x + 2\pi R\,n)
\end{equation}
With this definition, the line becomes a circle; we are describing it in terms of a periodic boundary condition.

Notice that when $R\to \infty$, the circle approaches the usual non-compact 1D line. In other words, compact extra dimensions are only discernible at small $R$. This is analogous to treating a cylinder as a line when at large distances -- when the radius is small with respect to your distance from the cylinder, it "looks like" a line, and you can get an effective theory by treating it as one instead of a cylinder. A compact dimension is one similar to this periodic line, where it can be thought of as closing in on itself or having a bounded size rather than extending to infinity.

## How do wavefunctions behave under compact extra dimensions?
Now that we have a feel for what a compact dimension is, let's see how it affects things quantum mechanically by comparing an example system to a version of it with a compact extra dimension!

### The 1D infinite well
Consider a standard system in quantum mechanics, the 1D infinite well, with a potential
\begin{equation}
V(x) = \begin{cases}
0 & x \in (0, a)\newline \infty & x \notin (0, a)
\end{cases}
\end{equation}
What are our boundary conditions?
\begin{enumerate}
\item The probability density $\psi^\ast(x)\, \psi(x) = 0$ in the regions where $V = \infty$
\begin{itemize}
\item $\psi(x)$ must vanish there, so $\psi(0) = \psi(a) = 0$
\end{itemize}
\item $\psi(x)$ should be normalized (we should have a 100\% chance to find the particle somewhere in this potential well)
\end{enumerate}
Since the potential is time-independent, we can use the time-independent Schr&ouml;dinger equation to find the steady states. If you're unfamiliar with the derivation of the time-independent Schr&ouml;dinger equation (separation of variables from the time-<em>de</em>pendent Schr&ouml;dinger equation), it's worth looking at it, since it will be important later. Nevertheless,
\begin{gather*}
\hat{H}\psi = E\psi\\
-\frac{\hbar^2}{2m}\pdv[2]{\psi}{x} + V(x)\psi = E \psi
\end{gather*}
In the region $(0, a)$, $V(x) = 0$, so we simply have 
\begin{equation}
-\frac{\hbar^2}{2m}\pdv[2]{\psi}{x} = E \psi \implies \boxed{\pdv[2]{\psi}{x} = -\frac{2mE}{\hbar^2}\psi}
\end{equation}
To solve this differential equation, let's assume a solution 
\begin{equation}
\boxed{\psi(x) = A\sin(k x) + B \cos(k x)}
\end{equation}
 and solve for the constants. Starting on the left side of the Schr&ouml;dinger equation, we have:
 \begin{align*}
\pdv{x}\qty[A\sin(k x) + B \cos(k x)] &= Ak\cos(k x) - Bk \sin(k x)\\
\pdv[2]{x}\qty[A\sin(k x) + B \cos(k x)] &= -Ak^2\sin(k x) - Bk^2 \cos(k x)\\
&= - k^2\qty[A\sin(k x) + B\cos(k x)]
\end{align*}
which means, plugging back into the full equation,
\begin{equation}
- k^2\cancel{\qty[A\sin(k x) + B\cos(k x)]} =-\frac{2mE}{\hbar^2}\cancel{\qty[A\sin(k x) + B\cos(k x)]}
\end{equation}
and thus 
\begin{equation}
k = \sqrt{\frac{2mE}{\hbar^2}}
\end{equation}
Now we impose boundary condition 1, $\psi(0) = \psi(a) = 0$
\begin{gather*}
\psi(0) = A\sin(0) + B\cos(0) = B = 0\\
\psi(a) = A\sin(ka) = 0 \implies ka = \pi n
\end{gather*}
So now we have $\psi(x) = A\sin(\frac{\pi n}{a}x)$, and applying boundary condition 2 gives $A = \sqrt{\frac{2}{a}}$, proof of which is left as an exercise in integration for the reader :)
The important results to remember for comparison are the wavefunctions and their energy values:
<div class = "message">
\begin{equation}
\psi_n(x) = \sqrt{\frac{2}{a}}\sin(\frac{n\pi}{a}x)\qquad
E_n = \frac{\hbar^2}{2m}k^2 = \frac{\hbar^2}{2m}\qty(\frac{n\pi}{a})^2
\end{equation}
</div>