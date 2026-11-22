# 10. Computational domain, mesh, and near-wall resolution

## 10.1 Domain sizing

The current background block extends from $x=-1.44$ m to $x=2.40$ m, and from
$y,z=-0.72$ m to $+0.72$ m. For $D=0.24$ m, the inlet is 6D upstream and the
outlet is 10D downstream, for 16D total axial length. The transverse dimensions
are each 6D. The propeller shaft origin is at the center.

Domain-size adequacy is not established by these values alone. Repeat with
farther boundaries or compare with a trusted guideline if blockage, pressure
recovery, or wake truncation might affect integrated loads.

## 10.2 Mesh components

- **Background mesh:** structured hexahedra from `blockMesh`.
- **Surface refinement:** local cells near the propeller from
  `snappyHexMesh`.
- **Near-wall layers:** prismatic cells intended to resolve or model wall
  gradients; the current dictionary has `addLayers false`.
- **Rotating zone:** cells selected by `topoSet` and referenced by MRF.
- **Wake refinement:** additional downstream resolution needed to capture
  velocity deficit and swirl.

Resolution should follow flow physics, not a target cell count alone. Tip
vortices and blade leading edges require strong local refinement. A mesh with
large cells aligned poorly to a curved blade can smear pressure gradients.

## 10.3 Wall coordinate $y^+$

The viscous wall coordinate is

$$
y^+=\frac{u_\tau y_1}{\nu},
\qquad
u_\tau=\sqrt{\frac{|\tau_w|}{\rho}},
$$

where $y_1$ is distance from the wall to the first cell center and $u_\tau$ is
friction velocity.

Wall-resolved RANS generally targets $y^+$ near unity; conventional log-layer
wall functions generally require a first cell in the log layer, often
$y^+$ on the order of tens to a few hundred. The correct target depends on the
wall treatment and model. The current case uses a Spalding-type `nut` wall
function and has no explicit layer mesh, so its achieved $y^+$ must be measured
after a physically usable mesh exists.

Do not claim a $y^+$ target was met without calculating and plotting the
surface distribution. Avoid broad ranges presented as universal acceptance
criteria.

## 10.4 Mesh quality metrics

Use `checkMesh` to inspect at least:

- maximum and average non-orthogonality;
- skewness;
- cell volume and negative/near-zero volumes;
- face pyramid/tet quality;
- aspect ratio and cell-size jumps;
- patch topology and connectedness;
- cell-zone extent and count.

The current test mesh has one highly skew face (reported maximum skewness
4.23) and fails one default quality check. Do not ignore it simply because the
solver runs.

## 10.5 Mesh-independence plan

Create at least three systematically refined meshes while keeping geometry,
domain, physics, boundary conditions, discretization, and convergence criteria
fixed. Compare $T$, $Q$, $K_T$, $K_Q$, and $\eta_0$. Report both changes and
mesh sizes. If using a Grid Convergence Index, state the refinement ratio,
observed order assumptions, and whether asymptotic behavior is plausible.

## References

See the OpenFOAM snappyHexMesh documentation and ITTC CFD uncertainty guidance
in [references and further reading](15_references.md).
