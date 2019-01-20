from test_framework import generic_test


def number_of_ways_to_top(top, maximum_step):
    def number_of_ways_to_top_inner(j, state):
        if state[j] is not None:
            return state[j]
        if j <= 1:
            state[j] = 1
            return 1

        no_of_ways = 0
        for i in range(1, maximum_step + 1):
            if j - i >= 0:
                no_of_ways += number_of_ways_to_top_inner(j - i, state)
        state[j] = no_of_ways
        return no_of_ways

    cache = [None] * (top + 1)
    return number_of_ways_to_top_inner(top, cache)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_staircase.py",
                                       "number_of_traversals_staircase.tsv",
                                       number_of_ways_to_top))
