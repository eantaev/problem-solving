def reversed_number(n):
    assert n >= 0
    r = 0
    while n != 0:
        r *= 10
        r += n % 10
        n //= 10
    return r


def is_palindrome(n):
    if n < 0:
        return False
    if n == 0:
        return True
    return n == reversed_number(n)


assert is_palindrome(0) is True
assert is_palindrome(1) is True
assert is_palindrome(11) is True
assert is_palindrome(1221) is True
assert is_palindrome(122) is False
assert is_palindrome(12121) is True
assert is_palindrome(1212) is False
assert is_palindrome(-1) is False
assert is_palindrome(-121) is False
