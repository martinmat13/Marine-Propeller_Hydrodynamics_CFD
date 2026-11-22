# 14. Common failure modes and diagnostic reasoning

## Geometry and coordinates

**Symptom:** thrust or torque has the wrong sign.
**Check:** shaft axis, inflow direction, handedness, right-hand-rule rotation,
surface normals, and whether force is fluid-on-body or body-on-fluid.

**Symptom:** a plausible-looking STL but unexpected loads.
**Check:** actual closed surface, section thickness, chord, pitch distribution,
root/tip closure, and physical units. A finer mesh cannot repair wrong geometry.

**Symptom:** geometry is called B5-75 because it has five blades.
**Check:** B5-75 is not a full CAD definition. Document area ratio, pitch,
sections, hub, rake, skew, source, and reconstruction assumptions.

## Operating point and units

**Symptom:** coefficient is wrong by factors of 60 or $2\pi$.
**Check:** use $n=\mathrm{rpm}/60$ in $J$, $K_T$, and $K_Q$; use
$\Omega=2\pi n$ in shaft power.

**Symptom:** `10KQ` differs by ten.
**Check:** distinguish plotted $10K_Q$ from the coefficient $K_Q$.

**Symptom:** implausible power or efficiency.
**Check:** $P_D=2\pi nQ$, $P_T=TV_A$, pressure-unit conversion, density, axis
projection, signed loads, and geometry.

## OpenFOAM setup

**Symptom:** solver says no cell zone exists.
**Check:** `topoSetDict` ran and created the exact zone name in `MRFProperties`.

**Symptom:** turbulence wall function fails.
**Check:** wall-function field types are assigned only to boundary patches of
type `wall`.

**Symptom:** non-zero mass imbalance.
**Check:** inlet/outlet boundary conditions, pressure reference, mesh
connectivity, and convergence.

**Symptom:** residuals fall but integrated loads drift.
**Check:** force histories. Residual convergence is not force convergence.

## Mesh and model interpretation

**Symptom:** `checkMesh` reports poor skewness but solver runs.
**Check:** investigate the flagged cells and refine/remesh. Solver success is
not proof that mesh quality is adequate.

**Symptom:** MRF result is used to discuss blade-passage load cycles.
**Check:** steady MRF cannot resolve those cycles; use a transient moving-mesh
approach if they matter.

**Symptom:** cavitation is claimed from a single-phase pressure contour.
**Check:** vapor fraction, pressure reference, cavitation model, temperature,
and validated cavitation conditions are all missing.

## Project-specific caution

The present STL is a proxy; mesh check reports one highly skewed face; and the
initial solver run was stopped at iteration 692. The resulting loads are not
performance predictions. See [`test_status.md`](../docs/test_status.md).
