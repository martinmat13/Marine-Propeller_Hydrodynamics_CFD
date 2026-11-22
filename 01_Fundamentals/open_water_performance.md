# Open-water performance

## Learning objectives

- Define advance, thrust, torque, and efficiency coefficients.
- Explain uniform-inflow open-water conditions.
- Interpret polynomial reference curves without confusing them with CFD data.

## Operating coefficients

Advance coefficient:

`J = VA / (nD)`

Thrust coefficient:

`KT = T / (rho n^2 D^4)`

Torque coefficient:

`KQ = Q / (rho n^2 D^5)`

Open-water efficiency:

`eta0 = J / (2 pi) * KT / KQ`

## Baseline condition

The first test uses:

- diameter `D = 0.240 m`
- rotational speed `n = 10 rps`
- advance speed `VA = 1.92 m/s`
- corresponding advance coefficient `J = 0.80`

The corresponding MRF angular speed is `omega = 62.831853 rad/s`.

## Interpretation

The first coefficient curve added to the repository is generated from the
Wageningen B-series polynomial, not a raw experimental dataset. It is a
literature reference for comparison and is not evidence of CFD validation.
