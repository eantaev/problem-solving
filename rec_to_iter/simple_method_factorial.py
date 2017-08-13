def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


# 1 Study the function.
# 2 Convert all recursive calls into tail calls. (If you can’t, stop. Try another method.)
# 3 Introduce a one-shot loop around the function body.
# 4 Convert tail calls into continue statements.
# 5 Tidy up.

def factorial2(n, acc=1):
    if n < 2:
        return acc * 1
    return factorial2(n - 1, acc * n)


def factorial3(n, acc=1):
    while True:
        if n < 2:
            return acc * 1
        return factorial3(n - 1, acc * n)
        break


def factorial4(n, acc=1):
    while True:
        if n < 2:
            return acc * 1
        (n, acc) = (n - 1, acc * n)


def factorial5(n, acc=1):
    while n > 1:
        (n, acc) = (n - 1, acc * n)
    return acc


def test(factorial_fn):
    assert factorial_fn(2) == 2
    assert factorial_fn(1) == 1
    assert factorial_fn(3) == 6
    assert factorial_fn(4) == 24
    assert factorial_fn(5) == 120


test(factorial)
test(factorial2)
test(factorial3)
test(factorial4)
test(factorial5)