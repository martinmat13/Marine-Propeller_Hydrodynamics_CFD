# Mesh strategy

The mesh stage begins only after a geometrically defined propeller exists.

## Baseline approach

1. Create a cylindrical rotating zone around the propeller.
2. Create a stationary outer domain sufficiently far from the propeller.
3. Use a refined surface mesh and boundary-layer cells on the blades and hub.
4. Resolve the near-tip gap and shaft interfaces consistently.
5. Use `blockMesh` or Gmsh for the background domain where appropriate.
6. Use `snappyHexMesh` for surface and boundary-layer refinement.
7. Verify closed, non-intersecting geometry and accepted mesh quality.

## Initial checks

- `checkMesh`
- minimum and maximum non-orthogonality
- maximum skewness
- free-surface or solid-region intersection
- wall-normal spacing
- MRF zone coverage
- boundary-patch naming

The first mesh will be intentionally coarse enough to test the workflow quickly.
A fine mesh is not automatically a converged mesh.
