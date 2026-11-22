# 7. Reynolds similarity and cavitation

## 7.1 Reynolds number

The Reynolds number compares inertial and viscous effects:

$$
Re=\frac{UL}{\nu}.
$$

For a propeller, the characteristic velocity and length must be stated. A
widely used section Reynolds number at radial station $r$ is

$$
Re_r=\frac{c(r)W(r)}{\nu},
\qquad
W(r)=\sqrt{V_x(r)^2+V_\theta(r)^2}.
$$

At $0.7R$, a first estimate that omits induced velocities is

$$
W_{0.7R}\approx
\sqrt{V_A^2+\left(2\pi n\,0.7R\right)^2}.
$$

The project case uses $D=0.24$ m, $n=10$ rev/s, $J=0.8$, and
$\nu=10^{-6}$ m$^2$/s. Hence $V_A=1.92$ m/s. With the approximate B-series
chord near $0.75R$, the section Reynolds number is about
$4.4\times10^5$ (order-of-magnitude estimate; induced flow and actual geometry
are omitted).

## 7.2 Similarity and scale effects

Matching $J$ alone is insufficient for complete model-to-full-scale
similarity. Reynolds number affects boundary layers, transition, friction
drag, and sometimes separation. Cavitation similarity requires matching an
appropriate cavitation number and water conditions. Geometry, roughness,
ventilation, and free-surface effects can also matter.

The B-series curve shipped with the project is generated from a regression
associated with an equivalent Reynolds number near $2\times10^6$. The
illustrative CFD condition above is much lower. It is not a like-for-like
validation condition. A proper comparison needs the reference's stated
Reynolds correction and model-test conditions.

## 7.3 Cavitation number

Cavitation occurs when local absolute pressure approaches vapor pressure
$p_v$. A common reference form is

$$
\sigma=\frac{p_{\mathrm{ref}}-p_v}
{\tfrac12\rho U_{\mathrm{ref}}^2}.
$$

The reference pressure and velocity must be defined. Propeller literature may
use a rotational-speed scale or a local section velocity; values from different
definitions must not be compared without conversion.

Temperature changes vapor pressure. Dissolved gas and nuclei affect inception.
Therefore “same $\sigma$” is not a complete guarantee of identical cavitation.

## 7.4 What the current case can and cannot say

The present case is single-phase, incompressible RANS. It can only provide a
single-phase pressure and velocity field on its specified approximate surface.
It cannot predict vapor volume fraction, cavity dynamics, erosion risk, or
cavitation inception.

A future cavitation study would need a validated blade, absolute pressure
reference, temperature-dependent vapor pressure, appropriate multiphase
cavitation model, suitable mesh/time step, and cavitation-tunnel or other
traceable comparison data.

## Physical interpretation

At fixed $n$ and geometry, increasing $V_A$ increases $J$ and changes section
angle of attack. At fixed $J$, increasing model size while preserving
geometric similarity can raise Reynolds number, changing viscous behavior even
when the nondimensional kinematics are similar.

## References

See [references and further reading](15_references.md) for ITTC scaling and
cavitation procedures and the B-series regression source.
