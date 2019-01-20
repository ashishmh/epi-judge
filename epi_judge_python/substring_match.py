from test_framework import generic_test


def rabin_karp(t, s):
    if len(s) > len(t):
        return -1
    s_len = len(s)
    t_len = len(t)
    s_hash = compute_hash(s)
    t_hash = compute_hash(t[0:s_len])
    if s_hash == t_hash:
        return 0c
    for i in range(t_len - s_len):
        t_hash = remove_hash(t_hash, s_len, t[i])
        t_hash = add_hash(t_hash, t[i + s_len])
        if s_hash == t_hash:
            return i + 1
    return -1


def remove_hash(hash, n, ch):
    mult = 10
    hash -= ord(ch) * (mult ** (n - 1))
    return hash


def add_hash(hash, ch):
    mult = 10
    return hash * mult + ord(ch)


def compute_hash(s):
    hash = 0
    for ch in s:
        hash = add_hash(hash, ch)
    return hash


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("substring_match.py",
                                       'substring_match.tsv', rabin_karp))
