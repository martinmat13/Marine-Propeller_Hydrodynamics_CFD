# 5. Open-water performance coefficients

## Learning objectives

- Calculate $J$, $K_T$, $K_Q$, power, and open-water efficiency.
- Interpret performance curves and their assumptions.
- Distinguish a B-series regression from experimental measurements.

## 5.1 Open-water test condition

An open-water propeller test measures a propeller operating in a sufficiently
uniform inflow, away from a ship hull. It typically varies advance speed and
records thrust and torque at controlled rotational speed and water properties.
The procedure specifies model installation, instrumentation, corrections, and
reporting; follow a current ITTC procedure for formal experimental work.

Open water is useful because it isolates propeller characteristics. It does
not reproduce the nonuniform hull wake.

## 5.2 Dimensionless coefficients

Use $n$ in rev/s:

$$
J=\frac{V_A}{nD},
\qquad
K_T=\frac{T}{\rho n^2D^4},
\qquad
K_Q=\frac{Q}{\rho n^2D^5}.
$$

Definitions and dimensions:

| Symbol | Definition | Units before division |
|---|---|---|
| $J$ | $V_A/(nD)$ | $(\mathrm{m/s})/(\mathrm{s^{-1}m})=1$ |
| $K_T$ | $T/(\rho n^2D^4)$ | N / N = 1 |
| $K_Q$ | $Q/(\rho n^2D^5)$ | N m / (N m) = 1 |

The frequently plotted `10KQ` is ten times the torque coefficient. It is not
the coefficient itself.

## 5.3 Power and efficiency

Shaft power delivered to the propeller and useful thrust power are

$$
P_D=2\pi nQ,\qquad P_T=T V_A.
$$

Substituting the coefficient definitions:

$$
\eta_0=\frac{P_T}{P_D}
=\frac{T V_A}{2\pi nQ}
=\frac{J}{2\pi}\frac{K_T}{K_Q}.
$$

This identity is a powerful consistency check. It requires compatible
definitions of $T$, $Q$, $n$, $D$, and $\rho$.

## 5.4 Worked dimensional scaling

For the selected *reference configuration* at $J=0.8$, the generated
B-series regression file gives approximately $K_T=0.24654$,
$10K_Q=0.48567$, hence $K_Q=0.048567$. With the case's illustrative scale and
water properties ($D=0.24$ m, $n=10$ rev/s, $\rho=1000$ kg/m$^3$):

$$
V_A=JnD=1.92\ \mathrm{m/s},
$$

$$
T=K_T\rho n^2D^4\approx81.8\ \mathrm N,
\qquad
Q=K_Q\rho n^2D^5\approx3.87\ \mathrm{N\,m},
$$

$$
P_D=2\pi nQ\approx243\ \mathrm W,\qquad
P_T=TV_A\approx157\ \mathrm W,\qquad
\eta_0\approx0.646.
$$

These values are **calculated from the published polynomial correlation**, not
from CFD and not a new experiment. The correlation is associated with a
specified Reynolds-number treatment; see [Reynolds similarity](07_reynolds_similarity_cavitation.md).

## 5.5 Open-water versus ship propulsion efficiencies

Open-water efficiency $\eta_0$ describes propeller thrust power divided by
delivered shaft power in uniform inflow. In a ship wake, hull-propeller
interaction introduces additional efficiencies. A common decomposition is

$$
\eta_D=\eta_0\,\eta_H\,\eta_R\,\eta_S,
\qquad
\eta_H=\frac{1-t}{1-w},
$$

where $w$ is wake fraction, $t$ is thrust-deduction fraction, $\eta_R$ is
relative-rotative efficiency, and $\eta_S$ is shaft efficiency. Definitions
vary with convention; use the relevant test or design standard. None of these
hull interaction factors is determined by an isolated open-water MRF case.

## 5.6 Factors affecting coefficient curves

At fixed geometry, coefficient curves can vary with:

- Reynolds number and transition/roughness;
- cavitation number and water vapor pressure;
- blade surface condition and measurement corrections;
- geometry differences and manufacturing tolerances;
- inflow nonuniformity and blockage;
- numerical discretization, turbulence model, and boundary conditions.

Dimensionless coefficients improve similarity, but do not erase Reynolds or
cavitation effects.

## References

The included file is
[`wageningen_b5_75_pd120.csv`](../05_Performance_Analysis/reference_data/wageningen_b5_75_pd120.csv).
Its source and status are described in [references](15_references.md).
