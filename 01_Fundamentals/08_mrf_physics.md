# 8. Multiple Reference Frame (MRF) physics

## Learning objectives

- Explain the difference between absolute and rotating-frame velocity.
- Understand the purpose and limits of MRF.
- Interpret the case's MRF axis, cell zone, origin, and angular speed.

## 8.1 Relative velocity in a rotating frame

Let $\boldsymbol{\Omega}$ be the angular-velocity vector and $\mathbf{r}$ the
position from the rotation origin. The local frame velocity is

$$
\mathbf{U}_{\mathrm{frame}}=
\boldsymbol{\Omega}\times\mathbf{r}.
$$

Absolute and relative velocities are related by

$$
\mathbf{U}_{\mathrm{abs}}
=\mathbf{U}_{\mathrm{rel}}+
\boldsymbol{\Omega}\times\mathbf{r}.
$$

For a frame rotating at constant angular velocity, the relative-frame
momentum equation contains Coriolis and centrifugal accelerations:

$$
\left.\frac{\partial\mathbf{U}_{\mathrm{rel}}}{\partial t}\right|_{\mathrm{rot}}
+(\mathbf{U}_{\mathrm{rel}}\cdot\nabla)\mathbf{U}_{\mathrm{rel}}
+2\boldsymbol{\Omega}\times\mathbf{U}_{\mathrm{rel}}
+\boldsymbol{\Omega}\times
(\boldsymbol{\Omega}\times\mathbf{r})
=-\nabla p+
\nabla\cdot\boldsymbol{\tau}
+\mathbf{f}_{\mathrm{other}}.
$$

Here $p$ is kinematic pressure and $\boldsymbol{\tau}$ is the viscous plus
modeled turbulent stress per unit density. The equation assumes constant
$\boldsymbol{\Omega}$; an accelerating frame adds the Euler acceleration
$\dot{\boldsymbol{\Omega}}\times\mathbf{r}$. The signs and exact representation
depend on whether the solver equation is written in relative or absolute form.
OpenFOAM's MRF model handles the transformation and source terms; do not add
these terms a second time by hand.

## 8.2 MRF versus sliding mesh

MRF solves a steady flow using a rotating cell-zone model and a fixed mesh. The
rotor is effectively frozen at one angular position relative to the stationary
domain. It can estimate mean loading economically when the interaction is
approximately steady.

Sliding mesh rotates the mesh region in time and resolves relative motion of
rotor/stator or blade/wake structures. It requires transient computation and
appropriate interface treatment.

MRF does not resolve blade-passage histories, time-varying blade loads, or
phase-resolved wake interaction. Agreement between MRF and a reference curve
does not prove transient physics are resolved.

## 8.3 Current case setup

The case uses:

```text
cellZone    rotor;
origin      (0 0 0);
axis        (1 0 0);
omega       62.83185307179586;
```

This represents positive rotation around the $x$ axis at
$\Omega=2\pi(10)=62.83$ rad/s. The zone is selected by a box in
[`topoSetDict`](../04_MRF_Steady/baseline/system/topoSetDict), not by an
axisymmetric cylinder. A cylindrical zone with adequate clearance is preferable
for a production-quality propeller setup, subject to interface/domain design.

The B5-75 blade radius is approximately 0.12 m; the selected zone extends to
about 0.15 m in coordinate directions. Check the actual meshed zone and its
interface before interpreting results.

## 8.4 Coordinate consistency

For the current geometry convention, the shaft is on $x$ and inflow is along
$+x$. The right-hand rule defines positive $\Omega$ around $+x$. Reverse the
rotation sign or axis as needed to match propeller handedness and advance
direction. Verify:

1. the inlet vector and shaft axis;
2. the handedness of the geometry;
3. the sign of the computed shaft moment;
4. the sign of the propeller reaction thrust.

## 8.5 MRF assumptions and checks

- The rotating zone must include the complete rotor and adequate near field.
- MRF interfaces must not pass through the blade surface.
- The same cell zone named in `MRFProperties` must exist in the mesh.
- The interface should not introduce severe abrupt changes in cell size.
- Outer patches intended to remain stationary must be handled correctly.
- Force integration must use the correct body surface and reference axis.

## References

Use the v2512 tutorial `incompressible/simpleFoam/mixerVessel2D` as installed
with OpenFOAM for dictionary syntax. See also OpenFOAM's MRF and rotating-frame
documentation in [references](15_references.md).
