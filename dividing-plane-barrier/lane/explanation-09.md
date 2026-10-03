# Section 9, explained: Residual improvement and the local field (pages 100 to 116)

## The problem this section is handed

Section 5 supplied a smooth axisymmetric background whose residual is minus the divergence of a stress supported in a thin annulus, plus an already flat remainder [p. 11]. Section 7 added two families of divergence-free pulses whose averaged quadratic flux supplies the leading part of that stress [pp. 11-12]; Section 8 built inverses for the angular mean [p. 100].

Sizes are powers of ε = Q^h (0 < h < 1/100) on dyadic bands where the concentration scale q, comparable to τ = 1 - t in the core, is comparable to Q [p. 7, p. 17]; a normalized residual times Q^(-2A-1/2), with A = 1/2 + h, is the physical one [p. 101]. The pulses have normalized amplitude ε^(1/2) [p. 106], so the stress they cancel has order ε. What they leave is not yet smaller: the nonzero angular harmonics of the residual have order ε^(1-3κ_s), and the mean balances and three scalar integral defects order ε^(1-κ_s), with κ_s = 10^-5 [p. 100, pp. 106-107]. Our reading: the pulses trade a residual only a stress could absorb for same-size pieces that inverses can absorb, physically still about q^(-3/2-h), the size of the stress divergence [p. 11], and unbounded.

Theorem 3.1 asks for [pp. 15-16] an exactly divergence-free field curl A + B e_θ, smooth at the axis, whose residual has all space-time derivatives O(q^N) for every N on bounded ranges of the similarity radius X; the exact heat exterior beyond some X_ext; one-sided limits at τ = 0 of all derivatives of A, B e_θ, and p wherever q ≥ c > 0; and swirl growing like τ^(-A) along a fixed path. Every N is needed because Section 10 turns this residual into the force [p. 16] and each derivative costs a fixed power of q [p. 14], so any finite order of vanishing loses to enough derivatives (our reading).

## What a person would try first, and why it fails

**Invert everything at once.** No single inverse can take the whole residual: each accepts one form of source. The pulse inverse takes harmonics supported in the pulse rectangles with envelope bounds [pp. 103-104]; inverting the fast time derivative needs zero average over the auxiliary torus, the extra phase variable that keeps pulses apart [p. 12]; a compactly supported radial primitive needs zero weighted radial moments [p. 88]. And whatever one inverse does, the quadratic and cross terms regenerate the other forms [p. 13, p. 100], so the construction must cycle.

**Newton's method.** At stage j, linearize about the current field, so only the quadratic term survives and the error exponent doubles. Our reading of the obstacle: the current field contains the waves already added, whose advection couples each harmonic to its neighbors, so the principal part is no longer a separate ODE along each pulse, and every inverse's coefficients and divisors would move. Invertibility was proved once, below one threshold, for the fixed background and primary pulses [pp. 111-112]; a moving operator needs a new proof, and perhaps a smaller threshold, at every stage, and shrinking thresholds leave no neighborhood of the singular point on which to sum.

**Re-solve the positive stress problem.** The leading stress was written with positive weights on two wave directions, which became squared amplitudes [p. 10, p. 12]. To absorb a new averaged residual Σ, recompute weights for T + Σ and take square roots again. That needs positivity at every stage, but the weights vanish at the annulus edges along with the target stress [p. 10, p. 105], so a correction of either sign can turn them negative, and square roots near zero lose smoothness (our reading). The manuscript explicitly avoids any square root of the current covariance [p. 109].

## The idea, motivated

**An exact identity invites iteration.** The nonlinearity is quadratic, so an increment (δu, δp) changes the residual exactly: R(u + δu, p + δp) = R(u, p) + L_u(δu, δp) + ∇·(δu ⊗ δu), with L_u the linearization about u [p. 13, p. 105]. Cancel R(u, p) with any operator you can invert; what it misses, plus the quadratic term, is the next residual, and the section is its accounting. The unit is ε, comparable to the core's ratio of radius to height [p. 4]; pulses oscillate at frequency k ≈ ε^(-1/2) [p. 22]. A coefficient has order α if bounded by ε^α times fixed edge weights and logarithms: W_α for wave amplitudes, M_α for angular means, S_α for radial moments [p. 18].

**Four inverses, in order.** Since each inverse accepts one form, a cycle applies four, recomputing pressure and the full residual after each [pp. 107-108].

(i) Harmonics (M9.6). Mean operations never create a nonzero harmonic [p. 104], so waves must remove them via the pulse amplitude equation [p. 108]. The part of the linearized operator that equation ignores is smaller by ε^(1/2-3κ_s) (M9.1) [pp. 101-102]; Lemma 9.2 bounds the products (M9.2) [pp. 102-103]. The new waves disturb the angular mean at order C* - κ_s, C* being the current mean order, but conservation pays a bonus: with two velocity moments held at zero, the weighted radial moments of the mean residual are ε times axial derivatives of flux integrals, a full order better (9.12) [p. 94, p. 108].

(ii) The torus-averaged mean (M9.7). The fast-time inverse cannot touch it, but once its weighted moments are removed it is the radial divergence of a compactly supported stress [p. 108]. So subtract a fixed bump times each moment, harmless by the bonus, and integrate radially [p. 109]. Realize that stress by moving the amplitudes to first order about the fixed primary ones, δa_σ = (dΣ)_σ/(2a_σ): either sign, no square root [p. 109]. This repairs the third attempt. At the edges the source carries a full edge weight and the amplitude only its square root, so the quotient stays smooth [p. 105].

(iii) The torus-dependent mean (M9.8). After (ii) the mean keeps a part of order H = C* - 2κ_s with zero torus average [p. 110]. Since fields are evaluated on the torus along the phase map, the normalized time derivative splits into a slow part ε∂_T and a derivative along a fixed torus direction of irrational slope [pp. 63-64, p. 110]. On zero-average functions that fast derivative is inverted by Fourier division, losing four torus derivatives and no power of ε [p. 96]; the slow leftovers gain about one order [p. 110].

(iv) The defects (M9.9). Pressure and stress corrections stay compactly supported only if three radial integrals vanish [p. 93]. A fixed linear map on five bumps in a reserved patch, where the background is an exact power law, cancels their linear parts and keeps the two moments at zero [p. 111]; its invertibility is a Vandermonde determinant [p. 97].

Flat pieces fit no inverse and need none (M9.3): the background remainder, cutoff remainders, and pulse-cutoff tails, which live where the envelope is below e^(-cℓ²) while Q = 2^(-ℓ) [pp. 102-103]. They are set aside, never fed to a forward solve [p. 105], and never summed [p. 115].

**What one cycle must reproduce.** The minimal record (Definition 9.4, M9.4) is three orders, B_j = 1/2 + σ_j for harmonics and C*_j = 1 + σ_j for tangential means and defects, plus the two zero moments and bounds on the accumulated correction, which every new increment meets [p. 106]. The offset 1/2 is natural: a wave increment of order B moves the mean covariance, through the order-1/2 primary wave, at order B + 1/2 [p. 108].

**Freeze the inverses, accept an additive gain.** Every inverse is linear, with coefficients fixed by the background and primary pulses: the amplitude equations, the divisors 2a_σ, the five-bump matrix [pp. 111-112]. First, one domain 0 < q < q_big then serves every stage, for sources of any size; higher harmonics only add damping, so they need no smaller threshold (M9.11) [pp. 111-112]. Second, what Newton would absorb stays in the residual: cross terms with old waves at B + 1/2 - κ_s and with the accumulated mean at B + 0.4 [p. 108]. Two exact cancellations keep those margins positive. Wave self-advection would naively cost a factor k, erasing the half-order gain; the divergence-free identity turns that factor into amplitude derivatives, so the advecting wave must include its curl remainder [p. 101, p. 103]. At initialization the primary covariance cancels the order-zero stress exactly, slow-partition derivatives included, since the squared partition functions sum to one; the averaged mean starts at order 1.49 (M9.5) [p. 107]. Third, the gain is additive: every margin is at least 0.17 when B ≥ 0.7 [p. 111]. The weakest is the signed correction times the deviation of the current wave from the frozen primary wave, held at order 0.68 [p. 106, p. 109]. Our reading: this is the price of freezing, as in any frozen-derivative iteration. The schedule claims 1/10: σ_0 = 1/5, σ_(j+1) = σ_j + 1/10 (M9.10) [p. 14, p. 107].

**From ε to q (M9.12).** Each physical derivative of a phase factor costs about Q^(-1/2-h/2) in space or Q^(-1-3h/2) in time, at every stage [p. 113]. So the jth increment is O(q^(g_j - ℓ_m)) with g_j = hj/10, and the stage-j residual is O(q^(hσ_j - K_m)), with ℓ_m, K_m independent of j, up to logarithms and the flat part [p. 113].

**Summation: the naive series, then the repair (M9.13).** Adding all increments is natural, but the constants depend on j with no stated bound [p. 14, p. 111], so nothing makes the series converge. The repair multiplies the jth potential, azimuthal field, and pressure by χ(a_j q), which vanishes unless q < 1/a_j, with a_j so large that there the gain q^(g_j) beats the jth constants, leaving at most 2^(-j) q^(g_j/2) through order j [pp. 57-58]. The sum is locally finite for q > 0; near q = 0 it differs from a suitable fixed stage J by less than any prescribed power of q, and comparing residuals with that stage gives flatness (9.20) [pp. 114-115]. Cutting potentials before the curl keeps the field exactly divergence-free [p. 14, p. 114]. Our reading: this is the classical Borel construction's shape, unnamed in the manuscript.

**Up to t = 1, away from the origin (M9.14, M9.15).** Where q ≥ c > 0, only finitely many cutoffs are nonzero [p. 115], and η = ±1 there describes t = 1 [p. 7]. Each surviving term comes from discrete choices fixed on the closed range τ ≥ 0 and linear ODEs along paths inside it, so its derivatives stay bounded, and the fundamental theorem of calculus gives one-sided limits [pp. 115-116]. No correction reaches the growth point X_in < X_a or the exterior beyond X_b, where zero axial moments make the background streamfunctions vanish; the heat exterior and the swirl τ^(-A)(e_0 + O(τ^(2h))) survive [p. 116].

## What breaks without each move

- M9.1, linear residual of a pulse: a wave correction could leave an error as large as its source [pp. 101-102].
- M9.2, interaction estimates: wave self-advection loses k ≈ ε^(-1/2), the entire half order each wave step gains [p. 103].
- M9.3, quarantined flat part: flat pieces would reach the pulse inverse, whose hypotheses they fail [pp. 103-105].
- M9.4, finite correction state: interactions with the accumulated correction go unbounded, and the bonus (9.12) is lost [p. 106, p. 108].
- M9.5, initialization: the averaged mean stays at order 1 - κ_s, below the 1.2 the schedule starts from [pp. 106-107].
- M9.6, harmonic inverse: harmonics, which no mean operation reaches, stay at order B [p. 104, p. 108].
- M9.7, signed stress correction: the torus-averaged mean, invisible to the fast-time inverse, stays near order C* [pp. 108-110].
- M9.8, fast-time inverse: the torus-dependent mean stays at order H, since the stress map takes only torus-independent stresses [p. 103, p. 110].
- M9.9, five-equation map: the defects stay at order H, and with them the radial pressure leftover and the moments the next stress step removes [p. 106, p. 108, p. 111].
- M9.10, closing inequalities: without a stage-independent margin, σ_j need not tend to infinity [p. 111].
- M9.11, common domain: thresholds could shrink stage by stage to nothing [pp. 111-112].
- M9.12, stage-uniform derivative loss: ε-gains would not become q-gains usable by the summation [pp. 113-114].
- M9.13, cutoff summation: increments whose constants grow in j need not sum to any field [pp. 114-115].
- M9.14, one-sided limits: Section 10 could not show the force has limits as t ↑ 1 where q stays positive [pp. 115-116, p. 16].
- M9.15, exterior and growth: corrections could spoil the zero exterior residual or the growth path [p. 116].

## Three questions the section leaves open

1. **Can the rate rise without losing the common domain?** The gain is h/10 in powers of q per cycle, below 10^-3 [p. 113]. By our arithmetic from the normalization [p. 101] and the harmonic order B_j [p. 106], the stated schedule guarantees even a bounded physical residual only after more than 1,500 cycles, for every h < 1/100. The binding margin comes from linearizing at the frozen primary wave [p. 109]. Whether occasional re-linearization, a partial Newton step, can raise the rate while keeping one q_big matters for any explicit or machine-checked version.

2. **How fast do the stage constants grow?** Constants and derivative counts may depend on the stage without stated bound [pp. 111-112], and the Borel-type sum absorbs any growth, so (9.20) is purely qualitative [p. 115]. A bound, say factorial in j, would make the cutoff scales explicit and let one ask whether the force near the singular point, which is this residual [p. 16], is Gevrey rather than merely C^∞.

3. **Is the half-order mean-wave loss sharp?** Mean advection of a wave differentiates its phase and costs k ≈ ε^(-1/2) [p. 103], so wave errors from the accumulated mean sit at B + 0.4 only because that mean is held at order 0.9 [p. 106, p. 108]. Our reading: the loss arises because phases are transported by the fixed background, not by the corrected mean [p. 102]. It matters because it sets how small the primary construction's mean errors must be for the cycle to start.

## Page tags

pp. 4, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22, 57, 58, 63, 64, 88, 93, 94, 96, 97, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116.

Extraction note: sub- and superscripts and tables are flattened throughout pages 100 to 116; worst is page 113, whose radial chain-rule coefficient is illegible (nothing above uses it). No page was unreadable. Page 112 reuses B_j for an azimuthal increment; here it is the harmonic order.
