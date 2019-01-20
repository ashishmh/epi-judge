from test_framework import generic_test


def number_of_ways(n, m):
    def number_of_ways_inner(x, y, state):
        if state[x][y] is not None:
            return state[x][y]
        if x == 0 or y == 0:
            state[x][y] = 1
            return 1

        state[x][y] = 0
        if x - 1 >= 0:
            state[x][y] += number_of_ways_inner(x - 1, y, state)
        if y - 1 >= 0:
            state[x][y] += number_of_ways_inner(x, y - 1, state)

        return state[x][y]

    state = [[None] * m for _ in range(n)]
    return number_of_ways_inner(n - 1, m - 1, state)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
