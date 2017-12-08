#!/usr/bin/python3

import fileinput


def main():
    valid = 0

    for line in fileinput.input():
        if (line == 'end\n'):
            break
        if is_valid(line):
            valid += 1

    print(valid)


def is_valid(line):
    words = line.split()

    for i in range (len(words)):
        for j in range (i+1, len(words)):
            if not valid_words(words[i], words[j]):
                return False

    return True


def valid_words(word1, word2):
    dict1 = {}
    dict2 = {}

    for c in word1:
        if c not in dict1:
            dict1[c] = 1
        else:
            dict1[c] += 1

    for c in word2:
        if c not in dict2:
            dict2[c] = 1
        else:
            dict2[c] += 1

    for i in dict1.keys():
        if i not in dict2:
            return True
        elif dict1[i] != dict2[i]:
            return True

    for j in dict2.keys():
        if j not in dict1:
            return True
        elif dict2[j] != dict1[j]:
            return True

    return False


if __name__ == '__main__':
    main()