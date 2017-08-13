# Given an array of integers find max( |d[i] - d[j]| + |i - j| ) for all 0 <= i, j < d.length

# https://www.interviewbit.com/problems/maximum-absolute-difference/
# You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
# f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
#
# For example,
#
# A=[1, 3, -1]
#
# f(1, 1) = f(2, 2) = f(3, 3) = 0
# f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
# f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
# f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5
#
# So, we return 5.
# See Expected Output


def find_max_manhattan_distance(points):
    def distance(i, j):
        return abs(points[i] - points[j]) + abs(i - j)

    def project_up(point_index, current_index):
        return points[point_index] + current_index - point_index

    def project_down(point_index, current_index):
        return points[point_index] - current_index + point_index

    if not points:
        return 0

    top_index = 0
    bottom_index = 0

    max_distance = 0
    for i, value in enumerate(points):
        top_distance = distance(i, top_index)
        if top_distance > max_distance:
            max_distance = top_distance
            print('top:', top_index, '-', i, ' = ', top_distance)

        bottom_distance = distance(i, bottom_index)
        if bottom_distance > max_distance:
            max_distance = bottom_distance
            print('bottom:', bottom_index, '-', i, ' = ', bottom_distance)

        if project_up(top_index, i) < value:
            top_index = i
            print('top_index = ', i, '(', project_up(top_index, i), ')')
        if project_down(bottom_index, i) > value:
            bottom_index = i
            print('bottom_index = ', i, '(', project_down(bottom_index, i), ')')

    return max_distance


def brute_force_max_manhattan_distance(points):
    def distance(i, j):
        return abs(points[i] - points[j]) + abs(i - j)

    max_distance = 0
    for i, i_val in enumerate(points):
        for j, j_val in enumerate(points):
            d = distance(i, j)
            if d > max_distance:
                max_distance = d
                print(i, j)
    return max_distance


# assert find_max_manhattan_distance([0, 0]) == 1
# assert find_max_manhattan_distance([0, 1]) == 2
# assert find_max_manhattan_distance([0, -1]) == 2
# assert find_max_manhattan_distance([1, 0]) == 2
# assert find_max_manhattan_distance([-1, 0]) == 2
# assert find_max_manhattan_distance([-1, 0, 1]) == 4
# assert find_max_manhattan_distance([-1, 0, -1]) == 2
# assert find_max_manhattan_distance([0, 2, -1]) == 4
# assert find_max_manhattan_distance([1, 3, -1]) == 5
# assert find_max_manhattan_distance([55, -8, 43, 52, 8, 59, -91, -79, -18, -94]) == 158

# 0    1  2   3   4  5    6    7    8    9
# 55, -8, 43, 52, 8, 59, -91, -79, -18, -94

# assert find_max_manhattan_distance(
#     [-54, -48, -43, -2, 16, 16, 78, -5, 60, 58, -92, 62, 81, -89, 26, 89, -70, -48, 18, 76, 38, -39, -2, 59, -41, 66,
#      97, 87, -24, -31, 86, 45, -41, -96, -14, 47, 97, 93, -13, -51, 8, 46, 27, 14, -13, 0, 33, -48, -5, -99]) == 220

assert find_max_manhattan_distance(
    [-54, -48, -43, -2, 16, 16, 78, -5, 60, 58, -92, 62, 81, -89, 26, 89, -70, -48, 18, 76, 38, -39, -2, 59, -41,
     66,
     97, 87, -24, -31, 86, 45, -41, -96, -14, 47, 97, 93, -13, -51, 8, 46, 27, 14, -13, 0, 33, -48, -5, -99]) == 222
