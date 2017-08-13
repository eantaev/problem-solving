def max_nn_subarray(vs):
    max_start = 0
    max_end = 0
    max_sum = 0

    start = 0
    current_sum = 0
    i = 0
    input_length = len(vs)
    # Inv: vs[max_start:max_end] is a result for input vs[:i]
    # Inv: vs[start:i] is a candidate solution (i.e. has no negative elements)
    # Inv: sum(vs[start:i]) = current_sum
    # Check Inv
    while i <= input_length:
        if i == input_length or vs[i] < 0:
            if (current_sum > max_sum
                or (current_sum == max_sum
                    and max_end - max_start < i - start)):
                max_start = start
                max_end = i
                max_sum = current_sum
            start = i + 1
            current_sum = 0
        else:
            current_sum += vs[i]
        # Check Inv
        i += 1
    return vs[max_start:max_end]


# assert max_nn_subarray([]) == []
# assert max_nn_subarray([-1, -2]) == []
print(max_nn_subarray([1, 2, 3]))
assert max_nn_subarray([1, 2, 3]) == [1, 2, 3]
assert max_nn_subarray([1, 2, -1, 3]) == [1, 2]
assert max_nn_subarray([1, 2, 5, -7, 2, 3]) == [1, 2, 5]
assert max_nn_subarray([1, 2, 5, -7, 2, 3, 1, 2]) == [2, 3, 1, 2]
assert max_nn_subarray([-1, 1, 2, 5, 0, -7, 2, 3, 1, 2]) == [1, 2, 5, 0]
