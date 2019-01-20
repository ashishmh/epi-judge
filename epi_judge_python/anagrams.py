from test_framework import generic_test, test_utils
import collections


def get_char_map(word):
    mapping = {}
    for c in word:
        if c in mapping:
            mapping[c] +=1
        else:
            mapping[c] = 1
    return tuple(sorted(mapping.items()))


def find_anagrams(dictionary):
    state = collections.defaultdict(list)
    for word in dictionary:
        identity = get_char_map(word)
        state[identity].append(word)
    result = [anagrams for anagrams in state.values()]
    return list(filter(lambda x: len(x) > 1, result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
