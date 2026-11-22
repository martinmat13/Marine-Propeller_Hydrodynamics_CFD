# 12. Convergence, verification, and validation

## 12.1 Three different questions

**Convergence:** Has the iterative numerical solution reached a sufficiently
stable state for the chosen equations, mesh, and discretization?

**Verification:** Are the equations being solved correctly, and are numerical
errors controlled? Evidence includes code checks, mesh sensitivity, iterative
convergence, and conservation.

**Validation:** Does the model represent the physical experiment adequately
for the intended use? This requires comparison with independent, traceable
experimental data and its uncertainty.

These are related but not interchangeable. Residual reduction alone is not
validation; matching a curve by tuning without independent evidence is not
validation.

## 12.2 Residuals

The algebraic residual measures the imbalance left in a discretized equation
after a linear solve. OpenFOAM commonly reports initial and final residuals
within each iteration. A reduction in residual indicates the linear system was
solved more tightly; it does not directly show whether thrust or torque stopped
changing.

Track residuals for all transported variables ($U$, $p$, $k$, $\omega$) and
check continuity errors. A variable may have a small algebraic residual while
an integrated quantity is still drifting.

## 12.3 Force convergence

Plot signed axial force and signed shaft moment against steady solver
iteration. Define a late-iteration window and report its mean, standard
deviation, and drift. One useful normalized drift metric is

$$
\epsilon_T=
\frac{|\overline{T}_{\mathrm{last}}-
\overline{T}_{\mathrm{previous}}|}
{\max(|\overline{T}_{\mathrm{last}}|,T_{\mathrm{scale}})},
$$

with an analogous $\epsilon_Q$. State the window lengths and $T_{\mathrm{scale}}$;
do not choose an arbitrary threshold after seeing the result.

For transient sliding-mesh flow, average over complete rotor revolutions after
initial transients. Steady MRF iteration is not physical time and must not be
described as “averaged over the last seconds.”

## 12.4 Conservation checks

Check global mass imbalance using inlet and outlet fluxes:

$$
\epsilon_m=
\frac{|\dot m_{\mathrm{in}}+\dot m_{\mathrm{out}}|}
\max(|\dot m_{\mathrm{in}}|,|\dot m_{\mathrm{out}}|)}.
$$

Also inspect integrated force behavior, pressure references, and any unphysical
velocity or turbulence extrema.

## 12.5 Verification studies

At minimum:

1. **Input verification:** units, boundary conditions, geometry and zone
   definitions.
2. **Iterative convergence:** residual, continuity, force, and moment histories.
3. **Mesh sensitivity:** at least three consistent mesh levels.
4. **Domain sensitivity:** confirm far boundaries do not materially change
   coefficients.
5. **Numerical sensitivity:** test relevant scheme and turbulence-model
   choices if conclusions depend on them.
6. **Independent coefficient calculation:** hand-check a post-processing point.

The current test mesh fails one default quality check due to a highly skewed
face; the existing solver run stopped early. Neither a final mesh-independence
study nor verification is complete.

## 12.6 Validation comparison

For a common $J$ grid, report signed relative differences such as

$$
e_{K_T}=\frac{K_{T,\mathrm{CFD}}-K_{T,\mathrm{ref}}}
{K_{T,\mathrm{ref}}}\times100\%,
$$

and similarly for $K_Q$ and $\eta_0$. Include the geometry, Reynolds number,
water properties, test uncertainty, numerical uncertainty, and interpolation
method.

The repository's Wageningen polynomial curve is a regression of historical
model-test data, not raw measurements. It is not a suitable substitute for the
original measured test points when claiming strict validation.

## 12.7 Current claims

The truthful current statement is: the v2512 dictionaries initialized and the
solver advanced, but the mesh/geometry workflow remains a prototype and no
validated performance result has been produced. See
[`test_status.md`](../docs/test_status.md).

## References

See ITTC procedure and uncertainty references in
[references and further reading](15_references.md).
