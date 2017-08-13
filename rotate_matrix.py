import math


def rotate(m):
    length = len(m)
    n_iterations = int(math.floor(length / 2))
    v_len = length - 1  # length of vector to copy
    for o in range(n_iterations):
        for i in range(v_len):
            t = m[o + v_len - i][o]
            m[o + v_len - i][o] = m[o + v_len][o + v_len - i]
            m[o + v_len][o + v_len - i] = m[o + i][o + v_len]
            m[o + i][o + v_len] = m[o][o + i]
            m[o][o + i] = t
        v_len -= 2
    return m


assert rotate([[1]]) == [[1]]

assert rotate([[1, 2],
               [3, 4]]) == [[3, 1],
                            [4, 2]]
assert rotate([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]) == [[7, 4, 1],
                               [8, 5, 2],
                               [9, 6, 3]]
