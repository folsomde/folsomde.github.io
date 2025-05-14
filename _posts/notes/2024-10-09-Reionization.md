---
title: "Thermal History of the Universe and the Threshold for Galaxy Formation"
layout: post
categories:
  - Notes
tags:
  - Cosmology
  - Research
  - Notes
permalink: /:categories/thermal_history
excerpt: "Very very very under construction"
comments: false
published: false
---


<a name="toc"></a>

## Table of Contents 
1. [Recombination](#1)
2. [Thermal Decoupling](#2)
3. [Reionization](#3)
4. [Further reading](#resources)

---

# Recombination <a name="1"></a>
Once the temperature of the universe drops below the binding energy of hydrogen, 13.6&nbsp;eV, the electrons and protons combine to form neutral hydrogen. Under assumptions of equilibrium, this process is described the Saha equation, and the time when the ionization fraction reaches 10% is at \\(z \sim 1300\\) or \\(T \sim 0.3\\) eV. This is much smaller than the binding energy, since there are still a enough high-energy photons to keep hydrogen ionized even when the peak of the thermal blackbody spectrum is shifted to low energies. 

Correcting for out-of-equilibrium effects (i.e., the rates of recombination and ionization becoming smaller than the expansion rate of the universe) gives the timing of recombination as closer to \\(z \sim 1100\\), \\(T \sim 2.6\\) eV. This also leads to a freeze-out effect, where it is not possible for all of the free electrons to recombine; the residual ionization fraction is \\(X_e\sim 2\times 10^{-4}\\). Without free electrons for Thomson (elastic, non-relativistic) scattering, the CMB is allowed to free-stream through the universe. 

[Return to Table of Contents](#toc)
# Thermal Decoupling <a name="2"></a>
After recombination, the simple expectation is for the temperature of matter to fall as[^Tm] \\(T_m\sim a^{-2}\\) and radiation to fall more slowly, as[^Tgamma] \\(T_\gamma \sim a^{-1}\\). However, there is still inelastic Compton scattering which efficiently transfers temperature from the photons to the matter. The rate of energy transfer from Compton scattering only becomes comparable to the expansion rate at \\(z \sim 150\\), and it's only at this time that the temperatures of matter and radiation truly decouple. Despite this continued scattering, most photons are unaffected and retain the thermal spectrum from the time of recombination; there are many many more photons than there are matter particles, so energy is injected into the matter with minimal effect on the radiation spectrum.

[^Tm]: For matter, \\(k_BT \sim m\langle v^2\rangle \sim (a^{-1})^2\\) due to the redshfiting of peculiar velocities
[^Tgamma]: Stefan-Boltzmann says \\(\rho_\gamma \sim T^4\\), and \\(\rho_\gamma = n_\gamma E_\gamma \sim a^{-3}\cdot a^{-1}\\)

## Capture by Halos and Star Formation
The virial temperature of dark matter halos is roughly[^Tvir]
<div>\begin{equation}
T_\mathrm{vir} \approx 230 \left(\frac{M}{10^4~\mathrm{M}_\odot}\right)^{2/3}\left(\frac{1+z}{100}\right)~\mathrm{K}
\end{equation} </div>
which, for halos of \\(M_\mathrm{vir} \sim 10^4~\mathrm{M}_\odot\\), is comparable to the gas temperature during this epoch
<div>\begin{equation}
T_\mathrm{gas} = T_\gamma \approx 273 \left(\frac{1+z}{100}\right)~\mathrm{K}.
\end{equation} </div>

Therefore, it is possible for dark matter halos at or above this mass floor to begin trapping baryons, and this is enhanced after decoupling when the temperature of the gas begins to fall faster than that of the photons. This trapped gas gets shock-heated up to \\(T_\mathrm{vir}\\) as it falls into the potential well, and this could be the end of the story -- the gas stays hot, trapped in the dark matter halo. However, gas can radiate that energy away and cool.

At high temperatures, \\(T > 10^6~\mathrm{K}\sim 80~\mathrm{eV}\\), gas is entirely ionized and the only way for energy to radiate away is through bremsstrahlung, free electrons scattering from free protons and radiating a photon.  At lower temperatures, other processes are important:
<ul>
  <li> Collisional ionization: a free electron completely ionizes an atom, removing energy from it in the process and freeing an additional electron </li>
  <li> Collisional excitation: a free electron excites an atom, causing it to emit radiation when it relaxes </li>
  <li> Recombination: free electrons and ionized nuclei recombine, releasing a photon </li>
</ul>
with collisional processes contributing most of the cooling at \\(T \lesssim 10^{5.5}~\mathrm{K}\\) (\\(27~\mathrm{eV}\\)). All cooling quickly shuts off at temperatures below \\(T \sim 10^4\mathrm{K}\\), as at this point there are no ionized electrons remaining to source the interactions. Below this threshold, molecules such as \\(H_2\\) are required, as they have other low-energy rotational/vibrational modes which may emit energy. Therefore, star formation (which requires very high density, very cold gas) hinges crucially on the formation of \\(H_2\\) to get temperatures low. (MVdBW 446)

[^Tvir]: The scaling comes from \\(T \sim V_\mathrm{vir}^2 \sim M_\mathrm{vir}/R_\mathrm{vir}\\), for \\(M_\mathrm{vir} \sim \rho_c R_\mathrm{vir}^3\\), and \\(\rho_c \sim (1 + z)^3\\) 

[Return to Table of Contents](#toc)
# Reionization  <a name="3"></a>
At this point, the universe is fairly simple: a highly uniform and isotropic distribution of mostly-hydrogen (plus free electrons and BBN-produced helium, with \\(n_\mathrm{He}/n_\mathrm{H} \sim 0.07\\) cooling with the infrared-hot CMB. The free electrons (MVdBW 690)

[Return to Table of Contents](#toc)
# Further reading <a name="resources"></a>
 - Mo, Van den Bosch, and White
---