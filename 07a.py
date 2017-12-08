#!/usr/bin/python3

import fileinput
import re

def main():
    tower = Tower()

    for line in fileinput.input():
        if (line == 'end\n'):
            break

        extracted = re.search('^(.*) \(([0-9]+)\)(.*)', line)
        if (extracted.group(3) == ""):
            tower.add(extracted.group(1), int(extracted.group(2)))
        else:
            tower.add(extracted.group(1), int(extracted.group(2)), extracted.group(3)[4:].split(', '))

    print(tower.get_root())


class Tower:

    def __init__(self):
        self.dict = {}
        self.backtrace = {}
        self.weights = {}
        self.root = None

    def add(self, name, weight, subs = []):
        self.weights[name] = weight
        self.dict[name] = subs

        for sub in subs:
            self.backtrace[sub] = name



    def get_root(self):
        for k, v in self.backtrace.items():
            if (v not in self.backtrace):
                return v


if __name__ == '__main__':
    main()
