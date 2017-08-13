def binomial(n, k):
    if k == 0:
        return 1
    return step(n, k)[2]


def step(n, k, previous_x=None):
    if previous_x is None:
        previous_x = binomial(n - 1, k - 1)
    x = n * previous_x // k
    return n + 1, k + 1, x


def binomial2(n, k):
    if k > n - k:
        k = n - k
    t = k
    (n, previous_x) = (n - k + 1, 1)
    for k in range(1, t + 1):
        (n, previous_x) = n + 1, (n * previous_x // k)
    return previous_x


assert binomial2(4, 3) == 4
