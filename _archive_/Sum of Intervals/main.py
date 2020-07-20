from functools import reduce
from itertools import combinations


def sum_of_intervals(intervals):
    # crossing elements concatenation
    while True:
        print(intervals)
        not_clean = False
        for a, b in combinations(intervals, 2):
            print(f'{a} - {b}')
            if a[1] >= b[0] and a[0] <= b[1]:
                intervals.append((min(a[0], b[0]), max(a[1], b[1])))
                intervals.remove(a)
                intervals.remove(b)
                not_clean = True
                break

        if not not_clean:
            break

    return reduce(lambda x, y: x + y[1] - y[0], intervals, 0)


if __name__ == '__main__':
    print(sum_of_intervals([(1, 4), (10, 11), (2, 5),
                            (11, 12), (3, 6), (12, 13)]))
