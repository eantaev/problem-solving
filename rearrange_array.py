# https://www.interviewbit.com/problems/rearrange-array/


def rearrange_brute_force(d):
    result = []
    for p in d:
        result.append(d[p])
    return result


ORIG_VALUE_MASK = (1 << 16) - 1
NEW_VALUE_MASK = ORIG_VALUE_MASK << 16


def extract_orig_value(p):
    return p & ORIG_VALUE_MASK


def extract_new_value(p):
    return (p & NEW_VALUE_MASK) >> 16


def encode_new_value(p):
    return p << 16


def attach_new_value(orig, new_val):
    return orig | encode_new_value(new_val)


def rearrange(d):
    for i, orig in enumerate(d):
        new_val = d[extract_orig_value(orig)]
        d[i] = attach_new_value(orig, new_val)

    for i, combined in enumerate(d):
        d[i] = extract_new_value(combined)

    return d


assert rearrange_brute_force([1, 0]) == [0, 1]
assert rearrange_brute_force([1, 0, 0, 0]) == [0, 1, 1, 1]

assert rearrange([1, 0]) == [0, 1]
assert rearrange([1, 0, 0, 0]) == [0, 1, 1, 1]
