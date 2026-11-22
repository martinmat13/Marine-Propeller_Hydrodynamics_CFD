# Propeller mesh strategy

## Domain

The baseline domain is 6 diameter lengths long and 6 diameter widths high.
The inlet is 6 diameters upstream and the outlet is 10 diameters downstream
for the selected 0.24 m diameter.

The initial block mesh is intentionally coarse. SnappyHexMesh adds two
refinement levels around the reconstructed propeller surface.

## Patches

- `inlet`: advance velocity boundary
- `outlet`: fixed pressure, pressure-inlet/outlet velocity
- `walls`: slip boundaries
- `propeller`: wall boundary from the STL

## Zone

The `rotor` cell zone is generated after meshing by `topoSet`. It defines a
box around the propeller for MRF source terms.

## Quality gates

Do not proceed to a parameter study unless:

- `checkMesh` reports no failed thresholds
- the STL imports with a recognized `propeller` patch
- the rotor cell zone is populated
- residual and force histories are stable
- the mesh has sensible boundary-layer resolution
