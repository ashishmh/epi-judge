from test_framework import generic_test, test_utils

dictionary = {0: ['0'], 1: ['1'], 2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'], 5: ['J', 'K', 'L'],
              6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'], 8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}


def phone_mnemonic(phone_number):
    if len(phone_number) == 1:
        return [x for x in dictionary[int(phone_number)]]

    first_num = phone_number[0]
    mnemonic_list = phone_mnemonic(phone_number[1:])
    result = []
    for letter in dictionary[int(first_num)]:
        for mnemonic in mnemonic_list:
            result.append(letter + mnemonic)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
