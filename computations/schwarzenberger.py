#!/usr/bin/env python3
"""Exact rank-two Schwarzenberger arithmetic, Python standard library only.

This tests integral virtual K classes, NOT existence of rank-two bundles.
For source/proof/novelty qualifications see arithmetic_findings.md.
Run: python computations/schwarzenberger.py --verify
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from math import isqrt


def valuation(a: int, p: int) -> int:
    if a == 0:
        raise ValueError("valuation(0) is infinite")
    a = abs(a)
    s = 0
    while a % p == 0:
        a //= p
        s += 1
    return s


def primes_up_to(bound: int) -> list[int]:
    if bound < 2:
        return []
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(bound) + 1):
        if sieve[p]:
            sieve[p*p:bound+1:p] = b"\x00" * ((bound-p*p)//p + 1)
    return [p for p in range(2, bound + 1) if sieve[p]]


def prime_factors(a: int) -> list[int]:
    a = abs(a)
    out = []
    p = 2
    while p*p <= a:
        if a % p == 0:
            out.append(p)
            while a % p == 0:
                a //= p
        p += 1 if p == 2 else 2
    if a > 1:
        out.append(a)
    return out


def normalized(c1: int, c2: int) -> tuple[int, int]:
    twist = -((c1 + 1)//2)
    return c1 + 2*twist, c2 + twist*c1 + twist*twist


def newton_coefficients(c1: int, c2: int, n: int) -> list[Fraction]:
    """Coefficients of (1+x)^alpha + (1+x)^beta modulo x^(n+1).

    alpha+beta=c1, alpha*beta=c2. The recurrence is the differential
    equation [(1+x)d/dx]^2 F-c1[(1+x)d/dx]F+c2 F=0.
    """
    b = [Fraction(2)]
    if n == 0:
        return b
    b.append(Fraction(c1))
    for j in range(n-1):
        b.append(-((j+1)*(2*j+1-c1)*b[-1]
                   +(j*j-c1*j+c2)*b[-2])/((j+2)*(j+1)))
    return b


def local_height(c1: int, c2: int, p: int) -> int | None:
    """First j whose Newton coefficient is not p-integral; None = infinity.

    p must be a prime. The formula is exact, including ramification and p=2.
    """
    disc = c1*c1 - 4*c2
    if disc == 0:
        return None
    if p != 2:
        s = valuation(disc, p)
        u = disc // p**s
        if s % 2:
            return 2*p**((s+1)//2)
        if pow(u % p, (p-1)//2, p) == 1:
            return None
        return p**(s//2)*(p+1)
    c1n, c2n = normalized(c1, c2)
    if c1n == -1:
        return 3 if c2n % 2 else None
    d = -c2n
    if d == 0:
        return None
    s = valuation(d, 2)
    if s % 2:
        return 2**((s//2)+2)
    u8 = (d // 2**s) % 8
    if u8 == 1:
        return None
    return (3*2**((s//2)+1) if u8 == 5 else 2**((s//2)+2))


def obstruction_height(c1: int, c2: int) -> tuple[int | None, list[int]]:
    """Global first failed dimension and all primes giving this failure.

    Uses ramified primes and 2 to obtain a finite search bound. Therefore
    does not require a least-inert-prime estimate. Large inputs may require
    a faster factorization/primality backend; trial division is intentional.
    """
    disc = c1*c1 - 4*c2
    if disc >= 0 and isqrt(disc)**2 == disc:
        return None, []
    bad = {2, *prime_factors(disc)}
    upper_bounds = [h for p in bad if (h := local_height(c1, c2, p)) is not None]
    assert upper_bounds, "Every nonsquare integer discriminant has a finite local obstruction"
    upper = min(upper_bounds)
    all_heights = [(p, local_height(c1, c2, p)) for p in primes_up_to(upper)]
    height = min(h for _, h in all_heights if h is not None)
    return height, [p for p, h in all_heights if h == height]


def admissible(c1: int, c2: int, n: int) -> bool:
    return all(h is None or h > n for p in primes_up_to(n)
               for h in [local_height(c1, c2, p)])


def minimum_progression_modulus(c1: int, n: int) -> int:
    """Least M>0 for which every normalized pair (c1, M*t) is admissible.

    c1 must be 0 or -1. This is not the period of the full solution set.
    """
    if c1 not in (0, -1):
        raise ValueError("Use normalized c1=0 or -1")
    if c1 == -1:
        result = 2 if n >= 3 else 1
        for p in primes_up_to(n-1):
            if p != 2:
                result *= p
        return result
    result = 1
    if n >= 4:
        a = 0
        while 2**(a+2) <= n:
            a += 1
        result *= 2**(2*a)
    for p in primes_up_to(n-1):
        if p == 2:
            continue
        exponent = 0
        while True:
            h = (p**(exponent//2)*(p+1) if exponent % 2 == 0
                 else 2*p**((exponent+1)//2))
            if h > n:
                break
            exponent += 1
        result *= p**exponent
    return result


def verify() -> None:
    """Two mathematically different exact calculations, no floating point."""
    count = 0
    max_n = 48
    ps = primes_up_to(max_n)
    for c1 in range(-3, 4):
        for c2 in range(-40, 201):
            coeffs = newton_coefficients(c1, c2, max_n)
            first = next((j for j, b in enumerate(coeffs) if b.denominator != 1), None)
            predicted, _ = obstruction_height(c1, c2)
            assert first == (predicted if predicted is not None and predicted <= max_n else None), (c1, c2, first, predicted)
            for p in ps:
                local_first = next((j for j, b in enumerate(coeffs)
                                    if b.denominator % p == 0), None)
                h = local_height(c1, c2, p)
                assert local_first == (h if h is not None and h <= max_n else None), (c1, c2, p, local_first, h)
            count += 1
    print(f"PASS: {count} Chern pairs; Newton coefficients through n={max_n}; {len(ps)} primes per pair.")
    for c1 in (0, -1):
        for n in range(2, 15):
            m = minimum_progression_modulus(c1, n)
            assert all(admissible(c1, m*t, n) for t in range(-10, 11))
    print("PASS: least-progression formulas sampled at -10 <= t <= 10, 2 <= n <= 14.")
    for n in (5, 6, 7):
        for c1, period in ((0, 12 if n == 5 else 360), (-1, 6 if n == 5 else 90)):
            residues = [c for c in range(period) if admissible(c1, c, n)]
            print(f"n={n} c1={c1} period={period} residues={residues}")
    for c1, c2 in ((0, 3), (0, 20), (0, 180), (-1, 18), (-1, 30)):
        h, p = obstruction_height(c1, c2)
        print(f"c1={c1}, c2={c2}: first failed n={h}, primes={p}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--c1", type=int, default=0)
    ap.add_argument("--c2", type=int, default=20)
    ap.add_argument("--dimension", type=int, default=7)
    args = ap.parse_args()
    if args.verify:
        verify()
    else:
        h, p = obstruction_height(args.c1, args.c2)
        print({"c1":args.c1, "c2":args.c2, "n":args.dimension,
               "numerically_admissible":admissible(args.c1,args.c2,args.dimension),
               "first_failed_dimension":h, "obstructing_primes":p})
