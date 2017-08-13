import math


def is_prime(n):
    if n < 2:
        return False
    for d in range(3, int(math.floor(math.sqrt(n))) + 1):
        if n % d == 0:
            return False
    return True


def find_primes_up_to(n):
    if n < 2:
        return []
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for d in range(2, int(math.floor(math.sqrt(n))) + 1):
        if primes[d] and is_prime(d):
            c = 2 * d
            while c <= n:
                primes[c] = False
                c += d
    return [p for p, status in enumerate(primes) if status]


def prime_sum(n):
    primes = find_primes_up_to(n)
    i = 0
    j = len(primes) - 1
    while i <= j:
        s = primes[i] + primes[j]
        if s < n:
            i += 1
        elif s > n:
            j -= 1
        else:
            return [primes[i], primes[j]]
    

assert prime_sum(4) == [2, 2]
assert prime_sum(22) == [3, 19]
