from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    n = len(partial_assignment)

    # check valid rows
    for i in range(n):
        visited = set()
        for j in range(n):
            num = partial_assignment[i][j]
            if num == 0:
                continue
            if num in visited:
                return False
            visited.add(num)

    # check valid columns
    for j in range(n):
        visited = set()
        for i in range(n):
            num = partial_assignment[i][j]
            if num == 0:
                continue
            if num in visited:
                return False
            visited.add(num)

    # check valid 3x3 grid
    for i in range(0, n, 3):
        for j in range(0, n, 3):
            if not check_valid_grid(partial_assignment, i, j):
                return False

    return True


def check_valid_grid(grid, n, m):
    visited = set()
    for i in range(n, n + 3):
        for j in range(m, m + 3):
            num = grid[i][j]
            if num == 0:
                continue
            if num in visited:
                return False
            visited.add(num)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
