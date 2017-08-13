import math


def is_prime(a):
    if a < 2:
        return False
    for d in range(2, math.floor(math.sqrt(a)) + 1):
        if a % d == 0:
            return False
    return True


assert is_prime(0) == False
assert is_prime(1) == False
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(35) == False
assert is_prime(36) == False
assert is_prime(37) == True
