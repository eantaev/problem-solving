MAX_INT = 1 << 31


def reversed_integer(n):
    if n < 0:
        is_negative = True
        n = -n
    else:
        is_negative = False

    r = 0
    while r < MAX_INT and n != 0:
        r *= 10
        r += n % 10
        n //= 10
    if r > MAX_INT:
        r = 0
    if is_negative:
        r = -r
    return r

assert reversed_integer(123) == 321
assert reversed_integer(-123) == -321
assert reversed_integer(MAX_INT + 1) == 0
