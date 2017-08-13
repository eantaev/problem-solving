def has_noble_integer(xs):
    if not xs:
        return -1

    xs = sorted(xs, reverse=True)

    if xs[0] == 0:
        return 1

    for i in range(1, len(xs)):
        if xs[i] != xs[i - 1] and xs[i] == i:
            print(xs, 'found noble:', xs[i])
            return 1
    return -1


# assert has_noble_integer([]) == -1
# assert has_noble_integer([5, 4, 4, 3, 1]) == 1
# assert has_noble_integer([ 1, 2, 7, 0, 9, 3, 6, 0, 6 ]) == 1
assert has_noble_integer([ -4, -2, 0, -1, -6 ]) == 1