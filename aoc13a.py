#!/usr/bin/python3

import fileinput
import re


def main():
    layers = []
    depths = []
    positions = []
    going_down = []
    for line in fileinput.input():
        if (line == '\n'):
            break
        groups = re.search('(.*): (.*)', line)
        layers.append(int(groups.group(1)))
        depths.append(int(groups.group(2)))
        positions.append(0)
        going_down.append(True)

    severity = 0

    for i in range(layers[-1]+1):
        if i in layers:
            if scanner_pos(depths[layers.index(i)], i) == 0:
                severity += i * depths[layers.index(i)]

    print(severity)


def scanner_pos(depth, time):
    double_pos = time % ((depth-1) *2)

    if double_pos < depth-1:
        return double_pos
    else:
        return 2*(depth - 1) - double_pos


if __name__ == '__main__':
    main()
