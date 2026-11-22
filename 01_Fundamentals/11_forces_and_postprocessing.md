# 11. Surface forces, performance metrics, and post-processing

## 11.1 Surface traction

For a surface with outward normal $\mathbf{n}$, the fluid traction on the body
is obtained from pressure and viscous stress. With a Cauchy stress tensor
$\boldsymbol{\sigma}$, the force on a body surface can be written

$$
\mathbf{F}=\int_S \boldsymbol{\sigma}\cdot\mathbf{n}\,dS,
\qquad
\mathbf{M}_{O}=\int_S
(\mathbf{x}-\mathbf{x}_O)\times
(\boldsymbol{\sigma}\cdot\mathbf{n})\,dS.
$$

The numerical force object sums face contributions. Surface-normal convention
and whether force is fluid-on-body or body-on-fluid affect sign; verify both.

The OpenFOAM `forces` function object reports total, pressure, viscous, and
possibly porous components. For the incompressible case, its `rhoInf` setting is
needed to dimensionalize pressure forces. The object's center of rotation
(`CofR`) sets moment reference point.

## 11.2 Thrust and torque extraction

With shaft axis unit vector $\mathbf{e}_s$, project the integrated force and
moment:

$$
T_{\mathrm{signed}}=\mathbf{F}\cdot\mathbf{e}_s,
\qquad
Q_{\mathrm{signed}}=\mathbf{M}_{O}\cdot\mathbf{e}_s.
$$

Then report sign convention and positive magnitudes only when physically
justified. If the origin is on the shaft centerline and the axis is correct,
shaft torque is the moment component along that axis. Pressure and viscous
contributions should both be retained for auditability.

## 11.3 Derived metrics

For each converged operating point:

$$
n=\frac{\mathrm{rpm}}{60},\qquad
J=\frac{V_A}{nD},
$$

$$
K_T=\frac{T}{\rho n^2D^4},\qquad
K_Q=\frac{Q}{\rho n^2D^5},
$$

$$
P_D=2\pi nQ,\qquad
P_T=TV_A,\qquad
\eta_0=\frac{P_T}{P_D}
=\frac{J}{2\pi}\frac{K_T}{K_Q}.
$$

Calculate efficiency only when force and torque signs are consistent with
positive propulsive power. A NaN, negative value, or value above one should
trigger investigation rather than clipping.

## 11.4 Time/iteration averaging

For an unsteady physical simulation, average over a stated number of complete
blade revolutions after transients decay. For steady MRF, solver iteration is
not physical time; evaluate convergence using iteration histories and a
late-iteration window. State the averaging interval and statistic (mean,
standard deviation, range).

## 11.5 Current post-processing tools

- [`performance.py`](../05_Performance_Analysis/scripts/performance.py)
  calculates coefficients from a force data file.
- [`reference_comparison.py`](../05_Performance_Analysis/scripts/reference_comparison.py)
  compares a CFD row with the nearest polynomial-reference $J$ point.
- [`plotting.py`](../05_Performance_Analysis/scripts/plotting.py) plots CFD
  and reference data.
- The reference CSV stores `10KQ`, not `KQ`.

These scripts are early project utilities. Before using a result, verify that
the parser columns match the installed v2512 `forces` output, independently
check the force and moment components, and confirm the nearest-$J$ comparison
is suitable. Interpolate the reference curve only with a documented method.

Example:

```bash
python3 05_Performance_Analysis/scripts/performance.py \
  04_MRF_Steady/baseline/postProcessing/forces/0/force.dat \
  --diameter 0.24 \
  --rpm 600 \
  --advance-speed 1.92 \
  --rho 1000 \
  --output results/baseline.csv
```

Check the `force.dat` format before running: the parser must map its thrust and
torque source components correctly for the version's output.

## 11.6 Reproducible output table

Keep raw loads and metadata alongside derived coefficients:

| Required field | Example unit |
|---|---|
| geometry identifier and revision | text |
| mesh cell count and mesh level | cells |
| $D$, $Z$, $P/D$, $A_E/A_0$ | m, -, -, - |
| $\rho$, $\nu$, temperature | kg/m$^3$, m$^2$/s, deg C |
| $V_A$, rpm, $J$ | m/s, rev/min, - |
| signed force and moment vectors | N, N m |
| $T$, $Q$, $K_T$, $K_Q$, $10K_Q$ | SI and dimensionless |
| residual/force convergence status | evidence |
| source and reference-data version | citation |

## References

OpenFOAM's `forces` object documentation and a v2512 propeller tutorial are
listed in [references](15_references.md).
