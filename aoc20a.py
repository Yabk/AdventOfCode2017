#!/usr/bin/python3
#0

import fileinput
import sys
import re


def main():
    min_a = sys.maxsize
    min_i = 0
    i = 0

    for line in fileinput.input():
        if line == '\n':
            break
        split = re.search('p=<(.*),(.*),(.*)>, v=<(.*),(.*),(.*)>, a=<(.*),(.*),(.*)>', line)
        ax = int(split.group(7))
        ay = int(split.group(8))
        az = int(split.group(9))
        a = abs(ax) + abs(ay) + abs(az)

        if a < min_a:
            min_a = a
            min_i = i

        i += 1

    print(min_i)


if __name__ == '__main__':
    main()
