#!/usr/bin/python3

import re
import fileinput
import sys


def main():
    cpu = Cpu()
    for line in fileinput.input():
        if (line == 'end\n'):
            break
        cpu.process(line)

    print(cpu.get_max_reg())
    print(cpu.highest_ever)


class Cpu:

    def __init__(self):
        self.registers = {}
        self.highest_ever = -sys.maxsize - 1

    def process(self, line):
        extracted = re.search('^([a-zA-Z]+) ([a-z]+) (.+) if (.*)$', line)

        if not self.eval_cond(extracted.group(4)):
            return

        if extracted.group(1) not in self.registers:
            self.registers[extracted.group(1)] = 0

        if extracted.group(2) == 'inc':
            self.registers[extracted.group(1)] += int(extracted.group(3))
        elif extracted.group(2) == 'dec':
            self.registers[extracted.group(1)] -= int(extracted.group(3))
        else:
            print("Unknown instruction!")

        if self.registers[extracted.group(1)] > self.highest_ever:
            self.highest_ever = self.registers[extracted.group(1)]

    def eval_cond(self, cond):
        extracted = re.search('^([a-zA-Z]+) (.+) (.+)$', cond)

        if extracted.group(1) not in self.registers:
            self.registers[extracted.group(1)] = 0

        if extracted.group(2) == '>':
            return self.registers[extracted.group(1)] > int(extracted.group(3))
        elif extracted.group(2) == '<':
            return self.registers[extracted.group(1)] < int(extracted.group(3))
        elif extracted.group(2) == '>=':
            return self.registers[extracted.group(1)] >= int(extracted.group(3))
        elif extracted.group(2) == '==':
            return self.registers[extracted.group(1)] == int(extracted.group(3))
        elif extracted.group(2) == '<=':
            return self.registers[extracted.group(1)] <= int(extracted.group(3))
        elif extracted.group(2) == '!=':
            return self.registers[extracted.group(1)] != int(extracted.group(3))
        else:
            print("Wrong sign!")

    def get_max_reg(self):
        maxim = -sys.maxsize - 1

        for k, v in self.registers.items():
            if v > maxim:
                maxim = v

        return maxim


if __name__ == '__main__':
    main()