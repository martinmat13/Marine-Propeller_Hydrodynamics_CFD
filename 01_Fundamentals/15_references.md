# References and further reading

The following references are intended to support the physics, test methodology,
and OpenFOAM implementation. Use the edition and procedure revision applicable
to your work.

## Marine propulsion and propeller theory

1. MIT OpenCourseWare. (Fall 2006). *2.611 Marine Power and Propulsion*.
   Course materials include marine propeller theory.
   [Course materials](https://ocw.mit.edu/courses/2-611-marine-power-and-propulsion-fall-2006/)

2. Carlton, J. (2012). *Marine Propellers and Propulsion*, 3rd ed.
   Butterworth-Heinemann. ISBN 978-0-08-097123-0.
   [Publisher page](https://shop.elsevier.com/books/marine-propellers-and-propulsion/carlton/978-0-08-097123-0)

## Wageningen B-series

3. Oosterveld, M. W. C., and van Oossanen, P. (1975). “Further computer-
   analyzed data of the Wageningen B-screw series.” *International
   Shipbuilding Progress*, 22(251), 251–262.
   [DOI: 10.3233/ISP-1975-2225102](https://doi.org/10.3233/ISP-1975-2225102)

4. Bernitsas, M. M., Ray, D., and Kinley, P. (1981). *KT, KQ and Efficiency
   Curves for the Wageningen B-Series Propellers*. University of Michigan,
   Department of Naval Architecture and Marine Engineering.

5. Kuiper, G. (1992). *The Wageningen Propeller Series*. MARIN Publication
   92-001. Wageningen.

6. Foeth, E. J. (2019). “Remodeling the B-series geometry in a CAD
   environment.” *Proceedings of the Sixth International Symposium on Marine
   Propulsors*, Rome.
   [Proceedings PDF](https://www.marinepropulsors.com/proceedings/2019/MA2-2.pdf)

## Test procedures and uncertainty

7. International Towing Tank Conference (ITTC). *Recommended Procedures and
   Guidelines*, including the current procedures for open-water propeller
   testing, propulsion tests, and CFD verification/validation.
   [ITTC official website](https://www.ittc.info/)
   Find the latest procedure number and revision through the ITTC site before
   using it for a formal test or report; revisions change over time.

## OpenFOAM

8. OpenCFD Ltd. *OpenFOAM Documentation*, `simpleFoam` solver (v2312
   documentation). The local project uses v2512; local tutorials and runtime
   behavior take precedence for version-specific syntax.
   [simpleFoam](https://doc.openfoam.com/2312/tools/processing/solvers/rtm/incompressible/simpleFoam/)

9. OpenCFD Ltd. *OpenFOAM Documentation*, `forces` function object.
   [forces](https://doc.openfoam.com/2312/tools/post-processing/function-objects/forces/forces/)

10. OpenFOAM v2512 local tutorial references include
    `$FOAM_TUTORIALS/incompressible/simpleFoam/rotatingCylinders` for MRF
    dictionary syntax and
    `$FOAM_TUTORIALS/incompressible/pimpleFoam/RAS/propeller` for propeller
    force-object examples. These are installed with the selected software and
    should be inspected directly.

## Technical citation policy

- Cite the original source for a formula or data table when possible.
- Cite the exact OpenFOAM version for dictionary claims.
- Do not cite an implementation repository as the original source of
  experimental measurements.
- The project CSV is a generated evaluation of a published regression, not a
  raw measurement dataset.
- Confirm bibliographic details and redistribution terms before final public
  release.
