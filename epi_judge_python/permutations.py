from test_framework import generic_test, test_utils


def permutations(A):
    if len(A) == 0:
        return [[]]
    if len(A) == 1:
        return [A]
    total_permutation = []
    for i in range(len(A)):
        for arr in permutations(A[0:i] + A[i+1:]):
            arr.insert(0, A[i])
            total_permutation.append(arr)
    return total_permutation


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
