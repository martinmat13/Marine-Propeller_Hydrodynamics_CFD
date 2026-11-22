# CFD-Based Hydrodynamic Performance Analysis of a Marine Propeller

An OpenFOAM investigation of open-water propulsion, rotating flow,
hydrodynamic loading, and cavitation.

## Project status

This repository is under active development. The current milestone establishes
the project structure, local environment record, and marine propeller
fundamentals. It does **not** yet contain a simulation, CFD result,
experimental comparison, or authentic Wageningen propeller geometry.

## Project objective

Develop and document a reproducible OpenFOAM v2512 study of a five-bladed
Wageningen B-series propeller in open-water conditions. The intended core
deliverable is a steady Multiple Reference Frame (MRF) simulation that predicts
thrust, torque, and open-water efficiency for published operating conditions.

No result should be interpreted as validated until CFD data are compared with
traceable experimental or reference data.

## Scope

- Marine propeller thrust and torque fundamentals
- Wageningen B-series geometry specification
- Experimental open-water reference data
- Steady MRF simulation with `simpleFoam`
- Thrust and torque post-processing
- Advance and force coefficient calculations
- Mesh and operating-condition studies
- CFD verification and experimental validation
- Planned transient sliding-mesh, cavitation, and hull-interaction studies

## Repository

```text
01_Fundamentals/       Propeller theory and learning material
02_Geometry/           Geometry sources and preparation instructions
03_Mesh/               Mesh strategy and mesh case support
04_MRF_Steady/         Steady open-water MRF cases
05_Performance_Analysis/
                       Python calculations and result summaries
06_Verification_Validation/
                       Mesh, convergence, and validation methodology
07_Post_Processing/     Plotting and ParaView workflow
08_Sliding_Mesh_Advanced/
09_Cavitation_Advanced/
10_Hull_Interaction_Advanced/
docs/                  Project and engineering documentation
scripts/               Environment and workflow automation
images/                Selected reproducible publication figures
```

## Development workflow

1. Verify the local environment.
2. Select and document a traceable propeller configuration.
3. Obtain or prepare legally redistributable geometry.
4. Create and inspect the computational mesh.
5. Run a small steady MRF baseline.
6. Verify force extraction and convergence.
7. Automate performance calculations.
8. Compare results with published reference data.
9. Perform mesh and operating-condition studies.
10. Only then begin advanced transient or cavitation work.

Detailed instructions are in [the project roadmap](docs/project_roadmap.md).

## Software baseline

- OpenFOAM v2512 installed in `/usr/lib/openfoam/openfoam2512`
- Python 3.12
- Gmsh
- NumPy, Pandas, Matplotlib, and SciPy

Run `scripts/check_environment.sh` to check the available tools.

## Important limitations

- A Wageningen B-series designation does not specify one complete geometry.
  Blade count, pitch ratio, area ratio, radial section shape, and hub
  dimensions must be identified for a specific configuration.
- The Wageningen B-series performance polynomials are reference models, not
  substitutes for a geometrically faithful CFD model.
- No geometry or experimental curve should be copied into this repository
  unless its redistribution terms are confirmed.
- The MRF method represents time-averaged relative rotation. It is not a
  transient simulation of individual blade passages.

## References

- International Towing Tank Conference, `Propulsion Committee`, final reports
  and recommended procedures for propeller testing and CFD.
- J. E. Kerwin, `Marine Propellers`, MIT OpenCourseWare.
- A. J. T. Oosterveld and P. van Oossanen, Wageningen B-screw series work.
- M. M. Bernitsas, D. Ray, and P. Kinley, `KT, KQ and Efficiency Curves for
  the Wageningen B-Series Propellers`, University of Michigan, 1981.
- OpenFOAM v2512 tutorials and program documentation installed with the local
  distribution.

## License

The repository license will be selected after confirming redistribution rights
for geometry and reference datasets. Repository software should not be treated
as granting rights to third-party geometry or published data.
