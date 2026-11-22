# 1. Propeller physics and force directions

## Learning objectives

By the end of this chapter, you should be able to explain how a propeller
produces thrust, distinguish a propeller's force from the reaction on its
support, and keep force, torque, and power signs consistent.

## 1.1 Physical picture

A marine propeller is a rotating set of lifting surfaces. Each blade section
experiences a relative flow composed principally of:

- axial inflow from the ship's motion through water;
- circumferential motion caused by propeller rotation;
- induced velocities created by the propeller itself.

The blade pressure field accelerates and turns water. The net force on all
blade and hub surfaces is the integral of pressure and viscous stress. The
propeller transfers axial momentum to the water; Newton's third law gives an
equal and opposite force on the propeller and its shaft support.

The phrase “thrust direction” is therefore ambiguous unless the body and axis
are specified. In this guide, $T$ denotes the **positive magnitude of
propeller-on-water axial force** in the downstream direction. The reaction
force on the propeller/hull points upstream. A CFD force-object output is a
vector on the selected body patches and may use either sign depending on the
surface-normal convention and axis orientation.

## 1.2 Control-volume momentum balance

For a steady, one-dimensional, incompressible control volume with a uniform
inlet and outlet and negligible wall shear, the axial momentum equation is

$$
\sum F_x = \dot m\,(V_{x,\mathrm{out}}-V_{x,\mathrm{in}}),
$$

where $\dot m$ is mass flow rate in kg/s and $V_x$ is the axial velocity in
m/s. In an idealized open-water propulsor, the water gains downstream momentum.
The propeller experiences the opposite reaction.

The full propeller flow is not one-dimensional: it includes nonuniform blade
loading, radial flow, swirl, a tip vortex, a hub wake, and viscous losses. The
control-volume balance is still useful as a global conservation check, but it
does not replace integration of blade and hub surface loads.

## 1.3 Thrust, torque, and power

Thrust $T$ is an axial force (N). Torque $Q$ is the moment about the shaft (N
m). A shaft rotating at $n$ rev/s has angular speed

$$
\Omega=2\pi n \qquad [\mathrm{rad/s}],
$$

and delivers power to the propeller

$$
P_D=Q\Omega=2\pi nQ \qquad [\mathrm W].
$$

The subscript $D$ denotes delivered power at the propeller shaft. The useful
thrust power in a uniform inflow is

$$
P_T=T V_A.
$$

These are not interchangeable. Shaft power must also supply wake kinetic energy,
swirl, and viscous dissipation; thrust power is the rate of useful work against
the advance speed.

## 1.4 Blade force resolution

At a blade section, hydrodynamic forces are conventionally resolved into lift
approximately perpendicular to local relative velocity and drag approximately
parallel to it. Their vector sum is projected onto the shaft axis and the local
tangential direction:

- the axial component contributes to thrust;
- the tangential component creates torque after multiplication by radius.

Pressure and viscous stress both contribute. For a well-designed lifting blade,
pressure forces often dominate integrated thrust, while viscous stress can be
important to torque and efficiency. The exact split depends on operating point,
Reynolds number, surface condition, and the numerical wall treatment.

## 1.5 Physical realization: a fan versus a propeller

A desk fan and a marine propeller both transfer momentum to a fluid. The
important difference is the operating environment and design objective. A ship
propeller operates in water at high density, is coupled to a hull wake, must
avoid excessive cavitation and vibration, and is constrained by diameter,
clearance, noise, strength, and engine matching. A visually similar air fan
does not provide a hydrodynamically equivalent blade geometry.

## 1.6 Project sign convention

The current case places the shaft axis on $+x$, uses an inlet velocity on $+x$,
and sets the force moment axis to $+x$. Before interpreting loads:

1. inspect the actual integrated force vector;
2. state whether it is fluid-on-propeller or propeller-on-fluid;
3. define positive thrust and torque axes;
4. verify moment sign by a right-hand-rule sketch;
5. compare against an independent hand calculation or a known simple case.

Do not silently apply `abs()` to a force or moment. A negative result can reveal
a sign convention error or a physically reversed operating condition.

## Engineering check

If torque is doubled at fixed $n$, then shaft power $P_D=2\pi nQ$ doubles. If
thrust is doubled at fixed $V_A$, useful thrust power also doubles. An efficiency
greater than one in a propeller open-water result is a warning to check units,
signs, or definitions; it is not an acceptable “high-performance” result.

## References

See [references and further reading](15_references.md), especially ITTC
open-water procedures and the MIT marine propulsion course.
