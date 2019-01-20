from test_framework import generic_test
import sys


def find_maximum_subarray(A):
    gsum = -sys.maxsize
    curr_sum = 0

    for i in range(0, len(A)):
        curr_sum += A[i]
        gsum = max(gsum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0

    return max(0, gsum)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_sum_subarray.py",
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
