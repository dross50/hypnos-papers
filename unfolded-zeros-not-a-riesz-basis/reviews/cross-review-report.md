**Astra referee report - September 29, 2026 (Eastern time)**

Reviewed `main.tex`, `README.md`, `scripts/`, and `data/` in `paper/unfolded-zeros`, after `git pull --ff-only`. The reviewed `main.tex` has Git blob `448de51471f4c0b894dae16212230b7367c74026`, identical to the version at `75c4388`. Unrelated commits advanced `main` during the review. I did not consult the prohibited planning file, status file, other review directory, or other paper directory. After the findings were written, an accidentally unscoped whitespace check traversed the dirty worktree and emitted truncated, unrelated CRLF diagnostics; that output was not used to form or revise the findings. The requested checks were undertaken in order (a)-(i); findings below are ranked by severity. Numerical agreement means agreement at the stated precision, not a new certification of the zero table.

**1. BLOCKING - (f): Theorem 6.1 applies multiplicity-sensitive density to a multiplicity-insensitive span.**

The paper explicitly counts ordinates with multiplicity. Its argument establishes exterior Beurling-Malliavin density one for that counting measure. But two copies of the same function `exp(i lambda t)` have exactly the same span as one copy. Completeness of the exponential system depends on the support of the frequency measure, not its multiplicities.

This is a substantive distinction. Take every point of `2Z` twice. Its multiplicity-counting function satisfies `n(x)=x+O(1)`, exactly the kind of estimate used here, but its ordinary exponential system has completeness radius `pi/2`, not `pi`. The version of the Beurling-Malliavin theorem that counts a point with multiplicity `m` uses the functions `t^j exp(i lambda t)`, `0 <= j < m`. This convention is explicit in [Seip and Ulanovskii, *The Beurling-Malliavin density of a random sequence*, p. 1745](https://www.researchgate.net/publication/268628906_The_Beurling-Malliavin_density_of_a_random_sequence).

The repeated-even-integers example is a counterexample to the inference, not a claim about the actual zeta zeros. The paper supplies no unconditional estimate proving density one for their distinct ordinates. Also, simplicity of the complex zeros alone would not fix this: two simple zeros off the critical line at `beta+i gamma` and `1-beta+i gamma` have the same ordinate.

**Concrete fix:** State the radius equality under an explicit additional hypothesis, such as eventual distinctness of the ordinates, which follows from RH plus eventual simplicity. Alternatively, prove exterior density one for the support by a separate argument. The present argument does establish the unconditional upper bound `R <= pi`, since support counts are at most multiplicity counts. Changing to exponential polynomials would also make the multiplicity version applicable, but would change the system being studied. Correct the abstract and README accordingly. This defect does not invalidate the Riesz-basis obstruction in Theorem 5.1.

**2. MAJOR - (c): Lemma 3.3 is false on its stated domain for negative unfolding constants; the finite-modification discussion also needs correction.**

For sufficiently negative `a`, some `x_a(gamma_n)` are negative. Their reflections are positive frequencies and are missed by the claimed description of the points in `[0,x)`. For example, at `a=-10`, `x_a(gamma_1)` is approximately `-10.55025`, so its reflection produces a positive counting jump near `10.55025`, although the stated cutoff is `x_0=1`. That extra jump is not a jump of `S(t_a(x))`. No choice of a constant `c_0` repairs the asserted identity throughout this domain.

**Concrete fix:** Replace the cutoff by a number

`X_a > max(1, x_a(7), -x_a(gamma_1))`.

Above this cutoff all reflected negative frequencies have been passed. The desired identity then holds with an appropriate additive constant. Alternatively, allow a bounded, compact-prefix correction even for the unmodified sequence. For a finite modification, increase the cutoff past all modified frequencies, or retain the bounded correction already used in the main proof. The subsequent argument only needs sufficiently large `T`, so this fixes every real `a` without changing the theorem.

The paragraph before the proof of Theorem 5.1 incorrectly says that one multiple zero necessarily leaves a repeated frequency in every finite modification. A finite modification can remove that repetition. Replace it with: assume the modified system is a Riesz basis; it consequently has no repeated frequencies. Infinitely many repetitions cannot be removed by a finite modification. Finitely many can be removed and change the counting function by a bounded function. The claim about the set of distinct frequencies should say “all but finitely many ordinates are distinct,” not merely “all but finitely many zeros are simple.”

**CORRECT - (c), after this repair:** The analytic obstruction itself works. In the normalization `exp(i lambda t)` on `(-pi,pi)`, the necessary condition is precisely `n_Lambda(x)-x in BMO(R)`. Rescaling the interval variable from the `exp(2 pi i lambda t)` convention changes no frequency-counting factor. [Kozma and Lev, Theorem 5.1](https://arxiv.org/pdf/1009.2188), explicitly crediting Hruscev-Nikol'skii-Pavlov, p. 240, gives the three conditions quoted here, including the strict `1/4` bound in condition (iii). Calling this the HNP form of Pavlov's theorem is appropriate; the BMO condition is not being confused with a sufficient condition by itself.

The Landau step is valid. Put `d=|I|/(2 pi)`. Ordinary positive-axis density one gives only `D^- <= 1 <= D^+`, but an alleged Riesz basis gives the additional inequalities

`d <= D^- <= 1 <= D^+ <= d`.

Thus `d=1`. It is unnecessary to prove that the actual uniform densities equal one. The sampling/interpolation directions agree with Landau's theorem as stated in [Kozma and Lev, introduction](https://arxiv.org/pdf/1009.2188). The one-sided sequence has lower density zero and cannot be a basis on any interval of positive length. Frequency translations and interval translations are handled correctly by unitary multiplication and unimodular coefficients.

The Jacobian is `theta'(t)/pi`, and its maximum/minimum ratio on `[T,2T]` tends to one. The inequality `|u+w|^2 >= |u|^2/2-|w|^2` is correct. Its use followed by a Jacobian ratio bounded below by `1/2` gives the displayed factor `1/4`. Minimizing over constants subtracts the square of the mean, not the mean of the squares. Littlewood gives that mean as `O(log T/T)`, while Selberg gives the second moment as `(1/(2 pi^2)) log log T+O(sqrt(log log T))`. The resulting lower coefficient `1/(8 pi^2)` is valid. John-Nirenberg is used in the correct direction: BMO implies a uniform bound on these mean-square oscillations, so their divergence contradicts BMO.

Every finite modification is covered by the bounded correction. In fact it is eventually constant, so it can be absorbed into the minimizing constant on all sufficiently large intervals. This also justifies the stronger lower coefficient mentioned in the README for finite modifications. Theorem 5.2 is correct: replacing `Lambda` by `d Lambda` reduces density `d` and interval length `2 pi d` to the stated normalization. No substantive change to this argument is required.

**3. MAJOR - (d): Remark 5.4 has an incomplete verification of condition (iii), but an A2 detour is not necessary.**

For `|c| <= 1`, the separation calculation and BMO conclusion for `lambda_n=n+c log(2+|n|)` are sound. The latter follows from the bi-Lipschitz increasing map `T(u)=u+c log(2+|u|)` and the decomposition into a bounded sawtooth, a logarithm, and a bounded remainder. These establish conditions (i) and (ii).

The stated justification of (iii) skips two points. The remainder is not globally smooth as claimed, because of the absolute values. Also, a gap mean of size `O(1/|n|)` does not by itself imply a uniform Poisson bound `O(1/y)`. The parenthetical Lyubarskii-Seip argument is not a substitute: it does not construct the generating function, establish its exponential type, or prove the claimed upper and lower bounds on its weight. Those are substantive requirements of the [Lyubarskii-Seip criterion](https://arxiv.org/pdf/math/9511212).

Here is a direct repair within HNP. Choose the lattice counting normalization with `s(u)=ceil(u)-u`, and set `q(x)=s(T^{-1}(x))-1/2`. On a distant gap,

`integral_[T(n),T(n+1)] q(x) dx = integral_0^1 (1/2-v) T'(n+v) dv = O((1+|n|)^(-2))`.

The improvement from the asserted inverse-first-power bound follows by subtracting the constant `T'(n)` inside the integral. The gap lengths are uniformly bounded. Consequently `q` has a bounded primitive `Q`, and

`||P_y*q||_infinity <= ||P_y'||_1 ||Q||_infinity = O(1/y)`.

For the drift, use the nonsingular model `g(x)=-(c/2) log(1+x^2)`. The difference

`R(x)=T^{-1}(x)-x+(c/2) log(1+x^2)`

is globally Lipschitz, bounded, and in `L^2`, with tail `O(log|x|/|x|)`. Its Hilbert transform is bounded: use Lipschitz cancellation for the local principal-value integral and Cauchy-Schwarz for the tail. Hence `P_y*R` is the Hilbert transform of a bounded function. The Poisson extension of `g` is `-c log|x+i(1+y)|`, whose harmonic conjugate is bounded. These terms supply the unrestricted bounded conjugate term in (iii), while `P_y*q` supplies a term of norm less than `1/4` for large `y`.

**Concrete fix:** Insert these estimates, or supply a complete generating-function/A2 proof. With the displayed repair, the Riesz-basis assertion for `|c| <= 1` follows. As written, the remark establishes separation and BMO but does not adequately justify its last sufficiency step. Remove or separately prove the sentence about larger `|c|`; restoring separation by a finite modification alone does not establish a Riesz basis.

**4. MAJOR - (e), (h): The abstract L-function corollary is correct, but its asserted applications are not adequately sourced.**

The hypotheses displayed in Corollary 5.3 suffice. The integral bound makes the mean of `S_F` on `[T,2T]` bounded; the divergent second moment therefore gives divergent centered variance. Uniform comparability `theta_F'(t) asymp log t` is sufficient for the change of variables; the Jacobian ratio need not tend to one. The same finite-prefix correction as in finding 2 is necessary.

The sentence applying this to Dirichlet L-functions requires a theorem and page for a *fixed character with height tending to infinity*. The identifiable Selberg 1946 moment theorem discussed in [Zhao, *Conditional estimates on the argument of Dirichlet L-functions*, introduction](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.70360), citing Selberg's Theorem 9, averages over characters as the modulus grows. That is a different statement. It cannot supply the displayed height integral for one fixed L-function. I did not obtain the original 1946 Dirichlet paper in a form permitting verification of another possible theorem there, so I am flagging an unverified attribution, not claiming that no appropriate classical fixed-character result exists.

Likewise, “for the Selberg class ... under its standard hypotheses” is too vague. The needed argument-variance result and any extra prime-coefficient, orthogonality, or zero-density assumptions must be stated. A central limit theorem for `log|F|` is not a theorem about `arg F`; for example, the explicit fixed-character statement in [Hsu and Wong, Theorem 1.1](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1139.pdf) concerns the former. A nondegenerate central limit theorem for the correctly normalized *argument* would suffice to give a divergent second moment by restricting to a fixed interval of normalized values bounded away from zero, but that inference and its assumptions must be supplied. An announcement is not a citation to a proof of every displayed hypothesis.

**Concrete fix:** Keep the conditional corollary exactly in terms of its explicit analytic hypotheses. For each claimed family, give precise fixed-function argument estimates, their hypotheses, and theorem/page references. Describe Selberg 1992 accurately as an announcement where appropriate. Until then, the general implication is proved; the advertised family-wide applications are not verified by the references as presented.

**5. MAJOR - (g): The numerical record contains a specific false sample/error pairing and overstates reproducibility.**

The last sentence of the identity paragraph claims a block residual at most `3.2e-34` over **40** windows. The committed files say:

| File | Continuation samples | Worst identity residual A | Worst block residual B |
| --- | ---: | ---: | ---: |
| `data/verify_10000.json` | 12 | `5.4565149617825e-21` | `3.1420249976497117e-34` |
| `data/verify_10000_40samples.json` | 40 | `7.113139113632402e-20` | `7.280724305602941e-34` |

**Concrete fix:** Say `7.3e-34` for 40 windows, or identify the 12-window run when quoting `3.2e-34`. The common identity bound `<1e-19` and the README's block bound `<1e-33` are supported.

The other principal numerical claims are traceable as follows. These are source checks unless explicitly included in the recomputations at the end of this report.

| Printed claim | Committed evidence and assessment |
| --- | --- |
| Job 313: 1,141 samples, epsilon `1e-6`, residual `1.5e-6` | `job-313/result.json`: `n_identity_samples=1141`, `max_abs_identity_residual=1.4938331778736945e-6`; `identity_residuals.json` stores the raw residuals. This number is the magnitude of the raw one-sided residual, not a separately reported error after subtracting `-epsilon theta'/pi`. |
| Kadec first crossing 9, height 48.005; maxima 0.734, 0.948, 1.129 | Jobs 110/202 and the verification files support the printed rounding, indices, and heights. |
| Centered maximum 1.103; counts 43,588 and 43,639; mean about `-7e-6` | Job 202, job 110, and `verify_kadec_1e5.json` support these. Both counts were independently reproduced. |
| Both rows of Table 1 | Every displayed entry agrees with `verify_kadec_1e5.json`, `verify_10000.json`, and the job 110 scan at printed precision. |
| Block-decay fits -1.03 and -0.94 | Job 110 gives `-1.0279849868018138`, fitted on `4096,8192,16384,32768,65536`; job 67 gives `-0.9437374560542408`. State the fit ranges. These finite fits do not establish an asymptotic `D(M) asymp M^(-1)`. |
| First tested successful length 8; `D(6)=0.330` | Job 110 gives `D(6)=0.33037996666...` and `D(8)=0.21615960561...`. “Among the lengths tested” is necessary. |
| Finite-section exponent -0.79 | Job 263 gives `slope_logA_logN=-0.7945684740716767`. |
| All five one-sided lower and upper eigenvalues | `job-263/riesz_finite_sections.json` and `result.json` support them; my independent double-precision calculation agrees at every printed digit. The recorded primary precision is 50 digits and `max_eig_residual=8.380823906208459e-31`. Specify that residual's normalization: the separately stored unit-infinity-vector residual reaches `1.3098494308946161e-30`. |
| Gaps 0.1376 and 0.02186; index 95,248; height 71,732.9; ordinate gap 0.0147 | Job 263, job 110, and `verify_kadec_1e5.json` support these; job 110 records the corresponding ordinate gap as `0.014701475392323176`. The stated pair bounds 0.0309 and `7.9e-4` are the correct derived rounding. |
| Symmetric lower constants 0.1324, 0.0771, 0.0404 | `job-260/frame_bound_report.json` supports them; my independent calculation agrees. The file records 60-digit primary arithmetic. |
| 100 jitter draws; means 0.0625, 0.0083, `3.1e-5` | Job 260 records means `0.062497071091640065`, `0.008265637519935932`, `3.093374809721891e-5`. I checked the stored values but did not rerun the random ensemble. |

The 100,000th zero has height about `74920.8275`. Thus the table supports the bound about `1.63` for `|S|` up to its own height, not the earlier sentence claiming that bound for every `t <= 100000`. Index and height have been conflated. Replace that height by the actual table endpoint. The values `3.3455` and `7.7573e27` belong to the external [Bober-Hiary computation, Table 2](https://arxiv.org/pdf/1607.00709), not the repository JSON files. Cite them as literature measurements and replace “largest ever” and “no computation has seen” by a dated, attributable statement.

The verification scripts do not independently reproduce every harness experiment. Their block-identity check uses the counting formula and a closed-form interval integral, so it is a useful algebra/implementation check but not a second independent argument-continuation measurement of `S`. The continuation check uses finite phase steps and does not certify that every step is small enough to preclude a missed winding. Neither issue undermines the exact analytic proof. They limit the numerical certification language.

`scripts/make_figures.py` also has an incorrect data path: `HERE` is the `scripts` directory, but `JOBS=HERE/'hypnos-jobs'`; the files are under `data/hypnos-jobs`. Its default output directory is also `scripts`, whereas the TeX reads `figures`.

**Concrete fix:** Use `HERE.parent/'data'/'hypnos-jobs'` and an explicit/default `HERE.parent/'figures'` output directory. Narrow “every number ... was reproduced” to the computations actually supplied, and distinguish independently rerun results from copied job records. Historical jobs 25, 48, 100, and 166 are mentioned, but their JSON artifacts are not among the committed copies. No paper or data file was changed during this review.

**6. MAJOR - (i): The broad novelty claim misses a directly relevant prior preprint.**

[Jan Mikulik, *Unfolded Gaussian Gram Stability for Zeta Zeros*, April 2026](https://www.researchgate.net/publication/403995908_UNFOLDED_GAUSSIAN_GRAM_STABILITY_FOR_ZETA_ZEROS), explicitly describes unfolded zeta ordinates, Gaussian Gram matrices, a Fourier representation by nonharmonic exponentials, and a conjectural frame inequality. The accessible abstract requires qualification of the README's broad negative literature-search claim. It is a preprint; I have not verified its conjectures or a peer-reviewed publication, so it does not establish priority in the narrower sense of refereed work “in print.” Its Gaussian/local-cluster problem is different from the fixed bounded-interval Riesz-basis theorem here, and I found no indication that it proves Theorem 5.1.

There is also older adjacent work: [Jean-Francois Burnol, *Two complete and minimal systems associated with the zeros of the Riemann zeta function*, JTNB 16 (2004), 65-94](https://jtnb.centre-mersenne.org/item/JTNB_2004__16_1_65_0/). Its systems live in the Sonine/de Branges setting and are not the ordinary unfolded exponential family on a bounded interval. It should be distinguished, not presented as the same result.

**Concrete fix:** Cite and compare these works, including the preprint status of the first. Replace the broad absence claim by a narrow statement about the exact theta unfolding and the unconditional Selberg-variance/Pavlov obstruction. My searches combining zeta ordinates or zeros with frame, Riesz basis, complete interpolation, and Kadec found no earlier proof of that precise statement. This is a bounded search result, not a certification of priority.

**7. MINOR - (b), (f), (g), (h): Quantifiers, endpoint bookkeeping, and interpretations need tightening.**

- **The threshold after Theorem 4.1:** `A > N/2+1/4` defeats the uncentered sliding window of the `N` ordinates immediately preceding the excursion. It does not defeat every window or automatically a fixed partition block. With `q=N(t_0)` and `r=q mod N`, the last full partition block has mean at most `r+N/2-A`. For centered means its positive-excursion threshold is `A > r+N/2+1/4-c`; for the preceding sliding window set `r=0`. The following sliding window at a negative excursion has mean at least `A-N/2`, giving threshold `A > N/2+1/4+c`. Restrict the subsequent finite-height “bracketing” language to the relevant windows and centering, and require those windows to lie within the horizon being discussed.
- **Corollary 4.2:** Proposition 3.2 initially treats complete ordinate clusters. For an arbitrary index block cutting through a repeated ordinate, add endpoint corrections. A cluster has `m=O(log b)` and its displacements are `O(log b)`, so the total correction is `O(log^2 b)`, preserving the claim. Replace “below `1/4` as soon as `M >= 4C log^2 b`” by a strict inequality on `M`, or enlarge the constant. A finite-height bound at a sufficiently large multiple of `log^2 T` does not assert the global Avdonin hypotheses.
- **The long-family calculation:** For the multiplicity measure, the lower direction is correct: the dyadic intervals form a long family and have density tending to one. For the upper direction, write `L=|I|`, `r=dist(0,I)`. If the interval has density at least `d>1`, then `(d-1)L <= K log(2+r+L)`, which implies `L <= C_d log(2+r)` by absorbing the logarithm of `1+L`. Disjoint intervals with this length bound have a summable long-family series. In the dyadic proof, also handle intervals crossing dyadic boundaries, for example by grouping them by their nearer endpoint in enlarged dyadic shells. These additions complete both density directions; they do not resolve finding 1's support/multiplicity problem.
- **Tsang's range:** Theorem 3 of [Tsang 1986, p. 370](https://matwbn.icm.edu.pl/ksiazki/aa/aa46/aa4646.pdf) assumes `1/log T <= h <= 1/log log T`. The paper omits the upper bound. Add it. The observation that this result does not force unbounded excursions at a single mean spacing remains correct.
- **Interpretation of numerical bounds:** The pair bound is an upper bound, not a proof that the closest pair determines the observed eigenvalue decay. Replace “is driven by” with the actual implication. A bounded sequence of upper Gram bounds is the Bessel/upper frame condition, not the full frame property, which also requires a lower frame bound and completeness. Theorem 3.1 alone does not predict a small average displacement; cite the block-sum estimate for that conclusion.
- **Separation for every `a`:** The equivalence in the first open question needs exclusion of finitely many cross-half collisions. For example, choosing `a=-theta(gamma_1)/pi` creates two copies of frequency zero regardless of the positive-tail gap behavior. State the equivalence for the tails, or include the finite collision condition.

**8. CORRECT - (a): The displacement and telescoping algebra are correct with ordinate multiplicity.**

Let `m` be the total number of zeros at ordinate `gamma`, counted with their complex-zero multiplicities, and write `n=N(gamma^-)+j`. The mean-value convention gives

`N(gamma)=n-j+m/2`,

so the Riemann-von Mangoldt formula gives

`x_n-n=-S(gamma)+(m+1)/2-j`.

In particular, an ordinate with a single zero gives exactly `d_n=-S(gamma_n)`, and `3/2` is the unique additive constant with that identity. The jump computation is also exact:

`Delta(S^2/2) = (S^+-S^-)(S^++S^-)/2 = m S(gamma)`.

Away from ordinates, `(S^2/2)'=-theta'S/pi`. This proves Proposition 3.2 with its displayed sign. The multiplicity corrections sum to zero over each entire cluster, justifying the displacement version. No RH is used. **Fix:** Define “multiplicity of an ordinate” explicitly as the total jump of `N`, and use “simple ordinate” where the scalar identity is asserted; simplicity of one complex zero is not sufficient if another zero shares its ordinate.

**9. CORRECT - (b): Theorem 4.1's actual proof works for both block forms and every fixed centering.**

At a positive excursion, both the preceding sliding block and the last completed partition block fit inside the last `2N` indices. Monotonicity gives

`d_n <= q-n+1/2-A`,

hence the paper's bound `2N-1/2-A-c`, and the sharper sliding bound `N/2-A-c`. At a negative excursion the next sliding block and next full partition block fit inside the next `2N` indices, and

`d_n >= A+q-n+1/2 >= A+1/2-2N`.

These inequalities do not assume distinct ordinates. Selberg's two-sided unboundedness lets `A` tend to infinity arbitrarily far out, so every fixed `N` and `c` is covered. Passing from a value at an ordinate to a nearby non-ordinate on the appropriate side is legitimate. Consequently both Kadec's bounded-deviation hypothesis and Avdonin's bounded-deviation and fixed-block hypotheses fail as claimed. **Fix:** None to this proof; correct its stronger explanatory threshold claim as in finding 7.

**10. CORRECT, with the exceptions above - (h): Classical theorem and attribution checks.**

| Citation | Check and required action |
| --- | --- |
| Kadec 1964 | The strict supremum bound `<1/4`, its sharpness, and the interval normalization are correct. The original attribution and statement are also recorded in [Alemany-Nitzan, introduction](https://arxiv.org/pdf/2501.11598). No correction needed. |
| Avdonin 1974 / English translation 1979 | Separation, uniformly bounded deviations, and one fixed partition length with strict averaged bound `<1/4` are the relevant sufficient hypotheses. The paper includes them. The sliding requirement is stronger, and its failure is separately proved. See [Alemany-Nitzan](https://arxiv.org/pdf/2501.11598). No correction needed. |
| Pavlov 1979 / HNP 1981 | The quoted formulation is checked against Kozma-Lev Theorem 5.1 and its explicit reference to HNP p. 240, rather than a direct inspection of that original page. Conditions (ii) and (iii) and their normalization are correct. Preserve this attribution chain. |
| Landau 1967 | Necessary sampling lower density and interpolation upper density have the correct directions and factor `1/(2 pi)`. Their use here is valid. |
| Beurling-Malliavin 1967 | Exterior density controls the completeness radius with factor `pi` for `exp(i lambda t)`. The long-family formulation is appropriate. The multiplicity convention is the blocking misapplication identified in finding 1. |
| Selberg 1946, zeta moments | The unconditional even-moment coefficient is `(2k)!/(k!(2 pi)^(2k))`; at `k=1` this is `1/(2 pi^2)`. The stated error `O(T sqrt(log log T))` is valid. See [Goldston, Theorem 8 and its historical discussion](https://arxiv.org/pdf/math/0412313). Subtraction between heights `T` and `2T` gives the version used here. No RH has slipped into this input. |
| Selberg 1946, two-sided Omega result | The stated weaker bound with exponents `1/3` and `-7/3` is correctly attributed. [Tsang, p. 369](https://matwbn.icm.edu.pl/ksiazki/aa/aa46/aa4646.pdf) explicitly records it as Selberg's Theorem 9, before proving an improvement. It supplies both signs, not just unbounded absolute value. |
| Littlewood 1924 | The unconditional `S_1(T)=O(log T)` used here is correct; it is stated and proved in [Titchmarsh, second edition, Theorem 9.9(A), p. 222](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf). Cite the precise subsection. This review verified the estimate through that source, not Littlewood's original article. |
| Selberg 1946, Dirichlet L-functions; Selberg 1992 | Exact fixed-function applications remain unverified for the reasons in finding 4. Do not count bibliographic existence as verification of the required theorem. |
| Tsang 1986 | Correct theorem and relevance, but restore the upper restriction on `h` in finding 7. |
| Ghosh 2015 | Almost-sure completeness for the sine-process exponentials at the critical interval is the claimed result of [Ghosh](https://arxiv.org/abs/1211.2435). Correct after the stated density normalization. |
| Bufetov 2019 | [Theorem 1.1](https://arxiv.org/pdf/1912.13454) gives the asserted excess-one statement: removing one point leaves uniqueness, while removing two permits a nonzero vanishing Paley-Wiener function. Correct. |
| Bober-Hiary | Their [Table 2](https://arxiv.org/pdf/1607.00709) gives `S` approximately `3.3455` just after a zero near `7.757304990367861e27`. Correct historical measurement; it does not establish a current world record or the absence of later larger computations. |
| Inoue 2026 | [The cited preprint](https://arxiv.org/abs/2604.05733) proves, under RH, the stronger bound `mu < 0.50895`. The paper's `0.509` is a valid weakening. It does not imply arbitrarily small gaps. |

**11. CORRECT - (f), (g): Proposition 6.2 is valid, with a minor domain clarification.**

Interlacing proves the monotonicity of both finite-section bounds. Trace gives `A_N <= 1`, with equality forcing the normalized Gram matrix to be the identity. For `N >= 2`, the closest-pair submatrix has eigenvalues `1 +/- |sinc(s_N)|`. These imply the paper's weaker signed-sinc inequalities, and `1-sinc(s) <= pi^2 s^2/6` for `s >= 0` is valid. Set `sinc(0)=1` by continuity. **Fix:** Specify `N >= 2` for the closest-pair assertions and avoid the unsupported causal interpretation noted above. The numerical pair bounds are correctly evaluated.

**Verdict on Theorem 5.1:** The unconditional Selberg-Pavlov obstruction is proved in substance, and I find no missing number-theoretic input or incorrect density/BMO implication in it. Literally, the text relies on a false all-`a` counting lemma and an incorrect sentence about finite modifications; the explicit finite-prefix and repetition corrections in finding 2 complete the proof for every stated constant, finite modification, and translation. These are local repairs, not a new argument. I would require revision before acceptance, principally because Theorem 6.1's unconditional lower completeness claim is not established for the system actually defined, and because the auxiliary drift proof, L-function applications, novelty claim, and numerical reporting need the corrections above.

**Numbers recomputed in this review:**

- `python3 scripts/verify_identity.py 2000 4 100`, run from `paper/unfolded-zeros`, exited successfully using 40-digit arithmetic. Worst identity residual: `1.5640209832550602e-20`; worst block residual: `3.664847576725151e-36`. Sample indices: `276,1166,1644,1736`; sampled block lengths: `17,121,125,1`. First Kadec crossing: `n=9`, `gamma=48.00515088116716`. Maximum absolute displacement: `0.7917062763792165` at `n=1936`; optimal centering: `0.01845572009915874`; centered maximum: `0.7732505562800578`; mean: `4.665561256538092e-5`; RMS: `0.2691452102544524`.
- `python3 scripts/verify_kadec_1e5.py 20000`, run from the same directory, exited successfully using 30-digit arithmetic. Maximum absolute displacement: `0.9538094665055175` at `n=17687`, `gamma=16210.037038862605`; optimal centering: `0.0026690846588876397`; centered maximum: `0.9511403818466297`; mean: `-6.280925676039517e-6`; RMS: `0.296157423202349`; uncentered quarter-bound crossings: `8282`. Minimum unfolded gap: `0.042098398548154926` at `n=6709`, `gamma=7005.062866174921`. First crossing again: `n=9`.
- Supplemental full 100,000-zero recomputation: maximum absolute displacement `1.1286944467284874` at `n=94352`, `gamma=71128.97080156027`; optimal centering `-0.02565465576822247`; centered maximum `1.1030397909602647`; mean `-6.988858649370489e-6`; RMS `0.3108484384964092`; uncentered and centered crossing counts `43588` and `43639`. Minimum unfolded gap `0.021860465151190524` at `n=95248`, `gamma=71732.90120787236`; corresponding pair bound `0.0007858956314403023`. Maximum absolute one-sided limit of `S` over this table: `1.6286944467284874`.

| Block length M | D(M), first 2,000 | D(M), first 20,000 | D(M), first 100,000 |
| ---: | ---: | ---: | ---: |
| 1 | 0.7917062763792165 | 0.9538094665055175 | 1.1286944467284874 |
| 2 | 0.515142300535341 | 0.7069410074560556 | 0.7951094246158471 |
| 4 | 0.2737439416102994 | 0.3936986383790763 | 0.4725894059501196 |
| 8 | 0.09160850196433806 | 0.17363831855787895 | 0.2161596056119217 |
| 16 | 0.05699941923833415 | 0.10263498809093101 | 0.10263498809093101 |
| 32 | 0.02914561854432792 | 0.04631575935595357 | 0.06161062998700859 |
| 64 | 0.017990631923044745 | 0.021762030674296422 | 0.02796555305213705 |
| 128 | 0.009596173958432777 | 0.012832700146973755 | 0.015008907134334264 |
| 256 | 0.00415284246166046 | 0.006163687435001211 | 0.007694854688348393 |
| 512 | 0.002150140437333491 | 0.0030200553673975505 | 0.004062270624299117 |
| 1024 | 0.0009580129539717129 | 0.0015136395423014121 | 0.0019394880997338293 |
| 2048 | Not in this run | 0.0007671213429424084 | 0.000996519226034616 |
| 4096 | Not in this run | 0.0003756588362130771 | 0.0004904913564794435 |

The requested 2,000- and 20,000-zero runs have different sample sizes from the published 10,000- and 100,000-zero records, so their extrema should not be expected to equal the published extrema. The supplemental 100,000-zero run does match the corresponding record at every printed digit.

- Independent `numpy.linalg.eigvalsh` calculations, using a normalized sinc Gram matrix and ordinates unfolded with mpmath at 40 digits, gave the following one-sided values. The eigensolver itself used double precision; these runs verify the displayed values, not the recorded 50-digit residual certificates.

| N | A_N | B_N |
| ---: | ---: | ---: |
| 100 | 0.11150334614439504 | 1.953086215559961 |
| 200 | 0.07743269808437789 | 2.0622406097220773 |
| 400 | 0.04207577712008683 | 2.1153976833356047 |
| 800 | 0.02832180995068679 | 2.2774813289865348 |
| 1000 | 0.01585470831056607 | 2.2779556135364905 |

- Independent symmetric-section minima: `r(50)=0.1324135638754068`, `r(200)=0.07707074823652549`, `r(500)=0.04035550315429591`. Recomputed first-1,000 minimum gap: `0.13762757819271076`; pair bound: `0.030867332588322957`. These agree with every corresponding printed finite-section value. The jitter ensemble and high-precision eigenpair residuals were checked in the JSON records, not independently rerun.
