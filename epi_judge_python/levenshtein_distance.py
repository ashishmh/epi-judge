from test_framework import generic_test


def levenshtein_distance(A, B):
    def levenshtein_distance_inner(i, j, state):
        if state[i][j] is not None:
            return state[i][j]
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if A[i] == B[j]:
            state[i][j] = levenshtein_distance_inner(i - 1, j - 1, state)
        else:
            a = levenshtein_distance_inner(i - 1, j, state) + 1
            b = levenshtein_distance_inner(i, j - 1, state) + 1
            c = levenshtein_distance_inner(i - 1, j - 1, state) + 1
            state[i][j] = min(a, b, c)
        return state[i][j]

    state = [[None] * len(B) for _ in range(len(A))]
    return levenshtein_distance_inner(len(A) - 1, len(B) - 1, state)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
