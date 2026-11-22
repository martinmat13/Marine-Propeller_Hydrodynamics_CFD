# 6. Governing equations and turbulence closure

## 6.1 Continuum conservation laws

For an incompressible fluid with constant density, mass conservation is

$$
\nabla\cdot\mathbf{U}=0,
$$

where $\mathbf{U}$ is velocity in m/s.

The incompressible momentum equation, written per unit mass, is

$$
\frac{\partial\mathbf{U}}{\partial t}
+\nabla\cdot(\mathbf{U}\mathbf{U})
=-\nabla p+\nabla\cdot\boldsymbol{\tau}+\mathbf{f},
$$

where $p=p_{\mathrm{static}}/\rho$ is kinematic pressure in m$^2$/s$^2$,
$\boldsymbol{\tau}$ is viscous plus modeled turbulent stress divided by
density, and $\mathbf{f}$ contains body or rotating-frame source terms in
m/s$^2$.

For a Newtonian laminar fluid,

$$
\boldsymbol{\tau}_{\mathrm{lam}}
=\nu\left(\nabla\mathbf{U}+(\nabla\mathbf{U})^T\right).
$$

For constant $\nu$ and incompressible flow, its divergence reduces to
$\nu\nabla^2\mathbf{U}$.

## 6.2 RANS and turbulence model

RANS separates a time-mean velocity from fluctuations:

$$
\mathbf{u}=\overline{\mathbf{U}}+\mathbf{u}',
\qquad
\overline{\mathbf{u}'}=\mathbf{0}.
$$

Time averaging introduces the Reynolds-stress tensor
$-\overline{\mathbf{u}'\mathbf{u}'}$, which must be modeled. The
$k$-$\omega$ SST model solves transport equations for turbulent kinetic energy
$k$ and specific dissipation rate $\omega$, then constructs an eddy viscosity
$\nu_t$. The mean momentum equation is commonly written in an eddy-viscosity
form:

$$
\frac{\partial\overline{\mathbf{U}}}{\partial t}
+\nabla\cdot(\overline{\mathbf{U}}\overline{\mathbf{U}})
=-\nabla p
+\nabla\cdot\left[
(\nu+\nu_t)
\left(\nabla\overline{\mathbf{U}}+
(\nabla\overline{\mathbf{U}})^T\right)
\right]+\mathbf{f}.
$$

This closure approximates the mean effect of turbulence. It does not resolve
individual turbulent eddies or replace a suitable near-wall mesh.
The isotropic part of the modeled Reynolds stress can be absorbed into a
modified kinematic pressure; this is why the compact eddy-viscosity equation
above does not display a separate $-\tfrac23 k$ stress term.

## 6.3 What `simpleFoam` solves

The case selects `simpleFoam`, which solves a steady incompressible RANS
problem using SIMPLE pressure-velocity coupling. “Steady” means the computed
mean fields do not change with the solver iteration; iteration count is not
physical time.

The `steadyState` entry in `fvSchemes` removes a physical time derivative. The
algorithm alternates momentum prediction, pressure correction, and velocity
correction until a converged fixed point is reached or the iteration limit is
hit.

## 6.4 Discrete finite-volume form

For a control volume $V_P$, a conservation law is integrated over the cell.
The divergence theorem turns volume fluxes into face fluxes:

$$
\int_{V_P}\nabla\cdot\mathbf{F}\,dV
=\sum_{f}\mathbf{F}_f\cdot\mathbf{S}_f.
$$

The face values $\mathbf{F}_f$ are interpolated from neighboring cell values.
The choice of interpolation and gradient schemes affects numerical diffusion,
boundedness, and accuracy. In the case, `div(phi,U)` uses bounded
linear-upwind interpolation while turbulence transport uses upwind
interpolation. These are discretization choices, not physical models.

## 6.5 Pressure-velocity coupling

The predicted velocity from the momentum equation generally does not satisfy
discrete continuity. A pressure correction modifies face fluxes and velocity
so that

$$
\sum_f \phi_f=0
$$

for each cell, where $\phi_f$ is volumetric face flux for this
incompressible case. SIMPLE iterates this correction in a steady calculation.

## 6.6 Limitations

The current case does not include free-surface waves, cavitation, compressible
effects, or a hull. A steady RANS closure also cannot represent deterministic
blade-passage fluctuations. State these scope limits whenever discussing
results.

## References

See [references and further reading](15_references.md). The installed
OpenFOAM v2512 tutorial dictionaries are the syntax reference for the current
case; the official documentation link is included in the references.
