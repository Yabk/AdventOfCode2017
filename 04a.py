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
            if words[i] == words[j]:
                return False

    return True


if __name__ == '__main__':
    main()