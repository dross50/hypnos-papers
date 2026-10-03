# Appendix B, explained: Analytic profiles near the axis and their continuation (pages 144 to 157)

## The problem this appendix is handed

The theorem needs fields smooth everywhere before blowup, with Cartesian estimates [pp. 1, 7]. The leading profiles, in X = r²/(2q) and η = z/q^D, are swirl E, axial velocity U, radial flux V0 and pressure Π [p. 7]. A field smooth in (r, z) can still be singular on the axis; Cartesian smoothness follows once E = √(2X)F and V0 = Xv0 with F, U, v0, Π smooth in X = (x1² + x2²)/(2q) [p. 25]. So the swirl vanishes linearly on the axis, and the true unknown is ϕ = CF [p. 25].

Pulses act only in the annulus Xa < X < Xb, so the leading stress, the tangential residual integrated from the axis, must vanish for X ≤ Xa [p. 9]. Hence the leading tangential equations hold exactly there: the identity (4.13), a radial equation each for ϕ and U [p. 27]. Their radial operators, X∂² + 2∂ and X∂² + ∂, have a regular singular point at the axis, and transport and pressure add η-derivatives [pp. 145, 147].

Section 4 needs [pp. 33, 36 to 37]: Cartesian regularity, ϕ > 0 and analyticity in η near the axis; (4.13) on [0, Xa]; a stress switching on flatly at Xa along the shear (a, −bs), with a > 0 and vs > 2 + cex; and a join to the outer profile with equal fields, axis pressure Π0 and five cumulative radial integrals, so Lemma 4.4 keeps the exterior [pp. 10, 28 to 29, 144].

## What a person would try first, and why it fails

**A power series in r.** A general series in r with η-dependent coefficients is not Cartesian-smooth; X and the factor √(2X) build in the parity [p. 25]. Our reading: the ∂η terms [p. 147] make each order differentiate earlier coefficients in η, so an iteration tracking finitely many η-derivatives loses one per step; the natural remedy is analyticity plus a norm in which radial degree pays for η-derivatives, the stated aim of the coefficient space [p. 145].

**Integrating inward from the exterior.** Our reading: the homogeneous radial operators have singular solutions, 1/X for swirl and log X for axial velocity, which inward marching generically hits; avoiding them means tuning two functions of η. The manuscript shows the analogous obstruction: nonzero integration constants would put X⁻² and X⁻¹ singularities into Qs, Ns [p. 26]. Also, pressure, radial velocity and stress at X depend on all smaller radii through cumulative integrals, so pasting values alone would change the exterior [p. 28].

**Keeping the reflection symmetry.** An odd axial velocity looks cleanest, but at the midplane it kills both axial transport of angular momentum and radial shear of axial velocity [p. 5]. Our reading sharpens this: a stress-free profile obeys DXa = XSq/L − (1 − a/2)a [pp. 26, 27, 149, 151]. At a = 2 the term −Wl, the order-one part of the angular source Sq, vanishes, leaving −Hc(log E)η − h(1 − 2ηU). Symmetry makes Hc = 0 at η = 0, so there Sq = −h < 0 whenever a = 2: a never reaches 2, bs = 0, and the edge inequality fails.

## The idea, motivated

**Solve outward, aiming at the edge.** Read forward, the singular point helps: axis values fix the regular solution. With Π0 imposed, the free data are the axis swirl ϕ∗ and axial velocity U∗, functions of η [p. 144]. The stress is T0 = F(ps − s), with ps = (p1, p2) the integrated inviscid terms and s = (a, −bs) the radial shear [p. 27]; stress-free means ps = s. The stress must be born along s, and the waves need vs = a + bs²/a > 2 [pp. 30 to 31, 33]; at a stress-free edge this is (B.19), p1 + p2²/p1 > 2 + cex [p. 149]. So every η needs large edge shear, rotational (a) or axial (bs).

**Break the symmetry just enough (MB.1).** Rotation needs the transport coefficient Hc, the axial route the axial source; their axis values are H∗ and Z∗ [pp. 26, 144, 148]. With U∗ = 4η, the outer value [p. 35], both vanish at η = 0 (our computation). U∗ = 4η + j0, with small j0 > 0, leaves H∗ one zero η0 < 0, of size comparable to j0, where Z∗ > 0 by the signs of Π0 [p. 144]. The indicator χ = H∗²/(H∗² + σ∗²) marks where rotation works; δ∗, σ∗ give every η either χ > .99 or |Z∗| > δ∗ [p. 144].

**Make transport win, then repair (MB.2).** By the barrier above, rotation lifts a past 2 only if −Hc(log E)η outweighs h(1 − 2ηU). The first guess, (log ϕ∗)η = −ΛL/H∗, makes it about ΛL but blows up at η0, and the profile must stay analytic (our reading). Replacing 1/H∗ by H∗/(H∗² + σ∗²) gives the holomorphic datum (B.3), with leading transport term exactly ΛLχ [pp. 145, 147], off only near η0, where the axial route takes over.

**Let the source set the scale (MB.4).** A source of size Λ against radial diffusion forces width about 1/Λ (our reading), hence Y = ΛX [p. 145]. There the leading problem is linear, with Λ⁻¹ remainders, solved by the alternating series Φ0 = f0(Yχ), in [.265, 1] on [0, 4.1], and u0 = −YZ∗/(2L) [pp. 146 to 148]. Our reading: in ρ = √(2Y) the angular equation is a four-dimensional radial Helmholtz equation, f0(Yχ) ∝ J1(kρ)/(kρ) with k² = χ, and a = −2YΦY/Φ exceeds 2, with Φ > 0, between the first zeros of J0 and J1; for χ > .99, Y = 4 lies there.

**Let radial degree pay for η-derivatives (MB.3, MB.5).** The remainders carry the η-derivatives that sank the naive series. The space Bρ weighs the β-th η-derivative of the degree-α coefficient with geometric, factorial and binomial factors [p. 145]. Trading a radial degree for an η-derivative costs a factor of order the degree, which each radial inversion divides out; the space is an algebra, and even mixed products of η- and logarithmic radial derivatives are bounded after inversion [pp. 145 to 147]. The order-one term χΦ is not small, but each inversion raises the lowest degree, so its iterates decay factorially and a geometric series inverts it [p. 148]. (Our reading: a Cauchy-Kovalevskaya majorant norm with Volterra-type inversion.) A contraction yields a real analytic stress-free profile within O(1/Λ) of the explicit one; since ϕ∗ may be exponentially large in Λ, the pressure coupling needs C ≥ sup|ϕ∗| on the complex domain [pp. 147 to 148].

**The edge inequality, two branches (MB.6).** Where χ > .99 the explicit profile gives p1 = a > 2.3 at Y = 4; elsewhere |Z∗| > δ∗, so p2 grows linearly in C while p1 stays bounded, and large C, meaning weak swirl (our reading), gives p2²/p1 > 2.3 [pp. 149 to 150]. Either way (B.19) holds with cex = .2 [p. 150].

**Switch the stress on by lowering the shear (MB.7, MB.8).** The analytic solution stops at Y = 4.1, yet the profile must reach radius of order C¹⁰ [pp. 146, 155]. A reference continuation cuts the logarithmic slopes to zero and freezes the fields, so nothing grows with length: p1 and ns stay bounded uniformly in C, and the left side of (B.19) above 2 + c [pp. 150 to 151]. The key: ps uses only profile values and cumulative integrals [pp. 28 to 29], while s is built from radial derivatives [p. 27]. Scaling the shear by κ = 1 − ea, ea a flat step at X0 = 4/Λ, moves ps only by O(y·ea), y = log(X/X0) [p. 152]. So T0 ≈ F·ea·ps,r (r for reference): born flat along the old shear, and exactly T0 = ea·B0 with B0 ≠ 0 [pp. 152 to 153].

**Hold the weakest condition, steer, quarantine (MB.9, MB.10).** With κ = κ0 small, vs < 1, so the relaxed cone of the joining reduces to Pc > 2, where Pc is ps along the shear [pp. 30 to 32, 153]. The axial shear is switched off and a steered to .8, the value of 2 − 2l on the outer law E ∝ X^(1/10), with a barrier keeping p1 > 2 [pp. 27, 35, 153]. A collar beside Xa is then closed to later edits, which forward integrals cannot carry back [p. 153].

**Join through five numbers (MB.11 to MB.14).** Over a logarithmic length Tsh bounded before C is chosen, E takes the outer η-shape f = (1 + η²)⁻¹ and the law C⁻¹f(X/Xi)^(1/10), Xi = 110 [pp. 150, 154]. That is the outer profile P∗f(X/XR)^(1/10) once XR = Xi(CP∗)¹⁰, so raising C pushes the matching radius out while the inner structure, fixed in X, shrinks to [0, xsep] with xsep ∝ C⁻¹⁰ in outer units [pp. 155 to 156]. Normalized, the moment formulas lose XR, so one tolerance serves all large XR, and inner contributions vanish as powers of xsep and 1/C [pp. 155 to 156]. After U is restored to 4η, two bumps in U and three in E cancel the five discrepancies; the linearization splits into blocks of distinct powers, invertible by a Rolle argument, and the quadratic remainder yields to contraction [pp. 34, 156 to 157]. Lemma 4.4 carries equality outward; the order (B.40) makes each choice depend only on earlier ones [p. 157].

## What breaks without each move

- MB.1 (offset j0): at η = 0 neither mechanism acts, so (B.19) fails.
- MB.2 (steep datum): nothing forces the shear a past 2; the unregularized datum is singular at η0.
- MB.3 (space Bρ): each iteration loses an η-derivative; the fixed point never closes.
- MB.4 (profile f0): Φ > 0, needed to divide by ϕ, is unproved; the edge shear is unknown.
- MB.5 (contraction): Theorem 4.6(i) and (ii) lack an axis-regular, stress-free inner region.
- MB.6 (two branches): for some η the stress could be born with vs ≤ 2, outside the cone.
- MB.7 (reference): past Y = 4.1 the cone quantities lack bounds uniform in length or C.
- MB.8 (activation): the stress could start non-flatly or off-cone, or disturb integrals the exterior reads.
- MB.9 (barrier): Pc > 2 could fail on the connection, missing the power-law state.
- MB.10 (quarantine): later edits could destroy the η-analyticity used by Theorem 4.6(i) and Lemma 5.1 [pp. 33, 47].
- MB.11 (early Tsh): raising C could lengthen the transition, undoing its own gain.
- MB.12 (XR scaling): inner moment contributions need not shrink in outer units.
- MB.13 (five bumps): outer pressure, radial velocity and stress would change, losing the heat exterior.
- MB.14 (ordering): some smallness condition could refer to a quantity not yet fixed.

## Three questions the appendix leaves open

1. **How large must Λ, C and XR be?** The proof takes C ≥ sup|ϕ∗| on a complex domain, possibly exponential in Λ, and XR = Xi(CP∗)¹⁰ [pp. 147 to 148, 155]. Effective sizes decide whether the profile can be computed, and which features the mechanism itself forces.

2. **Is analyticity in η essential?** Each radial order costs an η-derivative, and Corollary B.6 carries analyticity forward [pp. 145, 153]; whether Gevrey data suffice measures the inner profile's robustness.

3. **Is the midplane bias forced?** Our reading gives a < 2 on the midplane for symmetric stress-free profiles at leading order; could higher-order terms or an inner stress evade this? The answer decides whether flow through the midplane is intrinsic [pp. 5, 144].

## Page tags

pp. 1, 5, 7, 9, 10, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 47, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157.

Extraction: pp. 27 and 145 to 150 flatten fractions and exponents; all were recoverable.
