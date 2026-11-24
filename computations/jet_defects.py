#!/usr/bin/env python3
"""Exact rational matrix check of hyperplane jet defects in monomial CIs.

A=Q[x0,x1,x2,x3]/(x0^d,...,x3^d), h=x0+...+x(q-1), M=A(d).
For each t and k this constructs multiplication matrices and computes
  D_k(t)=dim ker(h:A_(t+d-1)->A_(t+d))
       -dim ker(h^(k+1):A_(t+d-k-1)->A_(t+d))
       +dim ker(h^k:A_(t+d-k-1)->A_(t+d-1)).
No sl2 decomposition is used in the matrix computation.
Python standard library only; exact integer row operations preserve Q-rank.
Run --verify for d=1..4, q=1..4, k=1..first_failure+1, all graded pieces.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import product
from math import factorial, gcd


def rank_over_q(matrix: list[list[int]]) -> int:
    """Fraction-free Gaussian elimination with primitive integer rows."""
    if not matrix:
        return 0
    rows = [list(row) for row in matrix]
    cols = len(rows[0])
    pivot_row = 0
    for column in range(cols):
        pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        divisor = 0
        for value in rows[pivot_row][column:]:
            divisor = gcd(divisor, value)
        if divisor > 1:
            rows[pivot_row] = [v//divisor for v in rows[pivot_row]]
        leading = rows[pivot_row][column]
        for i in range(pivot_row+1, len(rows)):
            coefficient = rows[i][column]
            if not coefficient:
                continue
            common = gcd(leading, coefficient)
            a, b = leading//common, coefficient//common
            rows[i] = [a*u-b*v for u, v in zip(rows[i], rows[pivot_row])]
            divisor = 0
            for value in rows[i][column+1:]:
                divisor = gcd(divisor, value)
            if divisor > 1:
                rows[i] = [v//divisor for v in rows[i]]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


@lru_cache(maxsize=None)
def monomials(d: int, degree: int) -> tuple[tuple[int, ...], ...]:
    if degree < 0 or degree > 4*(d-1):
        return ()
    return tuple(a for a in product(range(d), repeat=4) if sum(a) == degree)


@lru_cache(maxsize=None)
def power_terms(q: int, k: int) -> tuple[tuple[tuple[int, ...], int], ...]:
    """Multinomial expansion of (x0+...+x(q-1))^k."""
    out = []
    for a in product(range(k+1), repeat=q):
        if sum(a) != k:
            continue
        coefficient = factorial(k)
        for ai in a:
            coefficient //= factorial(ai)
        out.append((a+(0,)*(4-q), coefficient))
    return tuple(out)


@lru_cache(maxsize=None)
def multiplication_rank(d: int, q: int, k: int, source_degree: int) -> int:
    source = monomials(d, source_degree)
    target = monomials(d, source_degree+k)
    if not source or not target:
        return 0
    index = {a:i for i,a in enumerate(target)}
    matrix = [[0]*len(source) for _ in target]
    for column, a in enumerate(source):
        for increment, coefficient in power_terms(q, k):
            b = tuple(ai+bi for ai,bi in zip(a,increment))
            if all(bi < d for bi in b):
                matrix[index[b]][column] += coefficient
    return rank_over_q(matrix)


def defect(d: int, q: int, k: int) -> dict[int, int]:
    out = {}
    for t in range(1-d, 3*(d-1)+1):
        degree = t+d-1
        source_degree = degree-k
        value = (len(monomials(d, degree))
                 -multiplication_rank(d,q,1,degree)
                 -multiplication_rank(d,q,k,source_degree)
                 +multiplication_rank(d,q,k+1,source_degree))
        if value < 0:
            raise AssertionError((d,q,k,t,value))
        if value:
            out[t] = value
    return out


def polynomial_power(coefficients: list[int], exponent: int) -> list[int]:
    out = [1]
    for _ in range(exponent):
        next_out = [0]*(len(out)+len(coefficients)-1)
        for i,a in enumerate(out):
            for j,b in enumerate(coefficients):
                next_out[i+j] += a*b
        out = next_out
    return out


def predicted_defect(d: int, q: int, k: int) -> dict[int, int]:
    """Closed Jordan-count formula, independent of matrix construction."""
    active = polynomial_power([1]*d, q)
    inactive = polynomial_power([1]*d, 4-q)
    socle = q*(d-1)
    out = {}
    for i in range(socle//2+1):
        block_length = socle-2*i+1
        if block_length > k:
            continue
        multiplicity = active[i]-(active[i-1] if i else 0)
        if not multiplicity:
            continue
        degree = socle-i-d+1
        for j, coefficient in enumerate(inactive):
            if coefficient:
                out[degree+j] = out.get(degree+j,0)+multiplicity*coefficient
    return out


def first_failure(d: int, q: int) -> int:
    if q == 1:
        return d
    return 2 if q == 3 and d % 2 == 0 else 1


def first_defect_table(d: int, q: int) -> dict[int, int]:
    if q == 1:
        coefficients, shift, scale = polynomial_power([1]*d,3), 0, 1
    elif q == 2:
        coefficients, shift, scale = polynomial_power([1]*d,2), 0, 1
    elif q == 3 and d % 2:
        coefficients, shift, scale = [1]*d, (d-1)//2, 1
    elif q == 3:
        coefficients, shift, scale = [1]*d, d//2, 2
    else:
        coefficients, shift, scale = [1], d-1, d
    return {j+shift:scale*c for j,c in enumerate(coefficients) if c}


def verify() -> None:
    pairs = 0
    for d in range(1,5):
        for q in range(1,5):
            first = first_failure(d,q)
            for k in range(1,first+2):
                actual = defect(d,q,k)
                assert actual == predicted_defect(d,q,k), (d,q,k,actual,predicted_defect(d,q,k))
                if k < first:
                    assert actual == {}, (d,q,k,actual)
                elif k == first:
                    assert actual == first_defect_table(d,q), (d,q,k,actual,first_defect_table(d,q))
                pairs += 1
            print(f"d={d}, q={q}: first={first}, defect={first_defect_table(d,q)}")
    print(f"PASS: {pairs} (d,q,k) cases; all graded pieces; exact Q matrix ranks.")
    print(f"Distinct multiplication ranks computed: {multiplication_rank.cache_info().currsize}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--d", type=int, default=3)
    ap.add_argument("--q", type=int, choices=range(1,5), default=4)
    ap.add_argument("--k", type=int, default=1)
    args = ap.parse_args()
    if args.verify:
        verify()
    else:
        if args.d < 1 or args.k < 1:
            ap.error("d and k must be positive")
        print(defect(args.d,args.q,args.k))
