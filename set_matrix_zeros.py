def set_zeros(d):
    n_rows = len(d)
    if n_rows == 0:
        return
    n_cols = len(d[0])

    first_row_mark = False
    first_col_mark = False

    for r in range(n_rows):
        for c in range(n_cols):
            if d[r][c] == 0:
                # mark row r
                if r == 0:
                    first_row_mark = True
                else:
                    d[r][0] = 0
                # mark col c
                if c == 0:
                    first_col_mark = True
                else:
                    d[0][c] = 0

    # d[0, 0] = 1 # marks are already done. If d[0, 0] was 0 then marks are True, otherwise we don't change it.

    # process the row marks
    for r in range(1, n_rows):
        if d[r][0] == 0:
            for c in range(1, n_cols):
                d[r][c] = 0

    # process the col marks
    for c in range(1, n_cols):
        if d[0][c] == 0:
            for r in range(1, n_rows):
                d[r][c] = 0

    # process first row and col marks
    if first_row_mark:
        for c in range(n_cols):
            d[0][c] = 0

    if first_col_mark:
        for r in range(n_rows):
            d[r][0] = 0

    return d

assert set_zeros([
    [0, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]) == [[0, 0, 0],[0, 1, 1],[0, 1, 1]]
