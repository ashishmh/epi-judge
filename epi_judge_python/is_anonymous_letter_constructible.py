from test_framework import generic_test
import collections


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here.
    letter_text = collections.Counter(letter_text)
    magazine_text = collections.Counter(magazine_text)
    for char in letter_text.keys():
        if magazine_text[char] == 0 or magazine_text[char] < letter_text[char]:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
