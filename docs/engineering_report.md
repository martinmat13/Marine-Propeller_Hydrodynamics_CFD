# Engineering report

## Executive summary

The repository is under development. No CFD result or validated coefficient
prediction is available yet.

## Configuration

The baseline configuration is a reconstructed Wageningen B5-75:

- Z = 5
- D = 0.240 m
- P/D = 1.20
- EAR = 0.75
- hub diameter ratio = 1/6

## Numerical method

The intended baseline is steady incompressible `simpleFoam` with k-omega SST
turbulence and a rotating MRF cell zone.

## Reference

The included performance curve is calculated from the published polynomial
correlations attributed to Oosterveld and van Oossanen (1975). It is not raw
experimental model-test data.

## Limitations

- The blade STL is a parametric reconstruction.
- Rake and skew are omitted.
- No mesh-independence study has been run.
- No validation claim is made.
