#!/usr/bin/python3

from aoc10b import *
from queue import Queue


def hex(raw_input):
    lenghts = [ord(x) for x in raw_input] + [17, 31, 73, 47, 23]

    l = [x for x in range(256)]
    current = 0
    skip_size = 0

    for round in range(64):
        for lenght in lenghts:
            reverse(l, lenght, current)
            current = (current + lenght + skip_size) % len(l)
            skip_size += 1

    dense = reduce(l)

    out = to_hex(dense)

    return out


def count_used(grid):
    n = 0
    for row in grid:
        for b in row:
            if b == '1':
                n += 1

    return n


def count_regions(grid):
    taken = []

    n = 0

    for row in grid:
        taken.append(128 * [0])

    for i in range(128):
        for j in range(128):
            if grid[i][j] == '1' and taken[i][j] == 0:
                collect_group(grid, taken, i, j)
                n += 1

    return n


def collect_group(grid, taken, i, j):
    q = Queue()
    q.put((i, j))

    while not q.empty():
        curi, curj = q.get()

        taken[curi][curj] = 1

        if curj-1 >= 0:
            if grid[curi][curj-1] == '1' and taken[curi][curj-1] == 0:
                q.put((curi, curj-1))

        if curj+1 < 128:
            if grid[curi][curj+1] == '1' and taken[curi][curj+1] == 0:
                q.put((curi, curj+1))

        if curi-1 >= 0:
            if grid[curi-1][curj] == '1' and taken[curi-1][curj] == 0:
                q.put((curi-1, curj))

        if curi+1 < 128:
            if grid[curi+1][curj] == '1' and taken[curi+1][curj] == 0:
                q.put((curi+1, curj))


inp = input()

scale = 16
nob = 128

grid = []

for i in range(128):
    hash_string = inp + '-' +str(i)
    hexdata = hex(hash_string)
    binary = bin(int(hexdata, scale))[2:].zfill(nob)
    row = [b for b in binary]
    grid.append(row)

print(count_used(grid))
print(grid)
print(count_regions(grid))
