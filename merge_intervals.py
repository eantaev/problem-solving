class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


def intersect(int0, int1):
    if int0.start > int1.start:
        int0, int1 = int1, int0
    # int0.start <= int1.start
    return int1.start <= int0.end


def find_instersections(intervals, new_interval):
    f_id = -1
    l_id = -1
    for index, interval in enumerate(intervals):
        if intersect(interval, new_interval):
            l_id = index
            if f_id == -1:
                f_id = index
    return (f_id, l_id)


def find_insertion_index(intervals, new_interval):
    for i, interval in enumerate(intervals):
        if new_interval.end < interval.start:
            return i
    return len(intervals)


def merge(intervals, new_interval):
    if not intervals:
        return [new_interval]
    f_id, l_id = find_instersections(intervals, new_interval)
    if f_id == -1:
        insertion_point = find_insertion_index(intervals, new_interval)
        return intervals[:insertion_point] + [new_interval] + intervals[insertion_point:]
    new_interval = Interval(min(new_interval.start, intervals[f_id].start),
                    max(new_interval.end, intervals[l_id].end))
    return intervals[:f_id] + [new_interval] + intervals[l_id + 1:]


assert intersect(Interval(0, 2), Interval(0, 1))
assert intersect(Interval(0, 2), Interval(1, 2))
assert intersect(Interval(0, 2), Interval(2, 3))
assert intersect(Interval(2, 3), Interval(0, 2))
assert not intersect(Interval(0, 2), Interval(3, 4))

assert find_instersections([Interval(0, 1), Interval(4, 5)], new_interval=Interval(2, 3)) == (-1, -1)
assert find_instersections([Interval(0, 1), Interval(4, 5)], new_interval=Interval(1, 3)) == (0, 0)
assert find_instersections([Interval(0, 1), Interval(4, 5)], new_interval=Interval(1, 4)) == (0, 1)
assert find_instersections([Interval(0, 1), Interval(4, 5)], new_interval=Interval(4, 6)) == (1, 1)

print(merge([Interval(0, 1), Interval(4, 5)], new_interval=Interval(2, 3)))

assert merge([Interval(0, 1), Interval(4, 5)], new_interval=Interval(2, 3)) == [Interval(0, 1), Interval(2, 3), Interval(4, 5)]
assert merge([Interval(0, 1), Interval(4, 5)], new_interval=Interval(1, 3)) == [Interval(0, 3), Interval(4, 5)]
assert merge([Interval(0, 1), Interval(4, 5)], new_interval=Interval(2, 4)) == [Interval(0, 1), Interval(2, 5)]
assert merge([Interval(0, 1), Interval(4, 5)], new_interval=Interval(1, 4)) == [Interval(0, 5)]
assert merge([Interval(0, 1), Interval(4, 5)], new_interval=Interval(-1, 4)) == [Interval(-1, 5)]
