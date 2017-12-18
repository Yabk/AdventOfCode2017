#!/usr/bin/python3

import fileinput


def main():
    instructions = []
    registers = {}

    for line in fileinput.input():
        if line == '\n':
            break
        instructions.append(line.split())

    i = 0
    first_recovered = None
    last_sound = None
    while i < len(instructions):
        instruction = instructions[i][0]
        first = instructions[i][1]
        if first not in registers:
            registers[first] = 0
        if len(instructions[i]) == 3:
            second = instructions[i][2]
            try:
                value = int(second)
            except ValueError:
                if second not in registers:
                    registers[second] = 0
                value = None

        if instruction == 'snd':
            last_sound = registers[first]
        elif instruction == 'set':
            if value is not None:
                registers[first] = value
            else:
                registers[first] = registers[second]
        elif instruction == 'add':
            if value is not None:
                registers[first] += value
            else:
                registers[first] += registers[second]
        elif instruction == 'mul':
            if value is not None:
                registers[first] *= value
            else:
                registers[first] *= registers[second]
        elif instruction == 'mod':
            if value is not None:
                registers[first] %= value
            else:
                registers[first] %= registers[second]
        elif instruction == 'rcv':
            if first_recovered is None:
                first_recovered = last_sound
                i = len(instructions)
        elif instruction == 'jgz' and registers[first] > 0:
            if value is not None:
                i += value - 1
            else:
                i += registers[second] - 1
        i += 1

    print(first_recovered)
    

if __name__ == '__main__':
    main()
