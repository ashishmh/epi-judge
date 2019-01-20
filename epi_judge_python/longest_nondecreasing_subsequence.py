from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A):
    n = len(A)
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if A[i] >= A[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
