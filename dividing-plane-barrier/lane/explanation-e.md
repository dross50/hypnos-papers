# The Euler paper, explained: Finite Time Blowup for the Euler Equation (57 pages)

## The problem the paper faces

Beale, Kato and Majda showed that a smooth three-dimensional Euler solution continues past time T whenever the integral over [0, T] of the sup norm of the vorticity is finite, so any breakdown must make that integral diverge [p. 1]. A construction must drive the velocity gradient to infinity in finite time while solving the equation exactly.

The earlier constructions each leaned on a support. Elgindi's blowup on R^3 uses axisymmetric velocities without swirl in C^{1,α} for small α > 0, and Elgindi, Ghoul and Masmoudi proved its stability and gave finite-energy examples in the same class [p. 1]. The other whole-space results cited stay in C^{1,α}: smooth away from a point or a circle, or axisymmetric with α < 1/3 [pp. 1, 2]. Córdoba and Martínez-Zoroa reach C^{3,1/2} velocities before blowup, but for the forced equations, with a force bounded in C^{1,1/2-ε} ∩ L^2 [p. 2]. Chen and Hou have smooth data, but in an axially periodic cylinder with a wall, with a proof combining analysis and rigorous numerics [p. 2].

Theorem 1.1 asks for everything at once: a C^∞, divergence-free, compactly supported datum on R^3, no force, a finite lifespan, an unbounded gradient and a divergent vorticity integral [p. 1]. In plain terms, the singularity cannot be stored in rough data, fed in by a force, or held against a wall; smooth localized data must generate it unaided (our reading).

## What a person would try first, and why it fails

**One collapsing profile.** Several cited blowups are self-similar or nearly so, as their titles say [pp. 56, 57]. Among the cited results this route reaches smooth data only in a walled cylinder with rigorous numerics, and on R^3 it stops at C^{1,α} [pp. 1, 2]. The paper uses no self-similar profile; that one would stall at proving a smooth profile stable on R^3 is our reading, not the paper's claim.

**One packet on one shear.** A high-frequency disturbance on a smooth flow has a phase normal and amplitude obeying explicit transport equations, and some such disturbances have gradients growing along trajectories [pp. 2, 3]. But the paper's packet step returns an exact smooth solution on the whole interval [p. 13]: one gain is finite, and it is self-limiting, since growth slows once the phase normal has turned (Figure 2) [pp. 39, 40].

**Iterate, with exact waves or with a force.** The repair is repetition: let each packet's new gradient amplify the next. Exact waves on affine flows exist, but their iterated superpositions generally satisfy the equations along only one trajectory, so they cannot serve as the next background [p. 2]. Córdoba and Martínez-Zoroa iterate vorticity layers, each amplifying a more localized one, but with a force [pp. 2, 4]. Without the force, every future layer must already sit in the initial datum, riding passively through a flow whose gradient is enormous; a forward Gronwall bound would cost the exponential of that gradient over the waiting time (our reading of pp. 4, 35).

## The idea, motivated

*A fixed target.* Repetition needs one place where every stage deposits its gradient (our reading). The paper makes every flow odd, u(t,-x) = -u(t,x), so the origin is a stagnation point whose trajectory never moves [p. 4]. Each stage turns a parent U_{j-1} into an exact child U_j, which becomes the next parent; the goals are |∇U_j(t_j,0)| → ∞ with t_j increasing to T∞ < ∞, and initial changes summable in every H^m (ME.1) [p. 3].

*Particle coordinates.* A packet's phase stays fixed in particle labels [p. 3]. So let X(t,a) be the trajectory from label a, F = ∇_a X the deformation, and M, H the velocity gradient and pressure Hessian along it. Then det F = 1, F_t = MF and, from X_tt = -∇p, F_tt = -HF: the pressure Hessian is the acceleration of the deformation (ME.2) [p. 3].

*The packet.* Take the phase k m0·y in rescaled labels y = a/ℓ. Its physical gradient is (k/ℓ)m with m = F^{-T}m0, and the amplitude v, kept orthogonal to m by the pressure, obeys the ray system (2.4), which the paper traces to Lifschitz-Hameiri and Friedlander-Vishik [pp. 2, 3]. The added velocity is (ℓα/k)χ1 v f_δ(k m0·y), with χ1 a cutoff and f_δ a periodic profile whose derivative peaks at 1/δ. Differentiating the phase cancels the prefactor, so the gradient αχ1 v⊗m f_δ' does not depend on k, and at the center it is αv⊗m/δ (ME.3) [pp. 4, 5]. Size and gradient are decoupled. Making packets harmless by taking k huge is not quite right: the initial increment's H^m norm grows like αk^m ℓ^{-m} [p. 13]; the repair, later, is an exponentially small α.

*Amplification.* At the origin the parent gradient is B + hqp^T + E, with B the older flow's gradient, (p, q, n) a frame carried by it, and E small [p. 34]. The rank-one shear sends p to hq and kills the rest [p. 4]; it is nilpotent, so alone it gives no exponential growth (our reading). At the activation time t0 set a = B_pq(t0), β = B_nq(t0)/a, ε = (a/h*)^{1/2} with h* = h(t0), and τ = a(t - t0)/ε [p. 35]. Writing v = εUp + Vq + εWn [p. 38], with primes for τ-derivatives, the shear turns the p-part into the q-part (V' = -U), while B_pq, counted twice through the frame's rotation, turns the q-part back (U' = -2V) [pp. 38, 40]. The loop is hyperbolic: V grows at least like cosh(τ/√2) [p. 40], a physical rate of order (a h*)^{1/2} (our reading of p. 35). Meanwhile B_nq tilts the ray and the shear rotates the tilt into p, so the ray's p-component grows like x², with x = β^{1/2}τ (Figure 2) [p. 39]. Near x = 1 the pressure term begins to cancel the feedback (our reading of (4.20)), and by then V has gained exp(b0/√β) (ME.14, ME.15) [p. 40]. Since β x_prev² lies in [1/2, 2], with x_prev the previous stage's target value of x, the gain is exp(b x_prev) [pp. 35, 36].

*Transfer of the frame.* At the target, p2 = m/|m| and q2 = v/|v| frame a new shear with a2 ≈ a and β2 x_tar² ≈ 1 [p. 36], so the next stage faces the same problem with x_prev replaced by x_tar; with x_j = j²x_{j-1}, the gain grows every stage [pp. 46, 52]. The normalization α = δh_child/A_tar, with A_tar the central value of |m||v| at the target, deposits h_child q2 p2^T at the center and forces α ≤ P^c e^{-b x_prev}, where P collects the polynomial size bounds (ME.17) [pp. 7, 36]. The old shear also makes p2·Mp2 negative [p. 36], a sign the next activation needs [pp. 35, 53]. Comparing exact and ideal systems after dividing out the growth V0(t)/V0(s) makes errors cost powers, not exponentials (ME.16) [pp. 41, 42].

*Exactness.* Products of zero-mean oscillations can have nonzero mean [p. 4]. So treat the phase as an independent angle θ, whose average defines the mean, expand in κ = 1/k, and restrict to θ = k m0·y at the end [pp. 4, 12]. At each order a single unknown term, -(B_p·m)∂θA1, couples mean and oscillation, and it has zero angle mean; solving the mean first removes the circularity (ME.9) [p. 20]. The mean problem is nonlocal through the pressure, yet its initial value enters u0, which must be compactly supported [p. 5]; a displacement formulation with boundary operator L curl χNχ curl puts B(0) in a fixed ball and lets later mean fields stay nonlocal (ME.6) [pp. 14, 16]. The oscillatory problem is an ordinary differential equation at each label and angle, so it keeps support and zero mean; curl remainders make the sum exactly divergence free (ME.7) [pp. 16, 20].

Why all orders? The correction's energy estimate carries a factor up to exp(P^c), not polynomial in k, so a residual of size k^{-N} would not do (our reading of p. 28). Truncating at N_k = ⌊k^ϑ⌋, ϑ = 10^{-6}, leaves a residual at most exp(-0.7k^ϑ log k) (ME.10) [pp. 20, 23]. On R^3 × T the transport coefficient is small, while each derivative along the physical graph costs k [p. 24]; a Gevrey radius shrinking in time absorbs the lost derivative, and a correction with zero initial value makes the flow exact without changing the datum (ME.11) [pp. 24, 27, 28].

*The unforced difficulty.* Stages after the first activate at t_{j-1} > 0 [p. 48], but nothing can be injected then, so the packet must sit in the datum through a history interval [0, t0]. The paper prescribes its displacement η at t0, with η(0) = 0 and v = η_t - Mη [p. 4], taking the stationary path of ∫(|η_t|² - Hη·η)dt [p. 12]. Here F_tt = -HF pays: it yields the Euler-Lagrange equation, and by a Poincaré inequality the action is coercive once K+t0²/2 < 1, given H ≤ K+I; the size of M never enters, and negative eigenvalues of H only help (ME.5) [pp. 4, 16]. The paper credits this use of an upper bound on H to Brenier [p. 16]. The mean problem's coercivity rests on the same bound [p. 15]. The endpoint is picked through the symmetric, nonnegative endpoint map so that v starts in the growing sector (ME.13) [p. 37].

*Keeping H ≤ K+I at every stage.* A packet changes H by up to a constant times h_j h_{j-1} [p. 52]. The leading change is -2αχ1(m·Mv)(m⊗m/|m|²)f_δ' [p. 13], and m·Mv > 0 after a short initial time [p. 35], so the change is negative semidefinite where f_δ' ≥ 0. A symmetric profile would push both ways (our reading); instead f_δ is odd with f_δ'(0) = 1/δ and f_δ' ≥ -C (ME.4) [pp. 5, 11]. The wrong-sign part costs about δ_j h_j h_{j-1}, which is summable, and before the sign holds the exponential smallness of α pays [p. 50]. Summed, λ_max(H_j) ≤ K_B + 1 at every stage, K_B being the base flow's bound [p. 53].

*Gevrey-2.* Roughly k^ϑ linear solves, each losing derivatives, need one growth constant for all orders, with losses booked as integer shifts [p. 10]. Bounds of the form R^n(n!)² permit compactly supported cutoffs [p. 7], which analytic bounds forbid (our reading) (ME.8). The child's particle map keeps such bounds with growth constant polynomial in k [p. 13]; exponentiating a Lipschitz norm would lose this (ME.12) [p. 30].

*Scales.* Every scale has logarithm x_{j-1}/j^A, with A = 2 for frequency, 3 for profile concentration, 7/2 for localization and 5 for shear [p. 46], so k_j ≫ 1/δ_j ≫ 1/ℓ_j ≫ h_j (our reading). Constants are fixed in order, x0 last [p. 47], and no comparison needs an exponential of a power of P (ME.19) [p. 51]. An odd compactly supported base flow with a = 1, β = x0^{-2} and a seed packet at t0 = 0 start the induction (ME.18) [pp. 44, 51].

*The limit.* The early worry now resolves: each increment's H^m cost carries k_j^m, but α_j ≤ P^c e^{-b x_{j-1}} wins, because b x_{j-1} exceeds m x_{j-1}/j² once j is large [p. 54]. So U_j(0) converges in every H^m to a smooth, compactly supported, odd, divergence-free u0, and t_j increases to a finite T∞ [p. 54]. If its solution were smooth past T∞, H^3 stability would make it track U_j up to t_j, yet |∇U_j(t_j,0)| is at least h_j minus terms of order h_{j-1}, which tends to infinity (ME.20) [pp. 54, 55]. Both divergence statements then follow by a restart argument and a logarithmic Biot-Savart bound [pp. 55, 56].

## What breaks without each move

Each line is our reading of the counterfactual; a tag points to where the paper states the requirement.

- ME.1: no fixed target, and no exact solutions with converging data [p. 3].
- ME.2: the history and mean problems lose their action form, coercive under an upper bound on H [pp. 15, 16].
- ME.3: size and gradient stay tied, so small initial increments cannot make large shears [p. 4].
- ME.4: each packet raises λ_max(H) by about h_j h_{j-1}, and coercivity fails [pp. 3, 4].
- ME.5: a waiting packet is controlled only by Gronwall, at a cost exponential in the parent gradient.
- ME.6: the mean correction's initial velocity is nonlocal, so u0 is not compactly supported [p. 5].
- ME.7: corrections spread, lose zero mean, or outgrow the primary wave [p. 19].
- ME.8: constants compound over the k^ϑ solves, or compact cutoffs are lost [pp. 7, 10].
- ME.9: each order's equations stay coupled and cannot be solved in sequence [p. 20].
- ME.10: the residual is only polynomially small and cannot beat exp(P^c) [p. 28].
- ME.11: the solution stays approximate, and Euler without a force has nowhere to put the residual.
- ME.12: the next stage inherits bounds exponential in the new gradient [p. 30].
- ME.13: the activation velocity may start in the decaying direction [p. 35].
- ME.14: the huge shear leaves no scale-free model in which to prove growth [p. 38].
- ME.15: no gain exp(b x_prev), and no predictable next frame [p. 40].
- ME.16: coefficient errors grow by the same exponential, and the pressure sign is unproved [p. 41].
- ME.17: the child's gradient is not a shear the next stage can use [p. 5].
- ME.18: the induction has no first parent with a = 1 and small β [p. 51].
- ME.19: frequencies fail to dominate inherited losses, or costs and time steps stop being summable [p. 44].
- ME.20: growing solutions with different data never become one datum that breaks down [p. 54].

## What the Navier-Stokes paper kept and what it had to change

- What the texts show: NS pages 1 to 6 credit amplification across scales to Córdoba, Martínez-Zoroa and coauthors, give the amplified disturbances a different role, and do not name this manuscript [NS pp. 2, 3]; "kept" below means a shared mechanism, not a cited borrowing.
- Kept: amplification by background shear from a tiny seed. Euler's packet starts exponentially small and the shear loop brings it to size [pp. 36, 40]; in NS an exponentially small force seeds each pulse and the background shear supplies its growth [NS p. 6]. Both papers cite Lifschitz-Hameiri, Friedlander-Vishik and Craik-Criminale [p. 2; NS p. 2].
- Kept, with its role reversed: the averaged quadratic product of the oscillation. Euler cancels it at every order with the mean correction [pp. 4, 20]; in NS the pulses' mean momentum flux is the point, supplying the force a collapsing vortex lacks [NS p. 3], with two pulse families covering both stress components [NS p. 6].
- Kept: corrections to all orders. Euler cancels errors order by order and removes the rest exactly [pp. 20, 24]; NS corrects its base flow to every order, then cancels remaining singular terms [NS pp. 1, 6].
- Changed: what carries the blowup. Euler iterates shears at a fixed stagnation point, a gradient blowup from smooth data [pp. 1, 4]; NS builds a self-similar vortex with ℓ_r ≍ τ^{1/2} and ℓ_z ≍ τ^{1/2-h}, whose velocity becomes unbounded at bounded energy, starting from rest [NS pp. 1, 4].
- Changed by viscosity: in Euler a grown packet becomes the next parent's shear [pp. 5, 36]; in NS the shear shortens the radial wavelength until viscous damping overtakes amplification, so pulses grow and then decay [NS p. 6].
- Changed by the force: the residual. Euler must remove its residual exactly, with zero initial correction [p. 24]; NS defines the force as the residual and must make it smooth through the singular time [NS p. 3]. Euler's history problem and pressure-Hessian invariant, products of its unforced setting [p. 4], have no counterpart on NS pages 1 to 6 (our reading).

## Three questions the paper leaves open

1. **Where and when does the limiting solution actually break?** The proof gives T*(u0) ≤ T∞ by contradiction and allows the lifespan to end earlier [p. 55]; it neither locates the singularity nor gives a rate for the gradient. It matters because only then would the iteration describe the singularity rather than bound its time.

2. **How fragile is the datum?** Late increments enter u0 with H^m norms that decay super-exponentially in j [p. 54], so any fixed small perturbation dwarfs every packet past some stage (our reading). Do the sign conditions m·Mv > 0 and B_pp < 0, which hold with margins [pp. 35, 53], survive, perhaps with later packets retuned? It matters because it separates a robust mechanism from a finely tuned one, the question stability answered for Elgindi's C^{1,α} blowup [p. 1].

3. **What regularity does u0 really have?** Stage j adds an increment of size at most about e^{-b x_{j-1}}, oscillating at frequency about exp(x_{j-1}/j²) [pp. 46, 54]. If the size is not far smaller, our arithmetic gives decay faster than every power of the frequency N but slower than exp(-N^s) for each s > 0: u0 would be smooth yet in no Gevrey class, though every stage is analyzed in Gevrey-2 norms [p. 7]. Could a larger gain per stage, or a gentler frequency ladder within P^Q ≤ k^{ϑ/100} [p. 13], reach Gevrey data? It matters because it measures how far this mechanism sits from analytic data.

## Page tags

Euler: pp. 1, 2, 3, 4, 5, 7, 10, 11, 12, 13, 14, 15, 16, 19, 20, 23, 24, 27, 28, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57.
Navier-Stokes: pp. 1, 2, 3, 4, 6.

Extraction: figures (pages 6, 39) flatten to labels, and the notation tables (pages 8, 9) and page 56 garble some symbols; every formula used was recoverable.
