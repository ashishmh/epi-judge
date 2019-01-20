from test_framework import generic_test


def matrix_search(A, x):
    # TODO - you fill in here.
    n = len(A)
    m = len(A[0])
    i = 0
    j = m-1
    while i < n and j >= 0:
        if x == A[i][j]:
            return True
        if x > A[i][j]:
            i += 1
        else:
            j -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
