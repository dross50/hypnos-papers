# Section 8, explained: Compactly supported mean corrections (pages 88 to 100)

## The problem this section is handed

Sections 4 and 5 built an axisymmetric background whose residual is minus the cylindrical divergence of a stress confined to the annulus X_a ≤ X ≤ X_b, plus a flat error (every derivative smaller than any power of q) [p. 11, p. 60]. Section 6 gave the waves a torus variable Y, evaluated along the phase map Y = v_r r^{d_r} + v_t t, so overlapping waves get disjoint torus supports and vary fast in time at mild radial cost [p. 12, p. 62, p. 63]. Section 7 built pulses whose averaged quadratic flux supplies the leading stress, and an inverse for every nonzero angular harmonic [p. 88].

What remains is the angular mean of the residual. Waves average to zero around the axis but their products need not, so the mean contains quadratic wave products and can vary on the torus [p. 6, p. 88]. It must be removed with pressure, stresses, and divergence-free velocity, all vanishing outside the active annulus [p. 88]. Torus-dependent fields are kept off the axis, where r^{d_r} is not smooth [p. 64], and the inner growth must survive [p. 100]. Farther out, the flow is an exact heat solution with zero residual and a pressure normalized from infinity, used by the final localization [p. 15, p. 16].

Section 9 needs fixed linear maps to reapply after every wave update (pressure reconstruction, realizable stress targets, an inverse for the torus-oscillating part, a finite correction of leftover scalar defects), two velocity moments held exactly at zero, and a fixed gain per cycle [p. 14, p. 106, p. 111].

## What a person would try first, and why it fails

**Integrate outward from the axis.** After averaging, the radial equation reads D_r p_m = g_r, so the obvious pressure is p_m(R) = ∫_0^R g_r dR′. It vanishes below the shell, but beyond it equals the full integral, which is generally nonzero [p. 89, p. 92]; a constant offset there conflicts with the exterior pressure normalization [p. 15] (our reading). The stresses fail the same way: the Section 3.2 formulas vanish beyond the annulus only when R^2- and R-weighted residual integrals vanish [p. 9]. Integrating inward from outside just moves the leftover constant to the axis (our reading).

**Integrate at a frozen torus point.** The physical radial derivative of a torus-dependent field also moves Y: it is ∂_r plus d_r r^{d_r - 1} times the derivative along v_r [p. 63]. A primitive with Y held fixed does not invert the operator that appears; the paper notes the integrals must follow the torus path [p. 89].

**Give the whole mean to one mechanism.** Stress targets fail because Proposition 7.6 accepts only stresses independent of the auxiliary variable [p. 84]. A velocity whose fast time derivative matches the mean fails on the torus average, which no torus derivative produces. The manuscript names these two inversion problems [p. 88].

## The idea, motivated

**Why the angular mean, and in what form.** Section 7 handles every nonzero harmonic, leaving harmonic zero. Split the velocity into slow base (b, V, G), an angularly invariant correction (β, v, γ) that may depend on Y, and waves w with zero angular mean (M8.1) [p. 88]. Averaging kills products with one wave factor, so waves survive only through their angular covariance W_ab, curl remainders included [p. 88, p. 89]. Proposition 8.1 writes the averaged equations in divergence form, a pressure equation D_r p_m = g_r plus tangential residuals E_θ, E_z (M8.2), so that weighted radial integrals become boundary terms [p. 88, p. 89].

**The one fact behind compact support.** For e = 0, 1, 2 the product rule gives R^e(∂_R + e/R)φ = ∂_R(R^e φ). So (∂_R + e/R)φ = f has a solution vanishing near the axis and beyond the shell exactly when ∫R^e f dR = 0 [p. 88, p. 90]. Here e = 0 serves pressure, e = 1 the vector potential and axial momentum, e = 2 angular momentum, whose flux carries an extra frame term [p. 89, p. 92]. In our reading, the rest is bookkeeping of where these integrals go.

**Repairing the naive primitive.** Subtract a fixed cutoff χ_m (zero on an inner collar, one on an outer collar) times the full integral: I_c = I - χ_m J, which vanishes below X_a and above X_b (M8.3) [p. 89, p. 90]. The price is exact: the weighted inverse T_e obeys D_e T_e f = f - A_e f, with a cutoff remainder where χ_m varies (8.7), identically zero when f is torus independent with zero weighted integral [p. 90]. For the torus drag, the integrals shift Y by ((r′)^{d_r} - r^{d_r})v_r (8.4) [p. 90]: on the phase map this is plain integration of the physical function (our reading), and as an extended field its fixed-shift form keeps the large factor M out of coefficient derivatives [p. 91].

**Why the torus remainder is harmless.** Now J is a function on the torus. Its torus average is the integral of the averaged source, which a zero weighted mean removes [p. 91]. The rest oscillates along the path; an exact identity trades p integrations by parts for p factors of M^{-1} ≤ Cε^{κ_s}, up to logarithmic factors [p. 91, p. 92]. The small divisors obey |v_r·k| ≥ c/(1 + |k|), because v_r·k times its algebraic conjugate is a nonzero integer (6.7) [p. 64], so p inversions cost p + 3 torus derivatives (8.10) [p. 91]. Large p makes the remainder smaller than any power of q at each fixed derivative order, not uniformly in p (M8.4) [p. 92]. Flat errors are simply carried [p. 105].

**Pressure: move the obstruction onto a bump.** A compactly supported pressure has a derivative with zero radial integral, so it cannot balance a source with nonzero integral. Name that integral P = ∫⟨g_r⟩_Y dR, the first radial integral defect, subtract P times a fixed unit-mass bump ρ in a reserved interior patch, and invert the rest: p_m = T_0(g_r - ρP) (8.12) [p. 92, p. 93]. The obstruction now sits as -ρP in the radial equation (M8.5) [p. 93], in every later state too [p. 106].

**Axial velocity: a potential, and the moment it forces.** Later steps prescribe axial mean velocity, and incompressibility demands a radial partner. An azimuthal vector potential supplies both exactly: Ψ = T_1 γ_d, Δβ = -ε∂_Z Ψ, Δγ = (D_r + 1/R)Ψ = γ_d - A_1 γ_d (M8.6) [p. 93]. The hypothesis ∫R⟨γ_d⟩_Y dR = 0, zero net axial flux, makes Δγ equal γ_d up to a flat remainder, exactly if γ_d is torus independent [p. 93], so realizable axial increments respect M_z = 0 of (8.2) [p. 88, p. 89]. That is natural: averaging the divergence condition shows this flux cannot change with height (our reading). The radial partner gains a factor ε = Q^h, the radial-to-axial length ratio [p. 8, p. 93].

**Integrating the tangential equations.** A compactly supported stress can represent ⟨E_θ⟩_Y and ⟨E_z⟩_Y only if their R^2- and R-weighted integrals vanish [p. 93]. Radial fluxes, W and the base stress included, integrate to boundary terms; radial viscosity drops out after two integrations by parts [p. 94]. Torus averaging turns t_* into -ε∂_T, so the time derivative and axial viscosity become derivatives of ∫R^2⟨v⟩_Y and ∫R⟨γ⟩_Y [p. 94]. These are linear in the correction and not fluxes (our reading), so both moments are held at zero at every (Z, T) [p. 88, p. 93]. Only axial fluxes survive, each carrying D_z = ε∂_Z [p. 17]. They define the flux defects J_θ and J_z, with the pressure moment folded into J_z by one integration by parts: ∫R^2⟨E_θ⟩_Y dR = ε∂_Z J_θ and ∫R⟨E_z⟩_Y dR = ε∂_Z(J_z + c_ρ P) (M8.7) [p. 94]. The obstruction is now three scalar functions of (Z, T), the tangential ones entering only through ε∂_Z, a free order of smallness that Section 9 spends in (9.12) [p. 108].

**Stress targets.** Subtract σ_θ ε∂_Z J_θ and σ_z ε∂_Z(J_z + c_ρP), with bumps of unit weighted mass; the sources are then torus independent with zero weighted integrals, so T_2 and T_1 invert them exactly into shell-supported targets H_θ, H_z (M8.8) [p. 94, p. 95]. A wave covariance change equal to these targets, entering through W_rθ and W_rz, removes the averaged residual up to the bump terms [p. 94, p. 95].

**The torus-oscillating part: the fast-time inverse.** For E° = E - ⟨E⟩_Y, split t_* = -ε∂_T + cN with N = v_t·∂_y: the fast coefficient c is only logarithmically small, while the slow term carries a full ε [p. 63, p. 95]. Set Δv = -c^{-1}N^{-1}E°_θ and γ_d = -c^{-1}N^{-1}E°_z (M8.9) [p. 96]. N^{-1}, a Fourier multiplier on nonzero torus modes, loses four torus derivatives under the same Diophantine bound (8.19) [p. 95, p. 96]. The outputs have zero torus mean everywhere, so both moments are preserved for free; N commutes with the shifted primitives, so the potential's remainder stays flat; what remains is the slow derivative, one ε smaller [p. 96]. The two velocity mechanisms do not interfere linearly: zero-mean fast-time increments cannot move the averaged defects, and the torus-independent moment increments below create no fast-time term (our reading) [p. 107, p. 111].

**The three defects: count, then choose where.** Removing P, J_θ, J_z while keeping both moments at zero is five linear conditions, hence five coefficients: three swirl bumps and two axial bumps (8.25) [p. 96, p. 97]. A swirl increment moves P through the centrifugal term 2VΔv/R and J_z through the pressure moment [p. 97, p. 99]; an axial increment moves J_θ by carrying base angular momentum RV vertically [p. 3] (our reading). The simplest swirl, a free vortex with RV constant, fails: the J_θ row becomes a multiple of the zero-flux row, so zero-flux axial increments cannot move J_θ (our reading). The paper instead uses an interval I_mean, reserved in Section 4 for this lemma, with U = 0 and a power-law swirl of exponent λ > 0, kept exact by the background (M8.10) [p. 33, p. 34, p. 60, p. 97]. With G = 0 there, the equations split into a swirl block with power moments x^2, x^{-2-2λ}, x^{-2λ} and an axial block with x^1, x^{1-2λ}; geometric copies of one bump make each block Vandermonde, invertible because the exponents are distinct for λ > 0 (M8.11) [p. 97, p. 98]. The inverse is fixed once, may degrade as λ shrinks, and is reused at every stage [p. 98, p. 106].

**The gain, and the order of operations.** Applied to the current defects, the map removes their linear parts exactly; what is left is quadratic or carries an extra ε, a gain of ε^{0.9-2κ_s} whose weakest link is the product 2vΔv/R of new and accumulated swirl (M8.12) [p. 98, p. 99]. Recomputation uses the actual increment, remainder included, since a zero-mean remainder times another field can acquire a torus mean (M8.13) [p. 99, p. 100].

## What breaks without each move

These counterfactuals are our reading except where tagged.

- M8.1 (moments): weighted tangential integrals keep time-derivative and axial-viscosity terms, and axial increments lose their flat realization.
- M8.2 (divergence form): radial fluxes, W included, stop integrating to boundary terms, hiding the defects.
- M8.3 (cutoff primitive): primitives leak past the shell (a constant for pressure, an R^{-e} tail otherwise), and without the torus shift they miss the physical radial derivative [p. 89].
- M8.4 (flat remainder): torus-dependent sources, such as fast-time axial increments, leave a non-flat error where χ_m varies.
- M8.5 (pressure bump): the pressure leaks past the shell and shifts the exterior normalization.
- M8.6 (axial potential): a prescribed axial increment has no exactly divergence-free partner inside the shell.
- M8.7 (integrated identities): no finite list of obstructions, and no free ε∂_Z for (9.12).
- M8.8 (covariance targets): Proposition 7.6 cannot turn the averaged residual into amplitude changes [p. 84].
- M8.9 (fast-time inverse): the zero-torus-mean residual has no corrector, as stress targets must be torus independent.
- M8.10 (reserved patch): no explicit block structure, and at λ = 0 the axial block is singular.
- M8.11 (five-equation map): P, J_θ, J_z persist, leaving -ρP and both bump terms.
- M8.12 (exact update): no proof that reapplying the map raises the defect order; Step 4 of the cycle stays open [p. 111].
- M8.13 (recomputation order): corrections act on stale residuals and drop products, including remainders that acquire torus means [p. 99].

## Three questions the section leaves open

1. **Is the exact power law on I_mean essential?** With G = 0, the five functionals are independent on bumps in a patch whenever R^2, V/R and RV are linearly independent there and RV is not constant (our reading). Does exactness buy more than an explicit inverse, uniform in (Z, T) and band? It matters because Sections 4 and 5 must preserve the patch [p. 34, p. 60] and the axial inverse degrades as λ shrinks [p. 98]; the ledger's numerical check finds its condition number growing like 1/λ.

2. **How flat is the cutoff remainder, quantitatively?** Flatness of order N needs p integrations by parts with h(α + pκ_s) > N + L and κ_s = 10^{-5}, and nothing uniform in p is asserted [p. 92, p. 100]. It matters because this is the section's one estimate whose smallness comes from oscillation and small divisors rather than exact algebra (our reading), with near-resonant torus modes paid for by derivatives [p. 92]. A bound explicit in p, say of Gevrey type, would show whether the mechanism supports a force in a class smaller than C^∞.

3. **Are these five scalars canonical?** The moments and defects read like momentum budgets of a flow confined to a shell: angular momentum and net axial mass flux, the pressure drop the radial balance demands, and vertical fluxes of angular and axial momentum through a horizontal slice (our reading). Are they the complete set of obstructions to compactly supported axisymmetric mean corrections, whatever the order of operations? It matters because, if so, any annulus-confined scheme sustaining the collapsing vortex carries these five constraints and the free ε∂_Z is structural; if not, a leaner scheme may exist.

## Page tags

pp. 3, 6, 8, 9, 11, 12, 14, 15, 16, 17, 33, 34, 60, 62, 63, 64, 84, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 105, 106, 107, 108, 111.

Extraction note: pages 63, 90, 91 and 93 are mildly garbled: superscripts are flattened, and the special radial operator (radial derivative plus phase chain rule) prints as a plain r, so (r + 1/r)Ψ on page 93 is ambiguous. We used the ledger's notation.
