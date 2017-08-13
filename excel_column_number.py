def title_to_number(title):
    n = 0
    for c in title:
        n *= 26
        d = ord(c) - ord('A') + 1
        n += d
    return n


assert title_to_number('A') == 1 == (26 ** 0) * 1
assert title_to_number('B') == 2 == (26 ** 0) * 2
assert title_to_number('C') == 3 == (26 ** 0) * 3
assert title_to_number('Z') == 26 == (26 ** 0) * 26

assert title_to_number('AA') == 27 == 1 * (26 ** 1) + 1
assert title_to_number('AB') == 28 == 1 * (26 ** 1) + 2
assert title_to_number('AZ') == 52 == 1 * (26 ** 1) + 26

assert title_to_number('BA') == 2 * (26 ** 1) + (26 ** 0) * 1 == 2 * (26 ** 1) + 1
assert title_to_number('BB') == 2 * (26 ** 1) + (26 ** 0) * 2 == 2 * (26 ** 1) + 2
assert title_to_number('BC') == 2 * (26 ** 1) + (26 ** 0) * 3 == 2 * (26 ** 1) + 3
assert title_to_number('BZ') == 2 * (26 ** 1) + (26 ** 0) * 26 == 2 * (26 ** 1) + 26

assert title_to_number('CA') == 3 * (26 ** 1) + (26 ** 0) * 1

assert title_to_number('DCA') == 4 * (26 ** 2) + 3 * (26 ** 1) + 1 == (4 * 26 + 3) * 26 + 1
assert title_to_number('EDCA') == 5 * (26 ** 3) + 4 * (26 ** 2) + 3 * (26 ** 1) + 1 == ((5 * 26 + 4) * 26 + 3) * 26 + 1
