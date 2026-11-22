# Self-assessment and worked checks

Use these questions after reading the linked chapters. Each solution is brief;
write out the units and sign conventions before checking it.

## Questions

1. A propeller has $D=0.24$ m and rotates at 600 rpm. Convert rpm to $n$ and
   $\Omega$.
2. At $J=0.8$, what is $V_A$?
3. A coefficient data file lists $10K_Q=0.50$. What value belongs in the
   efficiency equation?
4. Given $J=0.8$, $K_T=0.25$, and $K_Q=0.05$, estimate $\eta_0$.
5. Why can a steady MRF run not report the time history of a blade passing
   behind a ship's nonuniform wake?
6. Residuals have fallen by four orders of magnitude, but shaft torque still
   drifts. Is the result converged for performance reporting?
7. Why is a mesh refinement study unable to repair a wrong section shape?
8. Name the additional evidence needed before a single-phase pressure contour
   can support a cavitation claim.
9. At fixed $J$, $n$, and coefficients, how do thrust and torque scale if $D$
   is doubled?
10. What is the difference between open-water efficiency and delivered-power
    efficiency for a ship propulsion chain?

## Answers

1. $n=600/60=10$ rev/s; $\Omega=2\pi n=62.83$ rad/s.
2. $V_A=JnD=(0.8)(10)(0.24)=1.92$ m/s.
3. $K_Q=0.50/10=0.05$.
4. $\eta_0=(0.8/(2\pi))(0.25/0.05)\approx0.637$.
5. MRF uses a fixed mesh and steady rotating-frame representation; it does not
   resolve the moving blade through a time-varying wake. A sliding-mesh
   transient setup is required for phase-resolved blade passage.
6. No. Integrated force histories must also stabilize, with an explicit
   averaging window and reported variation.
7. Refinement addresses numerical discretization error for the specified
   geometry. It cannot change model-form or geometric error.
8. A cavitation model, absolute pressure reference, water temperature/vapor
   pressure, cavitation number definition, suitable mesh and time resolution,
   plus comparison with credible cavitation data.
9. From $T\propto D^4$, thrust increases by 16; from $Q\propto D^5$, torque
   increases by 32, if nondimensional similarity holds. Reynolds and cavitation
   similarity may not hold in practice.
10. $\eta_0$ is propeller thrust power divided by delivered shaft power in
    uniform inflow. Ship-level delivered-power efficiency includes hull,
    relative-rotative, and shaft effects under a stated convention.
