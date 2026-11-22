# Mesh-independence plan

## Levels

Three meshes should be compared after the baseline workflow is functional:

1. coarse
2. medium
3. fine

Each level must preserve the same domain, MRF zone, boundary conditions,
operating point, and force-patch definition.

## Metrics

- thrust `T`
- torque `Q`
- `K_T`
- `10K_Q`
- `eta_0`
- maximum wall `y+` where appropriate
- residual convergence
- force-running averages

## Reporting rule

Report mesh-to-mesh differences and the change in key coefficients. Do not call
a result mesh-independent from visual comparison alone.
