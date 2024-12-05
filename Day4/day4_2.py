from typing import List

DIRECTIONS = {
    "down_left": (-1, 1),
    "down_right": (1, 1),
    "up_left": (-1, -1),
    "up_right": (1, -1)
}


def is_valid(x: int, y: int, size_x: int, size_y: int) -> bool:
    return 0 <= x < size_x and 0 <= y < size_y


def find_word_in_direction(grid: List[str], n: int, m: int, word: str, x: int, y: int,
                           direction: tuple, index: int = 0) -> bool:
    if index == len(word):
        return True

    if is_valid(x, y, n, m) and word[index] == grid[x][y]:
        return find_word_in_direction(grid, n, m, word, x + direction[0], y + direction[1], direction, index + 1)

    return False


"""
Check M and S positions given A
M.S
.A.
M.S

M.M
.A.
S.S
"""


def check_mas(a_x: int, a_y: int, size_x: int, size_y: int, grid: List[str]) -> bool:
    down_left_x, down_left_y = a_x + DIRECTIONS["down_left"][0], a_y + DIRECTIONS["down_left"][1]
    up_right_x, up_right_y = a_x + DIRECTIONS["up_right"][0], a_y + DIRECTIONS["up_right"][1]

    if is_valid(down_left_x, down_left_y, size_x, size_y) and is_valid(up_right_x, up_right_y, size_x, size_y):
        if grid[down_left_x][down_left_y] == 'M' and grid[up_right_x][up_right_y] == 'S':
            return True
        elif grid[down_left_x][down_left_y] == 'S' and grid[up_right_x][up_right_y] == 'M':
            return True

    return False


def search_word(grid: List[str], word: str) -> int:
    count = 0
    n = len(grid)
    m = len(grid[0])

    assert all([len(s) == m for s in grid])

    # X-MAS
    directions = [DIRECTIONS["down_right"], DIRECTIONS["up_left"]]

    for i in range(n):
        for j in range(m):
            # Check if the first character matches
            if grid[i][j] == word[0]:
                for direction in directions:
                    if (find_word_in_direction(grid, n, m, word, i, j, direction)
                            and check_mas(i+direction[0], j+direction[1], n, m, grid)):
                        count += 1

    return count


if __name__ == '__main__':
    file = "day4.txt"

    with open(file, "r") as f:
        search_space = [s.strip('\n') for s in f.readlines()]

    xmas = "MAS"
    print(search_word(search_space, xmas))
