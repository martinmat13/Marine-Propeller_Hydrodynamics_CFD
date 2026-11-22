# Baseline test status

Date: 2026-11-22

## Geometry

- Generated B5-75 reconstruction STL successfully.
- Diameter: 0.240 m
- Five blades
- P/D: 1.20
- EAR: 0.75

## Mesh

- `blockMesh` completed.
- `snappyHexMesh` completed without meshing errors.
- `topoSet` created a 4756-cell `rotor` zone.
- `checkMesh` reported one skew face with maximum skewness 4.2322077.
- The mesh passed volume, pyramid, non-orthogonality, and connectivity checks.
- It is not yet accepted as a final baseline mesh.

## Solver

- `simpleFoam` initialized k-omega SST and MRF fields successfully after
  dictionary corrections.
- The run reached iteration 692 before manual stopping.
- Residual values were on the order of 1e-5 to 1e-7 for solved variables.
- The force output at the last inspected state was approximately 213.7 N thrust
  and -5.05 N m moment about the shaft axis.
- This is a work-in-progress test result, not a converged operating-point result.

## Outstanding issues

- Remove or improve the skew face.
- Establish SIMPLE convergence criteria.
- Complete the full run and force averaging.
- Verify torque moment sign and axis.
- Perform mesh sensitivity.
- Acquire exact blade coordinates and raw model-test data.
