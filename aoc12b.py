#!/usr/bin/python3

import fileinput
import re
from queue import Queue


def main():
    programs = {}
    for line in fileinput.input():
        if (line == 'end\n'):
            break
        groups = re.search('(.*) <-> (.*)', line)
        neighbors = [int(x) for x in groups.group(2).split(',')]

        programs[int(groups.group(1))] = neighbors

    left = list(programs.keys())
    group = walk(0, programs)[1]
    left = [item for item in left if item not in group]
    n = 1

    while left:
        group = walk(left[0], programs)[1]
        left = [item for item in left if item not in group]
        n += 1
    print(n)


def walk(start, programs):
    n = 0
    group = []

    visited = set()
    q = Queue()
    group.append(start)

    q.put(start)
    visited.add(start)

    while not q.empty():
        current = q.get()
        n += 1

        for neigh in programs[current]:
            if neigh not in visited:
                visited.add(neigh)
                q.put(neigh)
                group.append(neigh)

    return n, group


if __name__ == '__main__':
    main()
