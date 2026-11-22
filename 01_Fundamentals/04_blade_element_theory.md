# 4. Blade-element theory

## Learning objectives

- Resolve local inflow into axial and tangential components.
- Relate section lift and drag to propeller thrust and torque.
- Understand why blade-element theory is local and requires sectional data.

## 4.1 Local kinematics

At radius $r$, let the undisturbed axial speed be $V_A$, axial induced velocity
be $v_a$, and tangential induced velocity magnitude be $v_t$. The blade's
rotational speed relative to the water is $\Omega r$. Under one common sign
convention, relative velocity components are

$$
V_x=V_A+v_a,\qquad
V_\theta=\Omega r-v_t,
$$

and the relative speed and inflow angle are

$$
W=\sqrt{V_x^2+V_\theta^2},\qquad
\phi=\tan^{-1}\left(\frac{V_x}{V_\theta}\right).
$$

The local geometric pitch angle is $\beta(r)$. Section angle of attack is
approximately

$$
\alpha=\beta-\phi.
$$

The exact signs depend on propeller handedness and the chosen direction of
rotation. A calculation should define the convention rather than rely on a
diagram from another coordinate system.

## 4.2 Section lift and drag

For one blade section of chord $c$ and radial width $dr$, quasi-steady section
loads are approximated as

$$
dL=\frac12\rho W^2 c C_L\,dr,\qquad
dD_f=\frac12\rho W^2 c C_D\,dr,
$$

where $C_L$ and $C_D$ depend on section shape, Reynolds number, transition,
roughness, and angle of attack.

Projecting these loads onto axial and tangential directions gives one common
first-quadrant convention:

$$
dT_{\mathrm{blade}}=dL\cos\phi-dD_f\sin\phi,
$$

$$
dF_{\theta,\mathrm{blade}}=dL\sin\phi+dD_f\cos\phi,
\qquad
dQ_{\mathrm{blade}}=r\,dF_{\theta,\mathrm{blade}}.
$$

For $Z$ identical blades, multiply the section contribution by $Z$ for an
axisymmetric mean model. A full CFD solution instead integrates actual surface
traction and does not need these section force projections.

## 4.3 Blade-element momentum (BEM) coupling

Blade-element theory alone needs induced velocities. Momentum theory alone
does not resolve blade forces. Blade-element momentum theory equates the
annular blade-element thrust/torque to the momentum changes in an annular
streamtube and solves for induced velocities.

Practical BEM methods add finite-blade corrections, root/tip loss factors,
empirical corrections, and robust iteration strategies. Their results are
sensitive to sectional polars and geometry. A BEM result is not equivalent to
RANS CFD and neither is automatically validated.

## 4.4 Why the present geometry prevents meaningful BEM/CFD loads

The current STL generator does not create closed upper and lower blade
surfaces or full B-series section coordinates. It also omits exact skew and
rake. Therefore its CFD surface forces cannot be interpreted as the loading of
a true B5-75. This is not fixed by using a finer mesh: mesh refinement reduces
discretization error for the specified surface; it cannot correct an
inaccurate surface.

## Physical intuition

Near the hub, rotational speed $\Omega r$ is small and the section often sees a
large inflow angle. Near the tip, rotational speed is large, local dynamic
pressure scales as $W^2$, and a small tip-vortex region can have strong
velocity and pressure gradients. This helps explain why uniform radial
resolution is inefficient.

## References

See [references and further reading](15_references.md), especially Kerwin's
marine propeller notes and standard lifting-line/BEM texts.
