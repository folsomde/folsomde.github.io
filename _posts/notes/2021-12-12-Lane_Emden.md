---
title: "The Lane&ndash;Emden Equation"
layout: post
categories:
  - Notes
tags:
  - Galactic Dynamics
  - Research
  - Notes
permalink: /:categories/lane_emden
excerpt: "Very very very under construction"
comments: false
published: false
---

isothermal hydrostatic equilibrium is
$$\frac{\sigma^2}{\rho}\frac{\partial\rho}{\partial r} = -\frac{\partial\Phi}{\partial r} = - \frac{GM_r}{r^2}$$
which can be massaged to
$$\frac{1}{r^2}\frac{d}{dr}(\frac{r^2}{\rho}\frac{d\rho}{dr}) = - \frac{4\pi G\rho}{\sigma^2}$$

if we assume $\rho = \rho_0 e^{-\theta}$ then
$$ \frac{\sigma^2}{4\pi G \rho_0} \frac{1}{r^2}\frac{d}{dr}(r^2\frac{d\theta}{dr}) = e^{-\theta}.$$ 


Now $\xi = \frac{r}{r_0}$ with $r_0 = \sqrt{\frac{\sigma^2}{4\pi G \rho_0}}$ and
$$ \frac{1}{\xi^2} \frac{d}{d\xi}(\xi^2 \frac{d\theta}{d\xi}) = \theta''(\xi) + \frac{2}{\xi}\theta'(\xi)= e^{-\theta} = f(\xi) = \sum \frac{A_i}{a_i + \xi^2}$$
with

| i | $A_i$ | $a_i$ |
|--|----------|-------|
|1 |24.941621 |9.229485  |
|2 |-22.890004|13.490639  |
|3 |-0.602714 |106.575159  |
|4 |0.551098  |5172.242487|


further manipulation: recognize the $4\pi r^2 \rho$ in the isothermal equation to write
$$\frac{d}{dr}(\frac{r^2}{\rho}\frac{d\rho}{dr}) = - \frac{G}{\sigma^2}4\pi r^2\rho \implies \frac{r\sigma^2}{\rho }\frac{d\rho}{dr} = -\frac{GM}{r} \implies \frac{d\rho}{dr} = -\frac{GM\rho}{r^2\sigma^2}$$
we can plug in $f(r) = \rho(r)/\rho_0$ and $\xi = r/r_0$ to say
$$\frac{df}{d\xi} = \frac{r_0}{\rho_0}\frac{d\rho}{dr} = -\frac{GM\rho r_0}{\rho_0 r^2\sigma^2} = -\frac{Gg(\xi)f(\xi) r_0^4\rho_0}{r^2\sigma^2} = -\frac{Gg(\xi)f(\xi)\rho_0}{\xi^2\sigma^2}\frac{\sigma^2}{4\pi G \rho_0} =-\frac{g(\xi)f(\xi)}{4\pi \xi^2}$$

---

by definition,
$$\frac{dM}{dr} = 4\pi r^2 \rho(r)$$
thus with the isothermal profile, we have
$$M_\text{iso} = 4\pi \int_0^r \mathrm{d}R\, R^2 \rho(R) =4\pi \rho_0 \int_0^r \mathrm{d}R\, R^2 f(R)$$

$$M_\text{iso} = \frac{\sigma^2 r_0}{G} \Bigg(\frac{r}{r_0}\underbrace{\sum A_i}_2 - \sum \sqrt{a_i} A_i \tan^{-1}\Big(\frac{r}{\sqrt{a_i} r_0}\Big)\Bigg)  =\rho_0 r_0^3 g(r)$$
for

$$g(\xi) = \frac{\sigma^2}{G r_0^3\rho_0} \Bigg(2\xi - \sum \sqrt{a_i} A_i \tan^{-1}\Big(\frac{\xi}{\sqrt{a_i}}\Big)\Bigg)$$

the differential equation for mass conservation adimensionalizes to 

$$\frac{dg}{d\xi} = 4\pi \xi^2 f(\xi) $$

and from above we have the isothermal conditoin
$$\frac{df}{d\xi} =-\frac{g(\xi)f(\xi)}{4\pi \xi^2}$$
where the scales don't enter into the problem whatsoever: we have $f(0) = 1$. 

---
define $$\gamma = \frac{M}{4\pi \rho r^3}$$ for an isothermal, 
$$\gamma = \frac{\rho_0 r_0^3 g}{4\pi \rho_0 f(r) r^3} = \frac{g(r)}{f(r)4\pi\xi^3}$$


and in NFW, we have 
$$\rho_\text{NFW} = \frac{\rho_s}{\frac{r}{r_s}(1 + \frac{r}{r_s})^2} = \frac{\rho_s}{x(1 + x)^2}$$
and
$$M_\text{NFW} = 4\pi \rho_s r_s^3 \left[\ln(1 + \frac{r}{r_s}) - \frac{\frac{r}{r_s}}{1 +\frac{r}{r_s}}\right] =  4\pi \rho_s r_s^3 \left[\ln(1 + x) - \frac{x}{1 +x}\right]$$
thus, we have
$$\gamma_\text{NFW} = \frac{M}{4\pi \rho r^3} = \frac{\rho_s}{\rho x^3}\left[\ln(1 + x) - \frac{x}{1 +x}\right] =\frac{(1+x)^2}{x^2} \left[\ln(1 + x) - \frac{x}{1 +x}\right] $$
and we want to set it equal to $\gamma_\text{iso}$:

$$(1+1/x)^2 \left[\ln(1 + x) - \frac{x}{1 +x}\right]= \frac{g(r)}{f(r)4\pi\xi^3}$$

we also have the density condition on its own,
$$\frac{\rho_s}{x(1 + x)^2} = \rho_0 f(\xi) \implies \frac{\rho_0}{\rho_s} = [f(\xi)x(1+x)^2]^{-1}$$

---
we make the ansatz
$$ \frac{\xi}{\sqrt{\pi}}\rho(r_1)\sigma \sigma_m t = \frac{\xi}{\sqrt{\pi}}\rho_0f(\xi_1)\sigma \sigma_m t=  1$$ 

defining
$$v_s = \sqrt{4\pi G \rho_s r_s^2} \text{ and }t_0^{-1} = \frac{\xi}{\sqrt{\pi}}\rho_s v_s\sigma_m$$
we have ==(verify)==
$$\frac{\rho_0}{\rho_s}\frac{\sigma}{v_s}f(\xi)\frac{t}{t_0} = 1$$

we can compute the velocity fraction to relate NFW and iso parameters
$$\frac{\sigma}{v_s} = \frac{\sqrt{4\pi G \rho_0 r_0^2}}{\sqrt{4 \pi G \rho_s r_s^2}} = \frac{r_0}{r_s}\sqrt{\frac{\rho_0}{\rho_s}} = \frac{x}{\xi}\sqrt{\frac{\rho_0}{\rho_s}}$$

so that
$$ f(\xi_1) \frac{t}{t_0}(\frac{\rho_0}{\rho_s})^{3/2}\frac{x_1}{\xi_1} = 1 = \frac{\rho_\text{iso}(r_1)}{\rho_\text{NFW}(r_1)}$$
and massage some more to get
$$ \frac{t}{t_0} = (1 + x_1)^3 \xi_1 \sqrt{f(\xi_1)x_1}$$

---
so the strategy is this:
1. get $\xi_1(x_1)$ from the gamma relation
2. solve $t/t_0$ for $x_1$ given a $t, \rho_s, r_s$ (the last two of which determine $t_0$)
3. $\xi_1$ gives us 

