#!/usr/bin/python3

import fileinput
import re
import math


def main():
    transformations = {}
    grid = ['.#.', '..#', '###']
    iterations = 18

    for line in fileinput.input():
        if line == '\n':
            break

        if line.count('/') == 3:
            split = re.search('(.*)/(.*) => (.*)/(.*)/(.*)', line)
            add_patterns2(transformations, split.group(1)+split.group(2), split.group(3)+split.group(4)+split.group(5))
        else:
            split = re.search('(.*)/(.*)/(.*) => (.*)/(.*)/(.*)/(.*)', line)
            add_patterns3(transformations, split.group(1)+split.group(2)+split.group(3),
                          split.group(4)+split.group(5)+split.group(6)+split.group(7))

    for it in range(iterations):
        if len(grid) % 2 == 0:
            newGrid = ['' for i in range(len(grid) + (len(grid)//2))]
            for i in range(len(grid)//2):
                for j in range(len(grid)//2):
                    sample = grid[i*2][j*2:j*2+2]+grid[i*2+1][j*2:j*2+2]
                    transformed = transformations[sample]
                    newGrid[3*i] += transformed[:3]
                    newGrid[3*i + 1] += transformed[3:6]
                    newGrid[3*i + 2] += transformed[6:]
        else:
            newGrid = ['' for i in range(len(grid) + len(grid)//3)]
            for i in range(len(grid)//3):
                for j in range(len(grid)//3):
                    sample = grid[i*3][j*3:j*3+3]+grid[i*3+1][j*3:j*3+3]+grid[i*3+2][j*3:j*3+3]
                    transformed = transformations[sample]
                    newGrid[4*i] += transformed[:4]
                    newGrid[4*i + 1] += transformed[4:8]
                    newGrid[4*i + 2] += transformed[8:12]
                    newGrid[4*i + 3] += transformed[12:]

        grid = newGrid

    n = 0
    for row in newGrid:
        for pixel in row:
            if pixel == '#':
                n += 1

    print(n)

def add_patterns2(trans, fromp, top):
    for i in range(4):
        fromp = fromp[2]+fromp[0]+fromp[3]+fromp[1]
        trans[fromp] = top


def add_patterns3(trans, f, top):
    for i in range(4):
        f = f[6]+f[3]+f[0]+f[7]+f[4]+f[1]+f[8]+f[5]+f[2]
        trans[f] = top
        trans[f[2]+f[1]+f[0]+f[5]+f[4]+f[3]+f[8]+f[7]+f[6]] = top
        trans[f[6:9]+f[3:6]+f[0:3]] = top


if __name__ == '__main__':
    main()
