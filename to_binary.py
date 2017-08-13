def to_binary(n):
    assert n >= 0
    if n == 0:
        return '0'
    assert n > 0
    digits = []
    while n != 0:
        d = n % 2
        n //= 2
        digits.append(str(d))
    return ''.join(reversed(digits))

assert to_binary(0) == '0'
assert to_binary(1) == '1'
assert to_binary(2) == '10'
assert to_binary(3) == '11'
assert to_binary(4) == '100'
assert to_binary(127) == '1111111'
