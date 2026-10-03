# Section 10, explained: Compact forcing and whole-space breakdown (pages 116 to 126)

## The problem this section is handed

Section 9 ends with local fields `u_loc, p_loc` [p. 114], defined only on `Ω∗ = {τ > 0, q < q∗}`, where `τ = 1 − t` and q is the concentration scale [p. 7, p. 15]. Theorem 3.1 gives them four properties [pp. 15 to 16]: a representation `u_loc = curl A + B e_θ`, smooth at the axis; derivative bounds up to τ = 0 where q stays between positive constants below q∗; a residual that is flat (every derivative `O(q^N)` at bounded X as q ↓ 0) and exactly zero for `X ≥ X_ext`, where A = 0 and the flow is an explicit heat swirl `K e_θ`; and swirl growth `τ^{−A}` (exponent `A = 1/2 + h`, not the potential) along one path.

Theorem 1.1 needs five things these fields lack [p. 1]: compact support for velocity and pressure; zero initial velocity; a force in `C_c^∞(R³ × (0, ∞))`, smooth through t = 1 and beyond; a uniform energy bound; and a comparison showing that no global smooth solution with the same force and datum has bounded energy. Their domain stops at `τ < q∗` (our reading, since `τ ≤ q`), their residual exists only for t < 1, and one construction says nothing about competitors. Section 10 supplies all five [p. 117].

## What a person would try first, and why it fails

**Cut the velocity.** Multiply `u_loc` and `p_loc` by a bump equal to one near (0, 1). The divergence becomes `∇χ · u_loc`, nonzero where the bump varies; projecting back onto divergence-free fields is nonlocal and loses compact support (our reading). The paper signals this by requiring the cutoff to act before a curl [p. 16, p. 117].

**Trust flatness at t = 1.** Take the residual as the force and rely on (3.4). But flatness holds at bounded X as q ↓ 0, near the singular point, while the cutoff creates terms such as `p_loc ∇c` in a transition region that reaches the terminal slice [p. 16]. The bounds available there depend on a positive lower bound for q [p. 119], and the paper names where that fails: positive radius with q → 0, on the plane z = 0 [p. 16, p. 119].

**Compare by the global energy identity.** To get nonexistence, show that any smooth competitor v with the same data equals u, via the energy identity for `w = v − u`. On R³ that needs decay of v, its derivatives and its pressure at infinity, and the paper assumes none [p. 121]. Some condition at infinity is unavoidable: with zero force and datum, a uniform velocity `a(t)`, `a(0) = 0`, driven by the pressure `−a′(t) · x`, is a smooth nonzero solution (our reading).

## The idea, motivated

**Cut the potential.** The construction already carries `u_loc = curl A + B e_θ` [p. 116], so cut the potentials: `u = curl(cA) + cB e_θ`, `p = c p_loc` (10.4). Both pieces are divergence-free, the second because cB is independent of θ, which is why the spatial cutoff is axisymmetric [p. 118] (M10.2). The product rule `u = c u_loc + ∇c × A` shows the price, an extra term wherever c varies [p. 118].

**Which potential.** So A must be controlled wherever c varies, including the axis and, as will emerge, the plane z = 0 near t = 1. The section checks two properties of its representative (9.21) [p. 115, p. 117] (M10.1). Near the axis the base streamfunction is `S = r² a(r², z, t)`, so `(S/r) e_θ = a(−x₂, x₁, 0)` is smooth in Cartesian coordinates. And A = 0 for `X ≥ X_ext`: each streamfunction integrates an axial profile `U_n` outward from the axis (10.1) and returns to zero past its support because the total axial flux `∫_0^∞ U_n dX` vanishes, a condition imposed in Sections 4 and 5 [p. 33, p. 49, p. 117]; wave and mean potentials vanish with their sources [p. 117]. Only the swirl B = K survives in the exterior [p. 116].

**Where to cut.** Ω∗ is described through q, defined by `τ = q(1 − η²)`, `z = q^D η`, `X = r²/(2q)` [p. 7]. So q depends on (z, t) only, Ω∗ contains every radius, and the cutoff's radius `r_0` is free [p. 118]. It remains to bound q by τ and |z| alone: if `1 − η² ≥ 1/2` then `q ≤ 2τ`, and otherwise `q ≤ (√2|z|)^{1/D}`, so `q ≤ C_0(τ + |z|^{1/D})` uniformly in r (10.3) [p. 118]. Only now is the cutoff defined: `c = χ_x χ_t`, an axisymmetric spatial bump of radius `r_0` and half-height `z_0` times a time bump switched on after `1 − τ_0`, with `τ_0, z_0` so small that c lives in `q < q∗/2`, a fixed margin inside Ω∗; the time bump gives the zero datum (10.2) [p. 118]. The force is the residual, `f = R(u, p)` (10.5), so the equation holds by construction; the paper notes that f need not be divergence-free [p. 118], the price of cutting the pressure locally (our reading).

**Where the force could fail at t = 1.** Repair the second attempt: where does q vanish at τ = 0? If z ≠ 0, then `q ≥ |z|^{1/D} > 0`, Theorem 3.1(ii) bounds one more time derivative, and the fundamental theorem of calculus makes every derivative uniformly Cauchy [p. 119] (M10.3). If z = 0, then η = 0 and q = τ [p. 116]: q → 0 on the whole plane, not only at the origin. At fixed r > 0, `X = r²/(2τ)` then tends to infinity, so the point enters the heat exterior, where A = 0 and the flow is explicit, `K = c∞ s^{−A} H(2τ/s)` with `s = r²/2` (10.7); derivatives of K and of its centrifugal pressure stay bounded down to τ = 0 (10.8) [p. 119, p. 138]. The uncut exterior solves the equations exactly, so only cutoff terms built from K and `p_loc` survive there, and they have limits [p. 119], a use the physical description announced [p. 6].

At the origin the individual terms diverge, but c = 1, so f is the local residual and (3.4) with (10.3) bounds every derivative by `C(τ + |z|^{1/D})^N` (10.9) [p. 119] (M10.4). A small ball, a late time and a finite cover then give uniform limits `F_j` of `∂_t^j f`: smooth, supported in K, flat at the origin (10.6), and compatible (10.10), hence one-sided time Taylor data at t = 1 [pp. 118 to 120].

**Past t = 1.** Extension by zero would in general jump, and the Taylor series `Σ σ^j F_j/j!` may diverge (our reading). The repair damps term j by `χ_0(b_j σ)`, `σ = t − 1` (10.11) (M10.5): on its support `σ ≤ 1/b_j`, so each derivative costs a factor `b_j` and the term is `O(b_j^{m−j})` (10.12); fast-growing `b_j` make it at most `2^{−j}` in all norms of order up to `⌊j/2⌋`. Every derivative then converges, the Taylor data are reproduced, and the support is `K × [0, 2]` [p. 120]. This is the classical Borel construction, unnamed in the paper; past t = 1 the force is one continuation among many (our reading).

**Energy from the equation.** The heuristic `E_core ≍ τ^{1/2−3h}` covers only the leading core [p. 16]; the paper reads the bound off the equation instead [p. 17] (M10.6). Compact support makes the energy identity (10.14) exact, and it bounds energy plus dissipation by `F(t)²`, `F(t) = ∫_0^t ‖f‖_2`, finite since f is smooth (10.13) [p. 121].

**From construction to nonexistence.** Repair the third attempt. The paper assumes only `v ∈ L^∞([0, T]; L²)`, T < 1 [p. 121], and spends it first on the pressure (M10.7). The force cancels in the difference equation (10.15), and the natural pressure is `π∗ = Σ R_i R_j g_ij` (Riesz transforms, `g = v ⊗ v − u ⊗ u`) (10.16) [p. 121]. The actual pressure difference π has the same Laplacian; averaged in time, `∇π − ∇π∗` lies in `H^{−3}`, because w ∈ L² and g ∈ L¹, and a harmonic element of `H^{−3}` vanishes, its Fourier transform being supported at the origin [p. 122]. The uniform flow fails here: its pressure gradient is a Fourier point mass, its energy infinite (our reading).

Boundary terms are handled on expanding balls (M10.8, M10.9). Pairing (10.15) with `χ_R w`, `χ_R = φ(x/R)^8`, leaves flux terms on an annulus where w = v for large R [p. 123]. The transport flux is bounded by powers of `‖φ_R^4 w‖_6`, which Sobolev controls by local dissipation (10.17) [pp. 122 to 123]. The pressure flux is nonlocal, so the cutoff is commuted through `R_i R_j` (10.18): the local part is bounded in `L^{3/2}`, and the commutator kernel gains `min{|x − y|/R, 1}`, so its contribution decays like `R^{−3/4}` (10.19) [pp. 122 to 123]. Every resulting power of the local dissipation is below 2, so Young's inequality absorbs the fluxes, leaving the stretching term `‖∇u‖_∞ E_R` plus `C_T/R`; Gronwall from `E_R(0) = 0` gives `E_R ≤ C′_T/R`, and R → ∞ gives v = u on [0, T] [p. 123]. T < 1 matters: with fixed compact support and unbounded sup norm, the gradient is unbounded (our reading).

Finally (M10.10), the points `x_τ = (√(2X_in τ), 0, 0)` sit at the similarity point `(X_in, 0)` and tend to the origin, where c = 1, so (3.6) gives `u_θ = τ^{−A}(e_0 + O(τ^{2h}))` along them (10.21) [p. 116, p. 124]. A global smooth bounded-energy v equals u on every [0, T], hence on [0, 1), and cannot be bounded near (0, 1) [p. 124].

**Every viscosity, and the torus.** Rescaling space by √ν gives every viscosity at the same singular time (10.22) [p. 124] (M10.11). For T³, a parabolic dilation with a time shift puts the support inside the open unit cube at the same singular time; integer translates then have disjoint supports with a gap and never interact, and the pressure is periodic, as the erratum to Fefferman's statement requires [p. 125] (M10.12). Periodic uniqueness is simpler: integration over T³ removes the transport and pressure terms [p. 126].

## Exactly what is claimed, and in which class

- **Constructed at viscosity one:** u, p smooth on `R³ × [0, 1)`, divergence-free, supported in K, zero for `t ≤ 1 − τ_0` [p. 118]; energy and dissipation at most `F(1)²` [p. 121]; growth (10.21) [p. 124]. The force is smooth with support in `K × [0, 2]` [p. 120], is the residual for t < 1, is not claimed divergence-free [p. 118], is nonzero, and depends on ν [p. 124].
- **Breakdown class:** excluded are smooth solutions on `R³ × [0, ∞)` with this force, zero datum and uniformly bounded kinetic energy [p. 1, p. 124], with no condition on P or on derivatives of v at infinity [p. 121].
- **Lemma 10.5's hypotheses:** viscosity one, fixed T < 1, the force of Lemma 10.3, zero initial velocity, v smooth on `R³ × [0, T]` and in `L^∞([0, T]; L²)` [p. 121]; general ν follows by inverse rescaling [p. 124]. Nothing is asserted at or after t = 1. The proof uses only an energy bound on each [0, T], less than the stated uniform bound (our reading).
- **Lifespan and growth:** the maximal classical interval [0, 1) is asserted in the `H³` class [p. 124]. Growth is a lower bound along `x_τ`; no upper bound on `‖u(t)‖_∞` is given (our reading).
- **Corollary 10.6:** no global smooth periodic solution with the same datum and force; the force is compactly supported in time and the pressure periodic [pp. 125 to 126]. No energy hypothesis is stated; on compact T³, smoothness gives finite energy anyway (our reading).
- **Scope:** the paper presents these as alternatives (C) and (D) of Fefferman's statement [p. 1, p. 125]. Section 10 assumes Theorem 3.1 and does not address the unforced equations, weak continuations past t = 1, or other data or forces (our reading).

## What breaks without each move

- **M10.1:** curl(cA) may be singular at the axis, and at z = 0, r > 0, `∇c × A` would involve A where no bounds exist.
- **M10.2:** cutting velocities breaks div u = 0; without (10.3) the cutoff could reach q = q∗ or beyond, where nothing is controlled.
- **M10.3:** cutoff terms away from the origin have no proven limit at t = 1, so f has no smooth extension.
- **M10.4:** the diverging terms at the singular point have no proven summed limit, and without (10.10) smoothness across t = 1 fails.
- **M10.5:** f exists only on (0, 1); zero extension jumps and the Taylor series may diverge.
- **M10.6:** the full field's energy is bounded only heuristically, so Theorem 1.1's energy claim is unproved.
- **M10.7:** the pressure flux cannot be estimated; a harmonic pressure gradient is not excluded.
- **M10.8:** the nonlocal flux cannot be absorbed with a remainder decaying in R.
- **M10.9:** no uniqueness, so the construction says nothing about other solutions.
- **M10.10:** no proof that the localized field, not only `u_loc`, diverges, and no contradiction.
- **M10.11:** the result holds only at viscosity one.
- **M10.12:** no torus result; overlapping translates would interact.

## Three questions the section leaves open

1. **Can the force be both divergence-free and compactly supported?** Cutting the pressure locally leaves a force with divergence [p. 118]; moving its gradient part into the pressure would in general cost compact support of f and p, since a divergence-free force dictates the Poisson pressure (our reading). The answer would show whether the divergence is an artifact of local cutting or forced by compact support.
2. **What do weak solutions with this force do at and after t = 1?** Comparison covers only smooth bounded-energy competitors before t = 1 [p. 121], and f past t = 1 is an arbitrary continuation [p. 120]. Leray-type solutions should exist globally (our reading; compare [p. 2]); their singular set, their uniqueness afterward, and the role of the continuation would say what the breakdown means outside the smooth class.
3. **How fast does `‖u(t)‖_∞` grow, and where?** Only a lower bound at one family of points is proved [p. 124]. Pulse amplitudes scale like `q^{−1/2−h/2}` [p. 11], below the core scale `q^{−A}`, so a matching upper bound seems plausible (our reading); it would fix the rate against the parabolic `τ^{−1/2}`.

## Page tags

Pages cited, in order: 1, 2, 6, 7, 11, 15, 16, 17, 33, 49, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 138.

Extraction note: superscripts and subscripts were flattened on pages 116 to 126, and displays on pp. 119, 120 and 123 broke apart; all were recoverable.
