# 2. Actuator-disk momentum theory

## Learning objectives

- Derive the ideal relation between thrust and slipstream acceleration.
- Explain induced velocity and ideal propulsive efficiency.
- Recognize the omissions that make actuator-disk theory unsuitable as a blade
  load prediction method.

## 2.1 Model and assumptions

Replace the finite-bladed propeller with an infinitely thin disk that applies
uniform pressure rise to an inviscid streamtube. Assume steady, incompressible,
axisymmetric, one-dimensional flow; no swirl; uniform far-upstream speed
$V_A$; and uniform far-wake speed $V_w$. The disk-plane speed is $V_d$.

Bernoulli's equation is applied separately upstream and downstream of the disk
because pressure jumps across the disk. In the ideal actuator-disk model,

$$
V_d=\frac{V_A+V_w}{2}.
$$

Define the axial induced velocity at the disk as $v_i=V_d-V_A$. Then

$$
V_w=V_A+2v_i.
$$

The disk accelerates water through a streamtube. With disk area
$A=\pi D^2/4$, continuity gives $\dot m=\rho A V_d$ for this idealized model.
The axial momentum rise and thrust magnitude are

$$
T=\dot m(V_w-V_A)
 =\rho A V_d(2v_i)
 =2\rho A V_d v_i.
$$

The last equality is an ideal actuator-disk result; do not apply it directly to
local blade loads.

## 2.2 Pressure and power

The pressure jump across the disk is

$$
\Delta p=\frac{T}{A}.
$$

The rate at which the disk does work on the water is

$$
P_D=T V_d.
$$

The useful thrust power at the undisturbed advance speed is $P_T=T V_A$.
Therefore ideal propulsive efficiency is

$$
\eta_{\mathrm{ideal}}
 =\frac{T V_A}{T V_d}
 =\frac{V_A}{V_d}
 =\frac{2V_A}{V_A+V_w}
 =\frac{V_A}{V_A+v_i}.
$$

This explains why excessive induced velocity costs efficiency: the propulsor
must put more energy into the wake than is needed to provide the same thrust.
For a stationary propeller in still water, the ideal actuator-disk limit tends
to zero useful efficiency as $V_A\to0$: thrust can exist, but useful power
$TV_A$ at zero advance speed is zero.

## 2.3 Example

Suppose a propeller advances through undisturbed water at $V_A=2.0$ m/s and the
ideal disk induces $v_i=0.5$ m/s. Then $V_d=2.5$ m/s and $V_w=3.0$ m/s. Ideal
efficiency is

$$
\eta_{\mathrm{ideal}}=\frac{2.0}{2.5}=0.80.
$$

The remaining 20% in this idealized power ratio is associated with energy left
in the accelerated slipstream. This is not a prediction for the repository's
propeller; it is a momentum-theory illustration.

## 2.4 Why CFD needs blades

Actuator-disk theory omits:

- discrete blade pressure distributions and blade-to-blade variation;
- finite-blade and tip-vortex physics;
- blade-section profile drag and boundary layers;
- hub and blade-root interactions;
- wake swirl and radial flow;
- cavitation and free-surface effects.

It is a valuable scaling and sanity-check model, not an exact CFD boundary
condition or replacement for a validated geometry.

## Check your understanding

1. Why does a stationary thruster create a wake but have zero useful thrust
   power under the definition $P_T=TV_A$?
2. What additional kinetic energy does swirl carry that this model neglects?
3. Why is the disk velocity the average of far-upstream and far-wake velocities
   in the ideal model?

## References

See [references and further reading](15_references.md).
