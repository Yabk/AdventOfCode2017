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

    print(walk(0, programs))


def walk(start, programs):
    n = 0

    visited = set()
    q = Queue()

    q.put(start)
    visited.add(start)

    while not q.empty():
        current = q.get()
        n += 1

        for neigh in programs[current]:
            if neigh not in visited:
                visited.add(neigh)
                q.put(neigh)

    return n


if __name__ == '__main__':
    main()
