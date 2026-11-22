# Steady MRF simulation

## Baseline status

A serial, steady MRF baseline scaffold is provided for the reconstructed
B5-75 geometry. A v2512 test run initialized and reached 692 iterations before
manual stopping. It is not a converged or validated CFD result.

## Run

```bash
cd 04_MRF_Steady/baseline
./Allrun
```

For J = 0.80 with n = 10 rps and D = 0.24 m, the advance velocity is:

`VA = J n D = 1.92 m/s`
