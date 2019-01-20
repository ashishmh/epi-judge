from test_framework import generic_test
import sys


def find_nearest_repetition(paragraph):
    state = dict()
    minDiff = sys.maxsize
    for i, word in enumerate(paragraph):
        if word in state:
            diff = i - state[word]
            minDiff = min(diff, minDiff)
        state[word] = i
    if minDiff == sys.maxsize:
        minDiff = -1
    return minDiff


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
