# Dividing-plane barrier: independent Astra review

Reviewed October 2, 2026, 12:15 a.m. EDT (America/New_York). Reviewer: GPT-6 Astra. Frozen source: `main.tex` and its 12-page `main.pdf`, including the consistency-pass changes in commit `7c3931b`. Locations below use the current TeX line numbers and printed PDF pages. This review proposes changes; it changes no manuscript.

Read the earlier cross-vendor review in `docs/research/2026-10-01-ns-open-map/reviews/astra/`, the paper's Claude report and disposition, and the latter's consistency-pass record. The present assessment is of the resulting statements, not an acceptance of the previous verdicts by inheritance.

## A. Statements against proofs.

| Statement | Verdict | Proof and hypothesis check |
|:--|:--|:--|
| Lemma 3.1, TeX 133, PDF p. 6 | **CORRECT** | At `eta=0`, the assumed vanishing of `U` kills `H_c H_eta`; it also makes all radial derivatives of `U` zero on the core. `L=1`, `W=1-w`, and the first stress-free equation gives (14) with the displayed sign of `hH`. Full parity is unnecessary. |
| Theorem 3.2(1), TeX 152, pp. 6-7 | **CORRECT** | Axis regularity and positive `phi` give `D_X H>0` initially. A first zero contradicts the positive source when `h>0`; when `h=0`, uniqueness for the homogeneous first-order equation on an interval away from zero supplies the strict conclusion. This includes the endpoint `X_a`. The extension to all `h>=0` concerns the scalar equation, as stated. |
| Theorem 3.2(2) | **CORRECT** | `b_s=0`. The shear frame is used only where `a>0`; the theorem does not divide by zero when `a=0`. |
| Theorem 3.2(3) | **CORRECT** | The running supremum is frozen at the radius under consideration. The maximal interval with `a>A_*(B)` handles both a positive entrance point and entrance at the axis. The cases `B>1+h`, `1<=B<=1+h`, and `B<1`, including `h=0, B=1`, all have the required derivative sign. The lower bound on `2-a` is not an equality or an upper bound. |
| Theorem 3.2(4) | **CORRECT** | At the inner annulus boundary, `a<=0` violates the required positive lower bound on `a`; `a>0` gives `v_s=a<2` and violates the other lower bound. The reference squared growth rate is negative in the latter case. No statement about an undefined frame is needed. |
| Proposition 4.1, TeX 210, pp. 8-9 | **CORRECT** | This is the source's terminal `S` identity, with compact radial support of `U` and an integrable positive heat tail for `h>0`. It forces axial velocity somewhere on each slice, not necessarily on the axis. Credit to Duraiswami is correct. |
| Lemma 4.2, TeX 226, p. 9 | **CORRECT** | The corrected range is `X>=X_b`. Canonical pressure in the pure heat exterior is independent of physical `z`, so `S_n=0` and `XN_s` is constant. With `R=(1/2) integral_X^infinity E^2`, heat scaling gives `d R_eta=4h eta R-eta X E^2`; this cancels the remainder in the integrated source identity and gives exactly `K(eta)`. The larger meridional-vanishing range alone would not suffice. |
| Proposition 4.3, TeX 241, pp. 9-10 | **CORRECT** | `V_0=0` gives `dM'+2D eta M=0`, whose interior solutions are `c d^D`. Oddness forces `M=0`. The weighted tail condition gives `K=0`, hence `S=c d^(-2h)`. Uniform heat-tail integrability and finite-core smoothness make `S` bounded at both endpoints, forcing `c=0` for `h>0`. No unjustified inference from an unweighted decaying stress remains. |

There are no other theorems, propositions, lemmas, or corollaries. Remarks 3.3, 3.4, 3.7, 4.4, and 4.5 have the stated limits: the `a=0` example solves the first stress-free equation; the parity computation is formal; no existence theorem for symmetric data is asserted; the `h=0` heat tail is outside the finite-moment class; the analyticity result's on-axis hypothesis is stronger than this paper's slice conclusion. Remark 3.5 needs NS-1 below. Remark 3.6's centrifugal reading is confined by the introduction's express denial of a full stability theorem.

**NS-2, MINOR: restore the physical similarity factors.** Location: TeX 222 and 224, PDF p. 9, the two paragraphs between Proposition 4.1 and Lemma 4.2. The normalized moment is identified literally with the physical flux, and the normalized constant `XN_s=K` literally with the physical tail coefficient. At fixed `(z,t)`, `r dr=q dX`, so the actual identities are

```text
integral_0^infinity (u_z^2+p) r dr = q^(1-2A) S_infinity = q^(-2h) S_infinity,
r T_z = q^(-A) K(eta)/L.
```

These factors are positive and independent of radius, so every zero condition and every proof survives. **Fix:** call `S_infinity` the normalized flux, display the first equality, and replace the assertion that the physical coefficient is the same constant by the second equality. The first factor is explicit in the pinned source's Lemma A.8, p. 141; the second follows directly from source (4.3) and (4.11), pp. 25 and 27. This is a units and identification error, not an obstruction to either theorem.

## B. Abstract and introduction against the statements.

The abstract's inequality is now correctly restricted to `B>1+h`; the complementary `a<=0` case is present. Strict angular-momentum monotonicity, strict `a<2`, vanishing axial shear, and the failure at the inner boundary all agree with Theorem 3.2. The introduction correctly splits the frame condition and uses the squared growth rate. Its `h>=0` assertion is explicitly about the scalar equation. The global flux statement retains the terminal identity, and the relaxed form retains the symmetric-profile context developed in Section 4.

**NS-1, MINOR: distinguish the lower bound from the actual margin and remove the unsupported limiting stability claim.** Locations: abstract, TeX 23, PDF p. 1; introduction, TeX 42, p. 3; Remark 3.5, TeX 195, p. 8. The bound `2h/(B-1)` is linear in `h` for fixed `B`, but the theorem does not say that the actual margin is proportional to `h`, or vanishes as `h` tends to zero. The closing sentence of Remark 3.5 makes that stronger assertion. For example, at `h=0` and constant `w=4`, the scalar equation has `H=c(1-exp(-3X/2))`, giving

```text
2-a = 3X/(exp(3X/2)-1) > 0
```

at every fixed positive dimensionless radius. The margin near the axis approaches 2, as the same remark already acknowledges. A bound degenerating with a parameter is not proof that the bounded quantity does so. Nor is a sign criterion by itself a marginal stability theorem.

**Fix:** in all three places say that the *explicit lower bound* is linear in `h` for fixed `B>1+h`. Replace Remark 3.5's limiting stability sentence with: "This lower bound degenerates as the anisotropy tends to zero; the theorem asserts neither convergence of the actual margin to zero nor spectral stability." Adjust the introduction's final sentence on loss of uniformity to refer to the bound only. No displayed theorem changes.

## C. Sources.

The OpenAI PDF was fetched anew from the bibliography's URL. It has **166 pages** and SHA-256 **`0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`**, exactly the pinned value. This check concerns the cited version, not an unspecified current revision. [Pinned PDF](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf).

| Source and manuscript use | Result of fresh check |
|:--|:--|
| OpenAI, abstract fragments and the long introduction quotation | All quoted words and mathematical conditions match source p. 5, after ordinary PDF line wrapping and mathematical typesetting are removed. The short angular-velocity quotation in Remark 3.6 matches p. 6. |
| OpenAI, equations and page locators in Sections 2-4 | (4.1), p. 24; Lemma 4.1 and (4.2)-(4.6), p. 25; (4.7)-(4.10), p. 26; (4.11)-(4.14), p. 27; (4.15)-(4.16), p. 28; (4.20), p. 30; cone conditions, pp. 31-32; Theorem 4.6(i)-(v), p. 33; Proposition 4.10(ii), p. 37; the squared growth rate immediately above (7.1), p. 74: all resolve and agree with the transcriptions. |
| OpenAI, axis construction and tail references | (B.1), p. 144; (B.3), p. 145; Proposition B.2, pp. 146-148; Proposition B.3 and (B.19)-(B.21), pp. 148-150; (B.25), p. 151; Lemma A.8, p. 141: checked in the fetched PDF. The uses are accurate, subject to NS-2's physical factors. |
| Duraiswami, arXiv:2609.17642v1 | Fetched 31-page PDF. The partial formula quotation and the axial-through-flow quotation match p. 20. Its pp. 6 and 20-22 support the characteristic, moment, numerical cone, and centrifugal-criterion attributions. The paper correctly limits computed cone failure to the profiles computed. Title, author, version, and year match p. 1. [PDF](https://arxiv.org/pdf/2609.17642v1). |
| Lei and Ren, arXiv:2609.35406v2 | Fetched 245-page PDF. Both quoted sentences match pp. 108-109; pp. 107-109 really concern their linear model and fixed positive shift. The explicit lack of a uniform zero-shift limit is on p. 108. Bibliography matches p. 1. [PDF](https://arxiv.org/pdf/2609.35406v2). |
| Constantin, Ignatova, and Vicol, arXiv:2609.20803v2 | Fetched 34-page PDF. Remark 2.6 and footnote 9, p. 11, require nonzero axial velocity at an axis point. Remark 4.5 correctly refuses to derive this from a nonzero slice integral. Bibliography matches p. 1. [PDF](https://arxiv.org/pdf/2609.20803v2). |
| Liu, arXiv:2609.14292v1 | Fetched 32-page PDF. The full-flow results are conditional on a completion input, pp. 1-2. A stationary center on p. 8 is not a reflection-symmetric profile; p. 19 expressly uses the zero-bias auxiliary core only for a parity estimate, not as a completed exit. The comparison is fair. Bibliography matches p. 1. [PDF](https://arxiv.org/pdf/2609.14292v1). |
| Rayleigh, 1917 | DOI metadata confirms author/title, volume 93 and pp. 148-154. Fresh publisher PDF access returned HTTP 403; the original full text was not checked here. [DOI](https://doi.org/10.1098/rspa.1917.0010). |
| Ludwieg, 1960 and 1961 | The 1961 entry is supported by the bibliography of the primary Leibovich-Stewartson paper; the 1960 and 1961 volume/page records also occur in the NASA report, p. 24. Neither original article was obtained. The abbreviated title of the supplement is identifiable, but this is not a fresh full-text certification. [NASA record PDF](https://ntrs.nasa.gov/api/citations/19680007009/downloads/19680007009.pdf). |
| Leibovich and Stewartson, 1983 | Publisher record confirms title, authors, volume 126, pp. 335-356 and DOI 10.1017/S0022112083000191. Its abstract states the centrifugal sufficient condition with axial shear. No complete fresh publisher PDF was obtained; this review does not certify every historical qualification of that condition. The paper's actual pulse criterion comes from the pinned OpenAI equations. [Publisher record](https://doi.org/10.1017/S0022112083000191). |
| Burgers, 1948 | Publisher search record resolves the chapter title and year under DOI 10.1016/S0065-2156(08)70100-5. Fresh full-text access returned HTTP 403; the chapter's exact historical formula and page range were not independently certified. The constant-strain scalar example itself was rederived above. [Publisher chapter](https://www.sciencedirect.com/science/article/pii/S0065215608701005). |

All direct quotations and the numbered source locations on which the proofs depend were checked. Historical original access remains incomplete as itemized. That is an explicit limit of this review, not a claim that those sources were read through another service.

## D. Priority and positioning.

Bounded independent search receipt: October 2, 2026, approximately 12:10-12:15 a.m. EDT (America/New_York). Queries included `"Navier Stokes" "dividing plane" "barrier"`; `"angular momentum" "2h" "symmetric" OpenAI Navier Stokes`; `"Ludwieg" "359" "361" 1961`; `"Leibovich" "Stewartson" 1983 sufficient condition columnar vortices`; and the Rayleigh/Burgers title-and-year queries. The first two returned no relevant indexed statement of the exact barrier. The historical queries returned the primary publisher records and NASA bibliography identified in Section C, plus secondary material not used to establish priority.

The independently fetched adjacent papers give the more useful result: Duraiswami p. 20 already proves the moment obstruction; OpenAI p. 5 states the symmetry-breaking rationale; Lei and Ren pp. 107-109 explain the same design choice in a linear model. None of those inspected passages states this paper's exact nonlinear scalar barrier with its running-strain bound. This is a bounded failure to find a predecessor, not a proof of novelty. The current closing paragraph's explicit statement that priority is unestablished is the right size. Retain it. The value offered to a first reader is a short explicit proof and quantitative refinement of an already articulated rationale.

## E. The attribution block and the house rules.

The block names both reviewer model lines and their actual verdicts, including Duraiswami's priority and the repaired tail hypothesis. The self-review's 3 major and 17 minor findings agree with its report. It states exactly that no human mathematician has reviewed the paper, places it in the second problem lane, and identifies the owner's responsibility. The fresh review here is not represented as a human endorsement.

The source and rendered PDF use the common house format. All 12 PDF pages were text-inspected; the figure page was also visually inspected. No broken mathematical glyph or clipped figure was found. US English and the no-em-dash rule are satisfied in manuscript prose; original German bibliography titles are source titles. The mathematical scope restrictions are appropriate, except for NS-1's stronger prose about the margin. The local program's finite series and sampled checks are expressly distinguished from proof and existence. I did not rerun a research look or any fleet workload.

## F. Verdict.

- **BLOCKING: 0 findings.** Every numbered mathematical statement is correct under its stated setting.
- **MAJOR: 0 findings.** No proof repair or new hypothesis is needed.
- **MINOR: 2 findings.** NS-1: describe the lower bound, not the actual margin, as linear in anisotropy. NS-2: restore the physical flux and stress scaling factors.

**First-reader decision: READY as it stands**, with NS-1 and NS-2 recommended before refreshing the package. Both are local explanatory corrections; the theorem, piecewise inequality, and relaxed tail obstruction remain unchanged. Historical original-source checks remain incomplete as disclosed in Section C, and mathematical priority remains unestablished.
