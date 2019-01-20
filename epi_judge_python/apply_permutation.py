from test_framework import generic_test


def apply_permutation(perm, A):
    n = len(A)
    if n == 1:
        return

    # state = [False] * n
    start = perm[0]
    i = 0
    while :
        temp = (A[perm[i]], perm[i])
        A[perm[i]] = A[i]
        # state[perm[i]] = True
        i = temp[1]

    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    #return A

    return max(0, l_max_wt_path, r_max_wt_path) + root.val, max(path_through_me, l_max_wt_dia, r_max_wt_dia)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
