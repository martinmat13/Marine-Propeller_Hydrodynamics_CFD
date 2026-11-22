# Project roadmap

## Learning objectives

- Understand the physical and numerical basis of open-water propeller CFD.
- Build a reproducible OpenFOAM v2512 case without inventing data.
- Separate verification, reference prediction, and physical validation.
- Produce portfolio-quality documentation and selected post-processing outputs.

## Milestone 1: Marine propulsion fundamentals

Status: in progress.

Deliverables:

- Marine propeller thrust and momentum explanation
- Blade geometry and open-water performance concepts
- Governing equations and coefficient definitions
- Environment inspection record
- Initial repository structure

## Milestone 2: Geometry and reference data

Status: blocked until a traceable configuration is selected.

Required decisions:

- five-bladed Wageningen B-series configuration
- pitch ratio and blade-area ratio
- diameter and nondimensional section coordinates
- hub geometry
- approved reference curves
- redistribution and attribution terms

No synthetic blade description may be represented as an authentic published
geometry.

## Milestone 3: Steady MRF case

Status: planned.

The baseline will use `simpleFoam` and an MRF cell zone. It will first be
developed in serial, on a small mesh, and with only basic operating conditions.

## Milestone 4: Verification and validation

Status: planned.

Verification will include mesh sensitivity, residual monitoring, iterative
convergence, force convergence, and implementation checks.

Physical validation will require comparison with traceable experimental or
published open-water data. Agreement will be reported with absolute and relative
error, not as a subjective visual match.
