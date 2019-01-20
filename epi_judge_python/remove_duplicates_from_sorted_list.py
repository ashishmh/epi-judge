from test_framework import generic_test


def remove_duplicates(L):
    if not L:
        return 0

    n = len(L)
    i, j = 0, 0
    count = 0
    while i < (n - 1):
        if L[i+1] == L[i]:
            count += 1
            pass
        else:
            L[i], L[j] = L[j], L[i]
            j += 1
        i += 1
    L[i], L[j] = L[j], L[i]

    # while count > 0:
    #     L[n - 1] = 0
    #     n -= 1
    #     count -= 1

    return n - count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
