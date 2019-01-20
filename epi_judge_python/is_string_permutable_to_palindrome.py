from test_framework import generic_test
import collections


def can_form_palindrome(s):
    # TODO - you fill in here.
    count = collections.defaultdict(int)
    for char in s:
        count[char] += 1
    numOdd = 0
    for ele in count.values():
        if ele % 2 != 0:
            numOdd += 1
    if numOdd > 1:
        return False
    else:
        return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
