def wave_array(xs):
    sxs = sorted(xs)
    for i in range(0, len(sxs) - 1, 2):
        sxs[i], sxs[i+1] = sxs[i+1], sxs[i]
    return sxs

assert wave_array([1, 2, 3, 4]) == [2, 1, 4, 3]