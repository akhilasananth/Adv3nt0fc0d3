from typing import List


# The levels are either all increasing or all decreasing.
def is_strictly_increasing(lst: List[int]) -> bool:
    return all(i < j for i, j in zip(lst, lst[1:]))


def is_strictly_decreasing(lst: List[int]) -> bool:
    return all(i > j for i, j in zip(lst, lst[1:]))


# Any two adjacent levels differ by at least one and at most three.
def check_adjacent_level_diff(lst: List[int]) -> bool:
    return all(1 <= abs(j - i) <= 3 for i, j in zip(lst, lst[1:]))


def is_safe(l: List[int]) -> bool:
    return (is_strictly_decreasing(l) or is_strictly_increasing(l)) and check_adjacent_level_diff(l)


def get_safe_reports(lst: List[List[int]]) -> int:
    count = 0
    for l in lst:
        if is_safe(l) or sum([is_safe(l[0:i] + l[i+1:]) for i in range(len(l))]) > 0:
            count += 1

    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = "day2.txt"
    with open(file, "r") as f:
        vals = [list(map(int, line.strip().split(' '))) for line in f]

    print(get_safe_reports(vals))
