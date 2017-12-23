#!/usr/bin/python3

import fileinput


def main():
    instructions = []
    registers = {}
    for c in 'abcdefgh':
        registers[c] = 0

    for line in fileinput.input():
        if line == '\n':
            break
        instructions.append(line.split())

    nmul = 0
    i = 0
    while i < len(instructions):
        instruction = instructions[i][0]
        first = instructions[i][1]
        if len(instructions[i]) == 3:
            second = instructions[i][2]
            try:
                value = int(second)
            except ValueError:
                if second not in registers:
                    registers[second] = 0
                value = None

        if instruction == 'set':
            if value is not None:
                registers[first] = value
            else:
                registers[first] = registers[second]
        elif instruction == 'sub':
            if value is not None:
                registers[first] -= value
            else:
                registers[first] -= registers[second]
        elif instruction == 'mul':
            nmul += 1
            if value is not None:
                registers[first] *= value
            else:
                registers[first] *= registers[second]
        elif instruction == 'jnz':
            if first in 'abcdefgh':
                if registers[first] != 0:
                    if value is not None:
                        i += value - 1
                    else:
                        i += registers[second] - 1
            else:
                if int(first) != 0:
                    if value is not None:
                        i += value - 1
                    else:
                        i += registers[second] - 1
        i += 1

    print(nmul)


if __name__ == '__main__':
    main()
