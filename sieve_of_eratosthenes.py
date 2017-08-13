import math


def is_prime(a):
    if a < 2:
        return False
    for d in range(2, math.floor(math.sqrt(a)) + 1):
        if a % d == 0:
            return False
    return True


def find_primes_up_to(n):
    if n < 2:
        return []
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for d in range(2, math.floor(math.sqrt(n)) + 1):
        if is_prime(d):
            c = 2 * d
            while c <= n:
                primes[c] = False
                c += d
    return [p for p, status in enumerate(primes) if status]


assert find_primes_up_to(0) == []
assert find_primes_up_to(1) == []
assert find_primes_up_to(2) == [2]
assert find_primes_up_to(3) == [2, 3]
assert find_primes_up_to(4) == [2, 3]