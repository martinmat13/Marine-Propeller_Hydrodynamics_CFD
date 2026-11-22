# Marine propeller physics

## Learning objectives

After studying this document, the reader should be able to:

1. Explain how a propeller transfers momentum to the surrounding water.
2. Distinguish thrust, torque, propeller power, and delivered power.
3. Explain the meaning of open-water advance coefficient and efficiency.
4. Describe blade loading and blade-element action in simple terms.
5. Identify why propeller CFD requires a documented geometry and operating data.

## 1. How thrust is generated

A propeller blade is a rotating foil. Its local angle of attack generates lift
and drag, and the component of the integrated pressure and viscous forces
resolved along the shaft axis produces propulsive thrust.

The fluid is accelerated through the propeller disk. In a vessel-fixed reference
frame, momentum leaving downstream is greater than momentum entering upstream.
The resulting reaction force acts in the opposite direction and is transmitted
through the shaft and hull.

For a control volume enclosing the propeller,

`T = mdot * (w_exit - w_in)` in the actuator-disk idealization,

where `mdot` is the mass flow rate and `w` is axial velocity. Real propellers
have nonuniform wakes, swirl, viscous losses, and blade-tip effects, so this
equation is a conceptual model rather than a complete CFD formula.

## 2. Thrust and torque

Thrust `T` is the axial force produced by the propeller, measured in newtons.

Torque `Q` is the shaft moment required to rotate the propeller, measured in
newton-metres.

The corresponding shaft power is:

`P_D = 2 * pi * n * Q`

where `n` is rotational speed in revolutions per second.

Useful propulsive power in the open-water actuator-disk idealization is:

`P_T = T * V_A`

where `V_A` is advance speed in metres per second.

Open-water efficiency is:

`eta_0 = P_T / P_D = (J / (2*pi)) * (K_T / K_Q)`

It describes propulsive conversion in uniform inflow and must not be confused
with overall ship propulsion efficiency.

## 3. Blade geometry

Propeller geometry is defined at radial stations. Important terms include:

- **Diameter `D`**: twice the maximum blade radius.
- **Pitch `P`**: the axial advance implied by a blade-section helix.
- **Pitch ratio `P/D`**: pitch normalized by diameter.
- **Chord `c(r)`**: blade width at radius `r`.
- **Rake**: axial offset of sections.
- **Skew**: circumferential offset of sections.
- **Expanded area ratio**: developed blade area divided by the propeller disk area.
- **Hub dimensions**: radius, length, and fairing shape.

A Wageningen B-series name or blade count alone does not identify all of these
features. The project therefore cannot start from a generic five-blade shape.

## 4. Operating coefficients

Advance coefficient:

`J = V_A / (nD)`

Thrust coefficient:

`K_T = T / (rho * n^2 * D^4)`

Torque coefficient:

`K_Q = Q / (rho * n^2 * D^5)`

At a fixed `J`, these coefficients help compare geometrically similar
propellers. SI units must be retained consistently even though `n` is often
reported in revolutions per second rather than radians per second.

## 5. Rotating-frame CFD

The MRF approach places a steady model of propeller rotation inside a rotating
cell zone. It adds rotational source terms to the momentum equations and assumes
a time-averaged field. The exterior domain remains stationary.

An MRF simulation is suitable for an initial open-water baseline. It is not
suitable for transient blade-vortex interaction, wake passage, or cavitation
sheet dynamics unless combined with more advanced modelling.

## 6. Verification and validation

- **Verification** asks whether the equations and numerical implementation are
  solved correctly.
- **Validation** asks whether the verified model represents a physical
  experiment accurately enough for the intended purpose.

Required verification evidence includes mesh independence, residual behavior,
and force convergence. Validation requires published or experimentally measured
open-water `K_T`, `K_Q`, and `eta_0` curves for the documented geometry.

## 7. Common errors

- Using the wrong shaft axis or force moment axis.
- Reporting torque and thrust with inconsistent sign conventions.
- Using revolutions per minute in a coefficient formula without conversion.
- Calling a generic Wageningen curve an exact geometric comparison.
- Confusing open-water efficiency with ship propulsion efficiency.
- Starting with a dense mesh before checking the boundary conditions.

## 8. References

- ITTC, Recommended Procedures and Guidelines for Propulsion, Test and
  Propulsors.
- J. E. Kerwin, `Marine Propellers`, MIT OpenCourseWare.
- M. Carlton, `Marine Propellers and Propulsion`.
- OpenFOAM v2512 MRFProperties and simpleFoam tutorials installed in
  `/usr/lib/openfoam/openfoam2512/tutorials`.
