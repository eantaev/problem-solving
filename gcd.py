def gcd(a, b):
    assert a >= 0
    assert b >= 0
    if a > b:
        a, b = b, a
    assert 0 <= a <= b
    if b == 0:
        raise ValueError('gcd(0, 0) is undefined')
    while a != 0:
        a, b = b % a, a
    return b

assert gcd(0, 1) == 1
assert gcd(1, 0) == 1
assert gcd(1, 1) == 1
assert gcd(2, 3) == 1
assert gcd(2, 4) == 2
assert gcd(4, 2) == 2
assert gcd(12, 28) == 4