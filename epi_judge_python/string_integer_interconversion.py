from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):

    return ''


def string_to_int(s):
    n = len(s) - 1
    isNegative = False
    if s[0] == '-':
        isNegative = True
        s = s[1:]
        n -= 1
    sum = 0
    for i, j in zip(range(n, -1, -1), range(n + 1)):
        sum += (ord(s[i]) - 48) * (10 ** j)
    if isNegative:
        return 0 - sum
    else:
        return sum


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
