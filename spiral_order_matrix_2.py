def spiral(n):
    m = [[0] * n for i in range(n)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0
    segment_length = n - 1
    steps = n * n
    segment_steps = 0
    r, c = 0, 0
    for i in range(1, steps + 1):
        if segment_steps == segment_length:
            segment_steps = 0
            direction_index = (direction_index + 1) % len(directions)
            if direction_index == 0:  # Right
                segment_length -= 2
                c += 1
                r += 1
        m[r][c] = i
        r, c = r + directions[direction_index][0], c + directions[direction_index][1]
        segment_steps += 1
    return m


assert spiral(1) == [[1]]
assert spiral(2) == [[1, 4],
                     [16, 9]]
assert spiral(3) == [[1, 4, 9],
                     [64, 81, 16],
                     [49, 36, 25]]


