import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reverse_array(arr, i, j):
    if i >= j:
        return
    while i <= j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    n = len(s) - 1
    j = n
    for i in range(n, -1, -1):  # At any point [i + 1 ,j] is the current word under construction
        if s[i] == ' ':
            reverse_array(s, i + 1, j)
            j = i - 1
    reverse_array(s, 0, j)
    reverse_array(s, 0, n)
    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
