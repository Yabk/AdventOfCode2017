#!/usr/bin/python3

import fileinput


def main():
    jumps = []
    for line in fileinput.input():
        if (line == 'end\n'):
            break
        jumps.append(int(line))

    print(execute(jumps))


def execute(jumps):
    pc = 0
    steps = 0
    while pc < len(jumps):
        steps += 1
        old_pc = pc
        pc += jumps[pc]
        jumps[old_pc] += 1

    return steps


if __name__ == '__main__':
    main()