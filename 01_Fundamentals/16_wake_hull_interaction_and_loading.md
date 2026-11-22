# 16. Wake, blade loading, and ship propulsion

## 16.1 Uniform inflow and ship wake

In an open-water test, the propeller is placed in a controlled, approximately
uniform inflow of speed $V_A$. Behind a ship, the local inflow varies with
radius and angular position because of the boundary layer, hull form, appendages,
and free-surface flow. The propeller then experiences a nonuniform wake.

The **wake fraction** $w$ is commonly defined by

$$
w=\frac{V_S-V_A}{V_S},
\qquad
V_A=(1-w)V_S,
$$

where $V_S$ is ship speed and $V_A$ is the effective mean advance speed at the
propeller. Exact definitions and measurement methods depend on the experimental
procedure.

A nonuniform wake may cause blade loads to vary as each blade rotates through
different local inflow velocities. This can create cyclic thrust and torque,
vibration, and acoustic excitation. A steady MRF field does not provide
phase-resolved blade-passage load histories.

## 16.2 Propeller loading versus blade loading

**Propeller loading** can refer to an integrated measure, such as disk thrust
loading:

$$
\frac{T}{A_0},\qquad A_0=\frac{\pi D^2}{4}.
$$

Its units are pressure (Pa). High disk loading generally requires a stronger
velocity change and can increase induced losses.

**Blade loading** refers to load distribution over blade radius and chord.
It is often expressed as sectional force per unit span, pressure coefficient,
or local surface pressure. Two propellers with equal total thrust can have
different blade loading distributions and therefore different structural,
cavitation, vibration, and efficiency behavior.

Integrated thrust alone cannot reveal whether load is concentrated near the
root, tip, leading edge, or a particular blade region.

## 16.3 Pressure forces and viscous effects

Pressure acts normal to the surface; viscous stress acts tangentially in the
continuum stress decomposition. Their integrated contributions can be written

$$
\mathbf{F}=\mathbf{F}_p+\mathbf{F}_v.
$$

Pressure distribution produces the dominant lifting action on many propeller
blades. Viscous shear contributes to skin-friction drag and torque, affects
boundary-layer development, and can influence separation and pressure recovery.
The exact fraction is operating-point and geometry dependent. A force-object
split into pressure and viscous terms is a useful diagnostic, not a license to
neglect the smaller term.

“Pressure drag” is not identical to “viscous drag”: pressure forces can produce
both useful lift and pressure/form drag, while viscous stress produces shear
force. The total force must be interpreted by vector projection and flow
physics.

## 16.4 Hull-propeller efficiency chain

A common decomposition of overall propulsive efficiency is

$$
\eta_D=\eta_H\eta_R\eta_0\eta_S,
\qquad
\eta_H=\frac{1-t}{1-w},
$$

where:

- $\eta_0$ is open-water propeller efficiency;
- $\eta_H$ is hull efficiency;
- $\eta_R$ is relative rotative efficiency;
- $\eta_S$ is shaft efficiency;
- $w$ is wake fraction;
- $t$ is thrust-deduction fraction.

Under the common convention, thrust deduction is $t=(T_R-T)/T_R$, where $T_R$
is the resistance-equivalent bare-hull force and $T$ is the propeller thrust
required with the propeller installed. Definitions can vary; cite the chosen
standard. These interaction factors cannot be inferred from the current
isolated-propeller case.

## 16.5 Delivered power and engine power

Delivered power is the shaft power arriving at the propeller:

$$
P_D=2\pi nQ.
$$

Brake or engine power is upstream of shafting losses. If shaft efficiency is
$\eta_S=P_D/P_B$, then

$$
P_B=\frac{P_D}{\eta_S}.
$$

Do not label $P_D$ as engine brake power unless drivetrain losses are included.

## Learning takeaways

- Wake inflow and propeller advance speed are related but are not generally
  equal to ship speed.
- Equal integrated thrust does not imply equal local blade loading.
- Pressure and viscous stresses both contribute to propeller loads.
- Open-water efficiency is one factor in, not a synonym for, overall ship
  propulsion efficiency.

## References

See [references and further reading](15_references.md), especially ITTC
propulsion procedures and marine-propeller textbooks.
