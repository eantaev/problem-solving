import math


def square_sum(A):
    ans = []
    a = 1
    a2 = 1
    max_a = int(math.floor(math.sqrt(A / 2)))
    while a <= max_a:
        b = a
        b2 = a2
        max_b = int(math.ceil(math.sqrt((A - a2))))
        while b <= max_b:
            if a2 + b2 == A:
                newEntry = [a, b]
                ans.append(newEntry)
            b += 1
            b2 = b * b
        a += 1
        a2 = a * a
    return ans


print(square_sum(2))
assert square_sum(2) == [1, 1]
