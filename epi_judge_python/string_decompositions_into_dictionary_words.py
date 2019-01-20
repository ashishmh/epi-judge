from test_framework import generic_test
import collections


def find_all_substrings(s, words):
    totalLen = len(words[0]) * len(words)
    answer = []
    for i in range(0, len(s) - totalLen + 1):
        substr = s[i:i+totalLen]
        result = isConstructableFast(substr, words)
        if result:
            answer.append(i)
    return answer


def isConstructable(str, words):
    if str == '' and len(words) == 0:
        return True

    for i, word in enumerate(words):
        if isPrefix(str, word):
            result = isConstructable(str[len(word):], words[0:i] + words[i+1:])
            if result:
                return result
    return False


def isConstructableFast(str, words):
    wordMap = collections.defaultdict(int)
    for word in words:
        wordMap[word] += 1
    strMap = collections.defaultdict(int)
    n = len(words[0])
    for i in range(0, len(str), n):
        substr = str[i:i+n]
        strMap[substr] += 1
    return wordMap == strMap


def isPrefix(str1, str2):
    if len(str2) > len(str1):
        return False

    for i in range(len(str2)):
        if str2[i] != str1[i]:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "string_decompositions_into_dictionary_words.py",
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
