# Related work and priority audit

Search conducted September 28, 2026 EDT. This is a scoped literature audit,
not proof that no prior publication contains the result.

## Primary sources examined

1. Jack Edmonds, *Maximum matching and a polyhedron with 0,1-vertices*,
   Journal of Research of the National Bureau of Standards B 69B (1965),
   125-130. [Original paper](https://nvlpubs.nist.gov/nistpubs/jres/69B/jresv69Bn1-2p125_A1b.pdf).
   Section 2, Theorem (P), provides precisely the vertex and odd-set
   inequalities used in the manuscript. Section 3 provides the dual used
   for certificates. Those results are explicitly attributed to Edmonds.

2. Terry A. Loring, *Transforming antiunitary symmetries to a normal form*,
   arXiv:2508.13004 (2025).
   [Full text](https://arxiv.org/html/2508.13004v1).
   Discusses constructive normal forms, even and odd antiunitaries, invariant
   observables, and simultaneous normal forms. It does not present the soft
   commutator-plus-square-penalty matching formula. Its classical normal-form
   facts are background, not the manuscript's novelty claim.

3. Eugene P. Wigner, *Normal Form of Antiunitary Operators*, Journal of
   Mathematical Physics 1(5) (1960), 409-413.
   [Publisher DOI](https://doi.org/10.1063/1.1703672).
   Bibliographic identity and the normal-form content were cross-checked
   against Loring. The publisher endpoint did not yield the full paper in
   this session; this is not recorded as a full-text inspection of Wigner.

4. Nicholas J. Higham, *Matrix Nearness Problems and Applications*, in
   Applications of Matrix Theory (1989), 1-27.
   [Author-hosted reprint](https://nhigham.com/wp-content/uploads/2023/10/high89n.pdf).
   Provides the matrix-nearness framework. The proposed theorem specifies
   an objective and constraint not identified with a result in this survey.

## Recent adjacent work checked at the abstract level

- Noferini and Zhukov, *Matrix nearness problems: Do real inputs admit real
  solutions?*, [arXiv:2609.14828](https://arxiv.org/abs/2609.14828).
  Its stated targets are normal matrices and stability regions. The present
  real-optimizer conclusion is specific to the weighted antiunitary objective,
  and does not assert a general principle for real inputs.
- Hokkyo and Tajima, *Quantitative Wigner-Araki-Yanase Theorems for Unitary and
  Antiunitary Symmetries*, [arXiv:2607.09075](https://arxiv.org/abs/2607.09075).
  Its abstract concerns measurement/gate errors and apparatus-state asymmetry.
  This is adjacent subject matter, not a matching formula for spectral defects.

## Targeted search families

Queries included the following literal combinations and close variants:

- `"skew-symmetric unitary" "matching"`
- `"skew-symmetric" "squared moduli"`
- `"skew-symmetric contractions" matching`
- `"skew symmetric" "contraction" "matching polytope"`
- `"squared" "skew-symmetric" "matching polytope"`
- `"antiunitary" "matching problem"`
- `"antiunitary" "optimization" "matching"`
- `"antiunitary" "Frobenius norm" minimization`
- `"antiunitary" "penalty" "commutator"`
- `"Kramers" "minimum-weight matching"`
- `"Kramers" "Frobenius" distance symmetry`
- `"Kramers degeneracy" "quantitative" theorem`
- `"nearest" "self-dual" "Hermitian" matrix`
- `"skew symmetric" "substochastic" matching`

Search results also led to work on unistochastic matrices and skew contractions
in standard real subspaces. No exact instance of the manuscript's weighted
penalty identity was located. Irrelevant results and search snippets were not
used as mathematical premises.

The repository search covered 472 entries in 17 completed-run promotion files
with exact terms `matching polytope`, `minimum-weight matching`,
`penalty-to-matching`, and `antiunitary matching`, with no matches. A history
query returned no relevant earlier derivation. This establishes the scope of
the search, not absence from every private conversation or document.

## Defensible contribution statement

The manuscript presents an original derivation, relative to the Hypnos record
examined, of the exact weighted penalty-to-matching identity and its stated
consequences. Its broader priority remains subject to specialist literature
review. The parity obstruction, Wigner normal form, Edmonds polytope, and
matching duality are not claimed as new. No novelty claim is based merely on
an unproductive search.

## Addendum, 2026-10-01 (Claude Fable 5.1)

A datedness check on 2026-10-01 (arXiv API and web searches for work posted after
the two reviews) found one adjacent paper: S. Looi, "Stability of isometries of
quantum states", arXiv 2609.37133, posted 2026-09-29. Read in full on
2026-10-01. It proves Hyers-Ulam stability of surjective approximate isometries
of the positive trace-class cone by Wigner symmetries (state side, metric
hypothesis, one approximating conjugation as the conclusion); it contains no
observable, commutation error, square relation, matching or hull lemma. Cited
and distinguished in Section 1 and Section 5.3 of the manuscript; the
reconciliation ledger carries the addendum. Also seen on 2026-10-01 and judged
not adjacent: Liu, Du, Tang, Liu, Eisert and Roth, "Efficient certification of
time-reversal symmetry requires entanglement", arXiv 2610.01555, a
query-complexity result about certifying exact time-reversal symmetry.
