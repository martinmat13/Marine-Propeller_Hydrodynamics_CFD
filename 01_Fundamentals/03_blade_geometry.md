# 3. Propeller blade geometry and Wageningen B-series notation

## Learning objectives

- Read a B-series designation and state what it does and does not specify.
- Explain pitch, chord, rake, skew, expanded area ratio, and hub ratio.
- Identify why geometry provenance matters to CFD validation.

## 3.1 B5-75 is not a complete CAD specification

In the Wageningen B-series designation, `B5-75` identifies the B-series family,
five blades, and expanded area ratio $A_E/A_0=0.75$. It does not alone identify
pitch ratio, diameter, hub construction, section coordinates, or exact
manufacturing geometry.

The project selects the **B5-75, $P/D=1.20$** family configuration. The
0.240 m diameter in the current case is a convenient scale selected for the
workflow; it is not claimed to be the diameter of a particular original model
test.

## 3.2 Principal dimensions

| Quantity | Definition | Interpretation |
|---|---|---|
| $D$ | Tip-to-tip diameter | Sets disk size and dimensional scaling |
| $R=D/2$ | Radius | Radial coordinate is often reported as $r/R$ |
| $Z$ | Blade count | Number of repeated blades |
| $P(r)$ | Local geometric pitch | Helical advance associated with a radial section |
| $P/D$ | Pitch ratio | Nondimensional nominal pitch |
| $c(r)$ | Chord | Section width in the local blade plane |
| $A_E/A_0$ | Expanded area ratio | Developed blade area / disk area |
| $d_h/D$ | Hub diameter ratio | Hub size relative to propeller diameter |

The **expanded** blade area is the sum of blade areas developed into a plane;
it is not the projected blade area. The disk area is $A_0=\pi D^2/4$.

## 3.3 Pitch and pitch angle

For a helix of pitch $P$ at radius $r$, the geometric helix angle measured from
the plane of rotation satisfies

$$
\tan\beta(r)=\frac{P(r)}{2\pi r}.
$$

Equivalently, if $x=r/R$ and local pitch ratio is $P(r)/D$,

$$
\tan\beta(x)=\frac{P(r)/D}{\pi x}.
$$

Geometric pitch is not the actual advance per revolution of a loaded propeller.
Slip and induced velocities make the hydrodynamic advance different.

## 3.4 Chord, thickness, skew, and rake

- **Chord distribution** $c(r)$ controls local planform and affects area and
  loading.
- **Thickness distribution** influences structural strength, cavitation
  resistance, wetted area, and section pressure gradients.
- **Skew** is a circumferential sweep of sections with radius. It changes
  unsteady loading and can reduce vibration in a nonuniform wake.
- **Rake** is an axial displacement of sections with radius. It changes blade
  shape, clearance, and structural load paths.
- **Hub geometry** affects root flow, torque transfer, and the hub wake.

These features cannot be reconstructed from blade count and pitch ratio alone.

## 3.5 Dimensional laws versus section coordinates

Published B-series regressions provide nondimensional performance as a function
of advance coefficient, pitch ratio, area ratio, and blade count. Geometry
tables may provide chord/thickness laws and section ordinates. Reconstructing a
solid blade requires both planform and full radial section shape, correct
section orientation, finite leading/trailing edge treatment, root blending,
hub join, and watertight topology.

The current [`generate_geometry.py`](../02_Geometry/generate_geometry.py) uses a
small set of radial shape values and five chordwise points. It does **not**
implement the published complete section ordinate functions. Its output is a
mesh-workflow proxy and cannot support quantitative propeller performance.

## 3.6 Useful geometric checks

Before meshing a future authoritative geometry:

1. check blade count, handedness, and shaft axis;
2. plot $c/D$, $t/D$, and pitch angle against $r/R$;
3. verify positive thickness and no self-intersection;
4. inspect the leading edge and trailing edge at each radial station;
5. check blade-hub intersection and tip closure;
6. ensure a watertight closed surface with consistent normals;
7. compare CAD dimensions against the source tables;
8. record source, units, transformations, and licensing.

## References

Oosterveld and van Oossanen (1975), Kuiper (1992), and Foeth (2019) are listed
in [references and further reading](15_references.md). Geometry sources and
limitations are also documented in [`02_Geometry/README.md`](../02_Geometry/README.md).
