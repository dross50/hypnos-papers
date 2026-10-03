# Section 4, explained: Constructing the leading order flow (pages 24 to 45)

## The problem this section is handed

The force is the momentum residual of the constructed flow, so the task is a blowup whose residual stays smooth through t = 1 [p. 3]. Section 2 pictures a slender self-similar vortex, spiraling inward and flowing out along the axis, joined across an annulus to a decaying exterior swirl; the join leaves an unbounded annular residual that shear-amplified ring pulses must cancel with their averaged momentum fluxes [pp. 3 to 6].

In Section 3's terms, pulses cancel the residual through the rθ and rz entries of their averaged covariance, as a positive combination of two families' covariance vectors [pp. 10, 12]. So Section 4 must produce profiles whose leading tangential residual is minus the radial divergence of a stress T that vanishes near the axis and in the exterior, points strictly inside the cone the two families span, and sits beside a residual-free exterior that can later be cut off [pp. 6, 9, 24]. Later sections need more: analyticity in η near the axis for Section 5 [p. 47], an edge weight for Section 6 [p. 69], positive shear bounds and a cone margin reaching the annulus edges for Section 7 [p. 74], and untouched intervals for Sections 5 and 8 [pp. 33, 34].

## What a person would try first, and why it fails

**An isotropic self-similar vortex.** The natural guess is Leray scaling: lengths like τ^{1/2}, velocities like τ^{-1/2}. Then every ratio the construction runs on is of order one: axial over radial diffusion (q^{2h} in the paper), rotation over radial diffusion (q^{-h}), pulse wavelength over core radius (q^{h/2}) [pp. 4, 8, 11]. Nothing orders corrections or makes pulses short relative to the core (our reading). The paper's axial length τ^{1/2-h}, with swirl and axial speeds τ^{-1/2-h}, instead puts axial transport, radial transport and radial diffusion all at rate τ^{-1} [pp. 4, 5].

**A symmetric axial profile.** The paper names the failure: under reflection symmetry about z = 0, midplane axial transport of angular momentum vanishes, and u_z = 0 there leaves no axial shear to compensate [p. 5]. In Section 4's terms, with axis data U* = 4η the transport coefficient H* and the axial source Z* both vanish at η = 0, since the axis pressure is even (our reading of [pp. 35, 37]). The paper adds a small upward offset, U* = 4η + j0, and its pressure bounds make Z* positive where H* vanishes [p. 37].

**A stress wherever the residual happens to be.** Near the axis the swirl is locally a rigid rotation: from l = 1 + XF_X/F and a = 2 - 2l [pp. 26, 27], the swirl shear a vanishes at X = 0, so nothing there can amplify pulses (our reading). The stress must vanish on a core solving the stress-free equations (4.13) [pp. 27, 33]. At the far end, zero exterior residual is not enough: the stress is an integral from the axis and can still carry tails like r^{-2} and r^{-1} [p. 30].

## The idea, motivated

**One clock for two lengths (M4.1).** Take radial length q^{1/2}, axial length q^D and tangential velocities q^{-A}, where A = 1/2 + h, D = 1/2 - h, and 0 < h < 1/100 is fixed [pp. 24, 32]; A + D = 1 keeps axial transport on the clock (our reading of [pp. 5, 26]). As z/τ^D would blow up at fixed z ≠ 0 (our reading), q is defined by τ = q(1 - η²), z = q^D η, keeping η in (-1, 1), with η = ±1 describing t = 1 away from the origin [pp. 7, 25]. Lemma 4.1 turns each time or axial derivative of q^b f(X, η) into a profile operator times an exact power of q [p. 25].

**Three profiles, one free function (M4.2, M4.3).** Write u_θ = q^{-A}E, u_z = q^{-A}U, r u_r = V0, p = q^{-2A}Π; since X = r²/(2q) is smooth in Cartesian coordinates, factoring √(2X) out of E and X out of V0 gives smoothness across the axis [p. 25]. Incompressibility fixes V0, and the leading radial equation is just pressure against centrifugal force, Π_X = E²/(2X); the rest of it, and axial viscosity, are smaller by q^{2h} and deferred to Section 5, whence its powers q^{2nh} [p. 26]. Free: E, U and the axis value of Π.

**Any residual is a stress, but a nonlocal one (M4.4).** Pulses supply stress divergences, so the tangential residuals must read -(∂_r + 2/r)T_θ and -(∂_r + 1/r)T_z [p. 9]. For an axisymmetric field this is free: multiply by r² or r and integrate from the axis [p. 27], with zero constants, since others blow up like X^{-2} or X^{-1} [p. 26]. The result is T = q^{-A-1/2}T0, T0 = F(p_s - s): p_s holds the integrated inviscid terms and the shear s = (a, -b_s) holds radial viscosity; zero stress means p_s = s, the pair (4.13) [p. 27]. The price is memory: T0 at X depends on the whole profile inside X.

**What the memory is (M4.5, M4.6).** This threatens any gluing, but Lemma 4.3 shows the memory is finite: beyond local values of U and E, p_s sees only the axis pressure and five cumulative integrals, axial momentum M, angular momentum I, axial transport of angular momentum J, axial momentum flux S and pressure increment Cp [pp. 28, 30]. By Lemma 4.4(i), profiles agreeing beyond X_h and sharing those five functions of η at X_h have the same pressure, radial velocity and stress beyond X_h [p. 29]. A join is five equations in η, after the axis pressure is fixed [pp. 28, 35].

**The exterior first (M4.10, M4.11).** The exterior must be residual-free with smooth limits at each fixed r > 0 as t → 1; the paper takes a pure swirl solving the radial heat equation exactly, E = c∞X^{-A}ℋ(2d/X) [pp. 6, 33], on our reading heat flow smoothing the power law similarity demands at large X. Normalizing the pressure to vanish at infinity fixes the axis datum Π0(η), so the exterior comes first [p. 35]. Against the tails of the third failed attempt, total moments vanish (4.28), so the stress integrates backward from infinity and is zero beyond X_b [pp. 30, 33, 36]. Four intervals, three pure power laws, are reserved for repairs [p. 35].

**Which stresses pulses can make (M4.7).** Two families supply T = c1v1 + c2v2 with c1, c2 > 0 and v1, v2 set by the local background [p. 10]. With P_c, J_c the products of p_s with (1, t_s) and (-t_s, 1), along and across the shear, t_s = -b_s/a, and v_s = a + b_s²/a, the admissible cone is v_s > 2, P_c > v_s and (v_s - 2)J_c² < 2(P_c - v_s)² [pp. 30, 31]. The middle inequality is T0·(1, t_s) > 0 [p. 32]: on our reading of the energy identity, pulses draw energy from the shear [p. 12]. The viscous waves need v_s > 2 [p. 31], positivity of the squared growth rate 2aF0²(1 - 2/v_s) [p. 74]. Our reading: with a = -rΩ'/Ω and b_s = W'/Ω (angular velocity Ω, angular momentum Γ = r²Ω, axial velocity W), v_s > 2 is Ω'Γ' + W'² > 0, the Leibovich and Stewartson combination, a cited precedent [p. 2], and without axial shear it is Rayleigh's condition that angular momentum decrease outward. By homogeneity in T0, the edges can carry the condition on T0/|T0| [p. 32].

**The core (M4.12).** Proposition 4.10 builds a stress-free, η-analytic flow near the axis from the offset data U* = 4η + j0, with an axis swirl shaped so that a regularized factor χ built from H* exceeds .99 wherever |Z*| is small [pp. 36, 37]; on our reading, this keeps one of the two amplification mechanisms active at every height [p. 5]. The core exits with v_s > 2 + c_ex, switches the stress on through a flat factor, and is continued until it equals the outer reference pair with all five integrals matched [pp. 37, 38]; Lemma 4.4(i) then joins it exactly [p. 40].

**The gap and the tempting fix.** After the join, the admissible cone holds near both edges but only the relaxed cone (P_c > 2 and v_s below a threshold U(P_c, J_c)) in between [pp. 31, 40]. Where the core meets the reference pair the swirl still rises like x^{1/10} and v_s < 1 [pp. 37, 38]; on our reading, angular momentum increases outward there. The tempting fix, steepening the shear, fails: the shear is a radial derivative, so a sustained order-one change across an interval moves E, U, the five integrals and p_s by order one, undoing the join (our reading).

**Oscillate instead (M4.13, M4.14).** The shear is made of radial derivatives, while Lemma 4.4(ii) bounds changes in p_s with no radial derivative of any difference [pp. 27, 29, 30]. So let the shear oscillate. Lemma 4.11 replaces it at each point by a periodic loop of shears, each admissible with p_s held fixed, averaging to the original shear; the relaxed cone, with admissibility near the ends, is its hypothesis [pp. 38, 39]. Our reading of the geometry: v > 2 is the outside of a disk in the shear plane, a nonconvex set; the loop runs on a circle of constant v above 2, and the original shear, inside it, is the loop's weighted barycenter. The loop is realized as E_N = E0 exp(𝒜(X, η, N log X)/N), U_N = U0 + ℬ(X, η, N log X)/N, with 𝒜, ℬ zero-mean primitives of the loop's deviation [p. 41]. The logarithm fits the operator X∂_X in which the shear is written: X∂_X(N log X) = N, so the modulation moves a and b_s by order one but values and integrals by O(1/N) [pp. 10, 27, 41]. Then p_s moves by O(1/N), inside the loop's strict margin, so the modulated profile is admissible at every point [p. 42], its stress oscillating in log X at frequency N.

**Pay back the integrals, then read off the edges (M4.9, M4.15, M4.8).** Bumps on the first power-law patch restore the five integrals exactly, since there the linear part of the moment map is a matrix of distinct-power integrals, invertible because a nonzero combination of m distinct powers has at most m - 1 positive zeros; a contraction handles the rest [pp. 34, 42]. The repair costs another O(1/N) in the shear quantities, and N is fixed last, after every radius, width and bump [pp. 40, 43]. The flat edge factorizations give a smooth unit direction up to X_a and X_b, a uniform margin κ, and a weight ζ built to vanish exactly as fast as the stress at both edges [p. 44]. Theorem 4.6 records all this, leaving two patches untouched for Sections 5 and 8 [pp. 32 to 34, 45].

## What breaks without each move

These counterfactuals are our reading unless a page is tagged.

- **M4.1** (q, Lemma 4.1): no exact powers, so no term is provably leading, and z ≠ 0 at t = 1 is an unbounded edge in η.
- **M4.2** (factors √(2X), X): the velocity is not smooth across the axis, so neither is the force for t < 1.
- **M4.3** (incompressibility, radial balance): a nonzero divergence or a leading radial residual survives outside the stress form, and the q^{2h} expansion is lost.
- **M4.4** (radial integration): no stress for pulses to target; nonzero axis constants make it singular [p. 26].
- **M4.5** (five integrals): matching means matching the whole interior profile, so no finite repair protects the exterior.
- **M4.6** (joining lemma): without (i), gluing alters the exterior pressure, radial velocity and stress; without (ii), the shear change leaves p_s uncontrolled.
- **M4.7** (admissible cone): Proposition 7.5 could need a negative squared amplitude; at v_s ≤ 2 the reference growth rate is not positive [p. 74].
- **M4.8** (Theorem 4.6): later constants would depend on q or the band, and edge amplitudes would go uncontrolled.
- **M4.9** (moment solve): the integrals cannot be restored, so repairs leak into the exterior; at λ = 0 two weights coincide [p. 42].
- **M4.10** (heat exterior): a residual or a missing limit at fixed r > 0 breaks the spatial cutoff [p. 6], and the axis pressure is unknown.
- **M4.11** (total moments): zero exterior residual still leaves r^{-2} and r^{-1} stress tails [p. 30].
- **M4.12** (offset core): without j0 both amplification mechanisms fail on one layer [p. 5]; without the core, nothing regular and stress-free matches the exterior.
- **M4.13** (prescribed mean): the primitives are not periodic, log E drifts by order one, and profiles, integrals and p_s all move.
- **M4.14** (frequency N): the loop stays a family of shears no profile has; at small N the O(1/N) errors exceed the margin.
- **M4.15** (repair, edges): the O(1/N) defect alters the exterior stress and heat tail; without Step 4, the edge direction, κ and ζ are missing.

## Three questions the section leaves open

1. **Is the modulation necessary, and is the relaxed cone its exact reach?** The loop is needed only because the joined profile fails the admissible cone on a stretch [pp. 38, 41]. Could a profile be admissible on the whole annulus? Is the relaxed cone exactly the set of barycenters of admissible shears at fixed p_s? It matters because the stress's radial derivatives grow like powers of N, and the answer decides which joined profiles are repairable.

2. **How small must h be?** The order of choices forces h < e^{-T_d}, T_d = e^{M_d} + 10 [p. 35]: doubly exponentially small in the exterior's axial-decrease parameter [p. 36]. Is that forced by the mechanism or by this exterior construction? It matters because h sets the anisotropy τ^h, the swirl Reynolds number τ^{-h} and the pulse scale separation q^{h/2} [pp. 4, 11]; a moderate explicit h would make the rate quantitative and numerically checkable.

3. **Does the core need analyticity in η?** The stress-free equations mix parameter and radial derivatives, with a regular singular point at the axis [p. 145], and the core and Section 5's recursion both use an analytic inner collar [pp. 33, 47]. Would a Gevrey or finite-regularity class do, and is the core locally unique given its axis data? It decides whether the leading flow is robust or finely tuned.

## Page tags

Pages cited, in order: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 69, 74, 145.

Extraction: displays on pp. 27, 31 and 40 to 42 were flattened; the fraction in (4.13) on p. 27 was read from context. No page was otherwise garbled.
