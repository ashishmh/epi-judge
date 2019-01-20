from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    i, j, k = 0, 0, -1
    n1 = len(A)
    n2 = len(B)
    result = []
    while i < n1 and j < n2:
        if A[i] == B[j]:
            if k == -1 or result[k] != A[i]:
                result.append(A[i])
                k += 1
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
