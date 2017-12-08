#!/usr/bin/python3
#193!!!

import fileinput
import re
from collections import Counter
import queue

def main():
    tower = Tower()

    for line in open('input.txt'):
        if line == 'end\n':
            break

        extracted = re.search('^(.*) \(([0-9]+)\)(.*)', line)
        if extracted.group(3) == "":
            tower.add(extracted.group(1), int(extracted.group(2)))
        else:
            tower.add(extracted.group(1), int(extracted.group(2)), extracted.group(3)[4:].split(', '))

    tower.sum_weights()
    print(tower.get_error())


class Tower:

    def __init__(self):
        self.reversed = []
        self.dict = {}
        self.backtrace = {}
        self.weights = {}
        self.summed_weights = {}
        self.root = None
        self.n = 0

    def add(self, name, weight, subs = []):
        self.weights[name] = weight
        self.summed_weights[name] = weight
        self.dict[name] = subs
        self.n += 1

        for sub in subs:
            self.backtrace[sub] = name

    def get_root(self):
        for k, v in self.backtrace.items():
            if v not in self.backtrace:
                self.root = v
                return v

    def sum_weights(self):

        if self.root is None:
            self.get_root()

        q = queue.Queue()
        q.put(self.root)

        while not q.empty():
            current = q.get()
            self.reversed.append(current)
            for node in self.dict[current]:
                q.put(node)

        self.reversed.reverse()

        for node in self.reversed:
            for subnode in self.dict[node]:
                self.summed_weights[node] += self.summed_weights[subnode]

    def get_error(self):

        for node in self.reversed:
            if not self.is_balanced(node)[0]:
                return self.is_balanced(node)[1]

    def is_balanced(self, node):
        if node not in self.dict:
            return True, 0

        l = [self.summed_weights[x] for x in self.dict[node]]
        if all_same(l):
            return True, 0

        c = Counter(l)
        right_value = c.most_common()[0][0]
        wrong_value = c.most_common()[1][0]

        for subnode in self.dict[node]:
            if self.summed_weights[subnode] == wrong_value:
                return False, (right_value - wrong_value + self.weights[subnode])

        print(node)
        return True, 0


def all_same(items):
    return all(x == items[0] for x in items)


if __name__ == '__main__':
    main()
