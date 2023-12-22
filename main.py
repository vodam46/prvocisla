#!/usr/bin/env python
from sys import argv
from time import time
import sympy

import algorithms as algs

n: int
debug: bool = False
printing: bool = False
checking: bool = False
generate: bool = False
rsa: bool = False
if "-n" not in argv:
    n = int(input("n: "))
else:
    n = int(argv[argv.index("-n")+1])

if "-d" in argv:
    debug = True

if "-p" in argv:
    printing = True

if "-c" in argv:
    checking = True

if "-r" in argv:
    rsa = True

if "-g" in argv:
    generate = True

print(f"n: {n}")

true_primes = []
if generate or checking or rsa:
    true_primes: list[int] = list(sympy.primerange(1, n))
if printing:
    print(len(true_primes), true_primes)


if generate:
    print("generators:")
    for alg in algs.generators:
        timestart = time()

        primes = alg(n)

        timeend = time()
        totaltime = timeend-timestart

        print(f"{alg.__name__} ({totaltime}) ", end="")
        if printing:
            print(": " + ", ".join([str(p) for p in primes]))
        else:
            print()

        if primes != true_primes:
            print(f"error: {alg.__name__}")
            if len(primes) > len(true_primes):
                print(f"extra: {sorted(list(list(set(primes)-set(true_primes))))}")
            else:
                print(
                    f"missing: {sorted(list(list(set(true_primes)-set(primes))))}"
                )


if checking:
    print("\ncheckers:")
    for alg in algs.checkers:
        timestart = time()

        for num in range(1, n):
            is_in = alg(num)
            if (
                is_in and num not in true_primes
                or not is_in and num in true_primes
            ):
                print(f"{alg.__name__} {num} wrong returned {is_in}")

        timeend = time()
        totaltime = timeend-timestart
        print(f"{alg.__name__} {totaltime}")

if rsa:
    print(
        f"\nRSA encryption: p =  {true_primes[-1]} q = {true_primes[-2]}\n"
        f"(n e d) = {algs.generate_rsa_keys(true_primes[-1], true_primes[-2])}",
    )

print("\nfactorizers")
for factorizer in algs.factors:
    factors = []
    timestart = time()

    try:
        factors = factorizer(n)
    except Exception as e:
        print(e)

    timeend = time()
    totaltime = timeend-timestart

    print(f"{factorizer.__name__} {totaltime} {n}: {' * '.join(map(str,factors))}")
