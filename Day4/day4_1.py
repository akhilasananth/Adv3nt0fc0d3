"""
Directions: horizontal, vertical, diagonal, written backwards, or even overlapping other words
        x   y
right   1   0
left    -1  0
up      0   1
down    0   -1
upleft  -1  1
upright 1   1
downleft    -1  -1
downright   1   -1
"""
from typing import List


def is_valid(x: int, y: int, size_x: int, size_y: int) -> bool:
    return 0 <= x < size_x and 0 <= y < size_y


def find_word_in_direction(grid: List[str], n: int, m: int, word: str, x: int, y: int,
                           dir_x: int, dir_y: int, index: int = 0) -> bool:
    if index == len(word):
        return True

    if is_valid(x, y, n, m) and word[index] == grid[x][y]:
        return find_word_in_direction(grid, n, m, word, x + dir_x, y + dir_y, dir_x, dir_y, index + 1)

    return False


def search_word(grid: List[str], word: str) -> int:
    count = 0
    n = len(grid)
    m = len(grid[0])

    assert all([len(s) == m for s in grid])

    # Directions for 8 possible movements
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(n):
        for j in range(m):

            # Check if the first character matches
            if grid[i][j] == word[0]:
                for dir_x, dir_y in directions:
                    if find_word_in_direction(grid, n, m, word, i, j, dir_x, dir_y):
                        count += 1

    return count


if __name__ == '__main__':
    file = "day4.txt"

    with open(file, "r") as f:
        search_space = [s.strip('\n') for s in f.readlines()]

    xmas = "XMAS"
    print(search_word(search_space, xmas))
