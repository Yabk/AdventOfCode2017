#!/usr/bin/python3

import os


def main():
    tape = [0]
    cursor = 0
    state = 'A'
    states = {'A': [[1, True, 'B'], [0, False, 'B']], 'B': [[1, False, 'C'], [0, True, 'E']],
              'C': [[1, True, 'E'], [0, False, 'D']], 'D': [[1, False, 'A'], [1, False, 'A']],
              'E': [[0, True, 'A'], [0, True, 'F']], 'F': [[1, True, 'E'], [1, True, 'A']]}

    for step in range(12683008):
        instruction = states[state][tape[cursor]]

        rows, columns = os.popen('stty size', 'r').read().split()
        os.system('clear')
        print('Step:{:8}'.format(step))
        print(tape_part(tape, cursor, int(columns)))
        print('State: ' + state)
        print('Write: '+str(instruction[0]))

        tape[cursor] = instruction[0]
        if instruction[1]:
            print('Going: Right')
            cursor += 1
            if cursor == len(tape):
                tape.append(0)
        else:
            print('Going: Left')
            if cursor == 0:
                tape.insert(0, 0)
            else:
                cursor -= 1
        print('Next state: '+instruction[2])
        state = instruction[2]
        input()


def tape_part(tape, cursor, columns):
    d = (columns-2)//2
    e = (columns-2)%2
    s = ''
    for i in range(cursor-d, cursor+d+e):
        if i == cursor:
            s += '['+str(tape[cursor])+']'
        elif (i < 0) or (i >= len(tape)):
            s += '0'
        else:
            s += str(tape[i])
    return s


if __name__ == '__main__':
    main()

'''
Begin in state A.
Perform a diagnostic checksum after 12683008 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state C.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state E.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state E.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state D.

In state D:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.

In state E:
  If the current value is 0:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state A.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state F.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state E.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
'''