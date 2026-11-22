# Local environment inspection

## Purpose

This record describes the software and hardware observed before project files
and meshes were created. It supports reproducibility but does not claim a
validated CFD result.

## Environment

| Item | Observation |
|---|---|
| OpenFOAM API | v2512 |
| Installation | `/usr/lib/openfoam/openfoam2512` |
| Core utilities | `blockMesh`, `snappyHexMesh`, `checkMesh`, `decomposePar`, `reconstructPar` |
| RANS baseline solver | `simpleFoam` |
| Geometry tool | Gmsh |
| Python | 3.12.3 |
| NumPy | 1.26.4 |
| Pandas | 2.1.4 |
| Matplotlib | 3.6.3 |
| SciPy | 1.11.4 |
| Logical CPU cores | 16 |
| System memory | 7.4 GiB |
| Available workspace disk | approximately 893 GiB |

The v2512 tutorial tree contains a propeller force function-object example and
an MRFProperties example. These examples are references for dictionary syntax,
not a complete marine propeller geometry or validation dataset.

## Resource approach

- Start the baseline mesh with serial execution.
- Use 16 cores only after a serial case succeeds and a suitable mesh is defined.
- Monitor RAM, disk consumption, residual behavior, and force convergence.
- Do not launch a large mesh or parameter sweep before patch names and force
  extraction are checked.

## Lessons

- OpenFOAM v2512 is installed and discoverable through the environment variables.
- Gmsh is available for meshing support.
- FreeCAD was not found in the current environment.
- Meshio was not found; it is not required for the initial case.
