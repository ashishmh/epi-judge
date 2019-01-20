from test_framework import generic_test


def maximum_revenue(coins):
    # sum is the sum of all elements from start to end inclusive
    def maximum_revenue_inner(start, end, sum, state):
        if start > end:
            return 0
        if state[start][end] is not None:
            return state[start][end]

        sum_left = sum - coins[start]
        pick_left = coins[start] + sum_left - maximum_revenue_inner(start + 1, end, sum_left, state)
        sum_right = sum - coins[end]
        pick_right = coins[end] + sum_right - maximum_revenue_inner(start, end - 1, sum_right, state)
        state[start][end] = max(pick_left, pick_right)
        return state[start][end]

    sum = 0
    n = len(coins)
    for i in range(n):
        sum += coins[i]
    return maximum_revenue_inner(0, n - 1, sum, [[None] * n for _ in range(n)])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
