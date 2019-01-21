from test_framework import generic_test


def longest_subarray_with_distinct_entries(A):
    n = len(A)
    max_count = 0
    start = 0
    distinct = set()
    for end in range(0, n):
        if A[end] not in distinct:
            distinct.add(A[end])
        else:
            count = len(distinct)
            max_count = max(max_count, count)
            while A[start] != A[end]:
                distinct.remove(A[start])
                start += 1
            start += 1
    return max(max_count, len(distinct))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
