"""Exact Fraction-arithmetic controls, independent of scientific libraries."""
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parent
RNG = random.Random(20260929)


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def add(a, b, scale=Q(1)):
    return [[x + scale*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def multiply(a, b):
    bt = transpose(b)
    return [[sum(x*y for x, y in zip(ar, bc)) for bc in bt] for ar in a]


def inverse(a):
    n = len(a)
    rows = [list(ar) + er for ar, er in zip(a, eye(n))]
    for k in range(n):
        pivot = next(i for i in range(k, n) if rows[i][k])
        rows[k], rows[pivot] = rows[pivot], rows[k]
        denom = rows[k][k]
        rows[k] = [v/denom for v in rows[k]]
        for i in range(n):
            if i != k:
                factor = rows[i][k]
                rows[i] = [v-factor*w for v, w in zip(rows[i], rows[k])]
    return [r[n:] for r in rows]


def norm_squared(a):
    return sum(x*x for row in a for x in row)


def all_matchings(vertices):
    if not vertices:
        yield ()
        return
    i, *rest = vertices
    for m in all_matchings(rest):
        yield m
    for j in rest:
        for m in all_matchings([k for k in rest if k != j]):
            yield ((i, j),) + m


def main():
    exact_cases = stability_cases = odd_checks = 0
    ties = 0
    maximum_denominator_bits = 0
    for n in range(1, 8):
        for case in range(10):
            a = [[Q(0) for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(i+1, n):
                    a[i][j] = Q(RNG.randint(-5, 5), 7)
                    a[j][i] = -a[i][j]
            u = multiply(add(eye(n), a, -1), inverse(add(eye(n), a)))
            assert multiply(u, transpose(u)) == eye(n)
            maximum_denominator_bits = max(maximum_denominator_bits,
                max(x.denominator.bit_length() for row in u for x in row))
            s = [[x/2 for x in row] for row in add(u, transpose(u))]
            k = [[x/2 for x in row] for row in add(u, transpose(u), -1)]
            assert norm_squared(s) + norm_squared(k) == n
            defect = norm_squared(add(multiply(u, u), eye(n)))
            assert defect == 4 * norm_squared(s)
            for size in range(1, n+1, 2):
                for subset in itertools.combinations(range(n), size):
                    mass = sum(k[i][j]**2 for i in subset for j in subset if i < j)
                    assert mass <= Q(size-1, 2)
                    odd_checks += 1
            c = [[Q(0) for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(i+1, n):
                    c[i][j] = c[j][i] = Q(RNG.randint(1, 20), 3)
            for tau in (Q(0), Q(2, 3), Q(13, 3)):
                energy = sum(c[i][j]*u[i][j]**2 for i in range(n) for j in range(n)) + tau*defect
                affine = 4*tau*n + 2*sum((c[i][j]-4*tau)*k[i][j]**2
                                         for i in range(n) for j in range(i+1, n))
                remainder = 2*sum(c[i][j]*s[i][j]**2 for i in range(n) for j in range(i+1, n))
                assert energy == affine + remainder
                costs = sorted((2*sum(c[i][j] for i, j in m)+4*tau*(n-2*len(m)), m)
                               for m in all_matchings(list(range(n))))
                optimum, matching = costs[0]
                assert energy >= optimum
                witness = eye(n)
                for i, j in matching:
                    witness[i][i] = witness[j][j] = Q(0)
                    witness[i][j], witness[j][i] = Q(1), Q(-1)
                w_energy = sum(c[i][j]*witness[i][j]**2 for i in range(n) for j in range(n))
                w_energy += tau*norm_squared(add(multiply(witness, witness), eye(n)))
                assert w_energy == optimum
                if len(costs) > 1 and costs[1][0] > optimum:
                    delta = costs[1][0] - optimum
                    error = energy - optimum
                    mass_error = sum(abs(k[i][j]**2 - Q((i, j) in matching))
                                     for i in range(n) for j in range(i+1, n))
                    assert mass_error <= n*error/delta
                    c_min = min(c[i][j] for i in range(n) for j in range(i+1, n))
                    s_off = sum(s[i][j]**2 for i in range(n) for j in range(n) if i != j)
                    assert s_off <= error/c_min
                    stability_cases += 1
                elif len(costs) > 1:
                    ties += 1
                exact_cases += 1
    report = {"arithmetic": "Python fractions.Fraction, exact; real orthogonal subset only",
              "seed": 20260929, "dimensions": [1, 7], "objective_cases": exact_cases,
              "odd_set_checks": odd_checks, "stability_cases": stability_cases,
              "tied_matching_cases_excluded_from_gap_estimate": ties,
              "max_unitary_entry_denominator_bits": maximum_denominator_bits,
              "failures": 0,
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT / "verification-exact.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
