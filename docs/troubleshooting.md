# Troubleshooting

## `propeller.stl` is missing

Run `02_Geometry/generate_geometry.py`, then copy it into
`04_MRF_Steady/baseline/constant/triSurface/propeller.stl`.

## `checkMesh` fails

Do not run the solver. Inspect STL closure, surface intersections,
non-orthogonality, and the initial mesh quality.

## Forces are zero

Check that the `propeller` patch exists, that the force object is active in
`controlDict`, and that the STL patch is named correctly.

## MRF zone is empty

Run `topoSet` and inspect `topoSet.log`. Confirm that the block mesh contains
cells inside `(-0.15 -0.15 -0.15)` and `(0.15 0.15 0.15)`.

## Residuals converge but forces oscillate

Do not treat the result as converged. Check force averaging, mesh quality,
boundary conditions, and local flow separation.
