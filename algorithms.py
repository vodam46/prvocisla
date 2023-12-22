import math
from typing import Callable
import random

from sympy import primerange


# generators
# input: max num
# output: list of primes up to the number (excluding)


def checking(n: int) -> list[int]:
    primes = [2]
    for i in range(3, n, 2):
        for prime in primes:
            if i % prime == 0:
                break
        else:
            primes.append(i)
    return primes


def sieve_eratosthenes(n: int) -> list[int]:
    nums = [True] * n
    primes = []
    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            for j in range(i**2, n, i):
                nums[j] = False

    return primes


def sieve_sundaram_1(n: int) -> list[int]:
    k = (n-1)//2
    nums = [True] * k
    for i in range(1, k):
        j = i
        while (i + j + 2*i*j) < k:
            nums[i + j + 2*i*j] = False
            i += 1

    primes = [2]
    for i in range(1, k):
        if nums[i]:
            primes.append(2*i+1)
    return primes


def sieve_sundaram_2(n: int) -> list[int]:
    # TODO DOESNT WORK
    """
    The sieve of Sundaram is a simple deterministic algorithm for finding
    all the prime numbers up to a specified integer.
    """
    if n < 3:
        if n < 2:
            return []
        else:
            return [2]
    k = (n - 3) // 2 + 1

    integers_list = [True for _ in range(k)]

    for i in range((int(math.sqrt(n)) - 3) // 2 + 1):
        p = 2 * i + 3
        s = (p * p - 3) // 2  # compute cull start

        for j in range(s, k, p):
            integers_list[j] = False

    count = 1
    for i in range(k):
        if integers_list[i]:
            count += 1

    primes = [2]
    for i in range(1, k):
        if integers_list[i]:
            primes.append(2*i+1)
    return primes


def sieve_atkin(n: int) -> list[int]:
    nums = [False] * (n+1)
    for x in range(1, math.isqrt(n)):
        for y in range(1, math.isqrt(n)):
            num = 4*x**2 + y**2
            if num <= n and (num % 12 == 1 or num % 12 == 5):
                nums[num] = not nums[num]
            num = 3*x**2+y**2
            if num <= n and num % 12 == 7:
                nums[num] = not nums[num]
            num = 3*x**2 - y**2
            if x > y and num <= n and num % 12 == 11:
                nums[num] = not nums[num]
    for x in range(5, int(math.sqrt(n))):
        if nums[x]:
            for y in range(x**2, n, x**2):
                nums[y] = False
    return [2, 3] + [prime for prime in range(5, n) if nums[prime]]


generators: list[Callable[[int], list[int]]] = [
    checking,
    sieve_eratosthenes,
    sieve_sundaram_1,
    # sieve_sundaram_2,
    sieve_atkin
]


# checkers
# input: number to check
# output: if prime True else False
def trial(n: int) -> bool:
    return n in checking(n+1)


def lucas_lehmer(p: int) -> bool:
    s = 4
    M = 2**p - 1
    for _ in range(p - 2):
        s = ((s * s) - 2) % M
    if s == 0:
        return True
    else:
        return False


checkers: list[Callable[[int], bool]] = [
    trial
]


def extended_euclid(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    gcd, new_k, new_d = extended_euclid(b, a % b)
    d = new_d
    k = new_k - (a // b) * new_d
    return gcd, d, k


def generate_rsa_keys(p: int, q: int) -> tuple[int, int, int]:
    n = p*q
    phi = math.lcm(p-1, q-1)
    e = 0
    for i in range(2, phi):
        if math.gcd(phi, i) == 1:
            e = i
            break
    d = extended_euclid(e, phi)[1] % ((p-1)*(q-1))
    return n, e, d


def naive_factorize_1(n: int) -> list[int]:
    primes = list(primerange(int(math.sqrt(n)+1)))
    factors = []
    while n != 1:
        if not primes:
            factors.append(n)
            break
        if n % primes[0] == 0:
            factors.append(primes[0])
            n //= primes[0]
        else:
            primes.pop(0)
    return factors


def naive_factorize_2(n: int) -> list[int]:
    primes = [2]
    factors = []
    square_root = int(math.sqrt(n))+1
    while n != 1:
        if primes[-1] >= square_root:
            factors.append(n)
            break
        if n % primes[-1] == 0:
            factors.append(primes[-1])
            n //= primes[-1]
        else:
            i = primes[-1]+1
            while True:
                for prime in primes:
                    if i % prime == 0:
                        break
                else:
                    primes.append(i)
                    break
                i += 1
    return factors


def fermat(n: int) -> list[int]:
    a = math.ceil(math.sqrt(n))
    b2 = a*a - n
    b = int(math.sqrt(b2))
    while b*b != b2:
        a += 1
        b2 = a*a - n
        b = int(math.sqrt(b2))

    return [a-b, a+b]


def pollard_p_minus_1(n: int) -> list[int]:
    B = 10
    g = 1
    primes = primerange(n)
    while B <= 1000000 and g < n:
        a = 2 + random.randint(0, n-3)
        g = math.gcd(a, n)
        if g > 1:
            return [g, n//g]

        for p in primes:
            if p >= B:
                continue
            p_power = 1
            while p_power * p <= B:
                p_power *= p
            a = int(math.pow(a, p_power)) ** n

            g = math.gcd(a-1, n)
            if (g > 1 and g < n):
                return [g, n//g]
        B *= 2
    return []


def f(x: int, c: int, mod: int):
    return ((x*x % mod) + c) % mod


def rho_turtle_hare(n: int, x0: int = 2, c: int = 1) -> list[int]:
    turtle = x0
    hare = x0
    g = 1
    while g == 1:
        turtle = f(turtle, c, n)
        hare = f(f(hare, c, n), c, n)
        g = math.gcd(abs(turtle-hare), n)
    return [g, n//g]


def rho_turtle_hare_brent(n: int, x0: int = 2, c: int = 1) -> list[int]:
    turtle = x0
    hare = f(x0, c, n)
    g = 1

    l = 1

    while g == 1:
        # želva se posune na místo zajíce
        turtle = hare

        # zajíc se posune o l míst
        for _ in range(l):
            hare = f(hare, c, n)

            g = math.gcd(abs(turtle-hare), n)
            if g > 1:
                break
        l *= 2

    return [g, n//g]


def rho_turtle_hare_brent_2(n: int, x0: int = 2, c: int = 1) -> list[int]:
    turtle = x0
    hare = x0
    g = 1

    l = 1
    q = 1
    m = 128
    xs = 1

    while g == 1:
        turtle = hare
        for _ in range(l):
            hare = f(hare, c, n)
        k = 1
        while k < l and g == 1:
            xs = hare
            i = 0
            while i < m and i < l - k:
                hare = f(hare, c, n)
                q = (q * abs(hare - turtle)) % n
                i += 1
            g = math.gcd(q, n)
            k += m
        l *= 2

    if g == n:
        g = 1
        while g == 1:
            xs = f(xs, c, n)
            g = math.gcd(abs(xs-hare), n)

    return [g, n//g]


factors: list[Callable[[int], list[int]]] = [
        naive_factorize_1,
        naive_factorize_2,
        fermat,
        pollard_p_minus_1,
        rho_turtle_hare,
        rho_turtle_hare_brent,
        rho_turtle_hare_brent_2
]
