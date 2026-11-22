# Initial project specification

## Core objective

Create a transparent, reproducible OpenFOAM v2512 open-water propeller project
using a documented five-bladed Wageningen B-series configuration.

## Mandatory core stages

1. Identify and document a specific propeller geometry.
2. Obtain an approved open-water reference dataset.
3. Build and inspect the computational mesh.
4. Run a steady MRF baseline with `simpleFoam`.
5. Extract thrust and torque from blade and hub surfaces.
6. Calculate `J`, `K_T`, `K_Q`, and `eta_0`.
7. Verify residual and force convergence.
8. Perform mesh sensitivity and parameter studies.
9. Compare CFD with published reference data.
10. Document differences and limitations.

## Initial engineering assumptions

The final baseline assumptions must be selected after geometry and test data are
available. Initially, the following categories remain open decisions:

- incompressible or variable-density flow
- turbulence model
- propeller diameter and rotational speed
- advance velocity
- outer-domain dimensions
- boundary conditions
- mesh density
- hub and shaft modelling
- blade surface patch naming
- convergence criteria

No numerical value will be invented as a placeholder for these decisions.

## Numerical reference

The first solver is expected to be `simpleFoam` with MRF source terms in a
propeller-relative cell zone. The stationary outer domain should use the
uniform inflow boundary conditions selected for the reference open-water case.

## Repository and publication rules

- Keep results out of source control until they are documented and reproducible.
- Store selected figures only after actual CFD or licensed reference data exist.
- Mark advanced modules as planned until implemented.
- State every geometry and reference-data limitation.
