#!/usr/bin/python3


def main():
    tape = [0]
    cursor = 0
    state = 'A'
    states = {'A': [[1, True, 'B'], [0, False, 'B']], 'B': [[1, False, 'C'], [0, True, 'E']],
              'C': [[1, True, 'E'], [0, False, 'D']], 'D': [[1, False, 'A'], [1, False, 'A']],
              'E': [[0, True, 'A'], [0, True, 'F']], 'F': [[1, True, 'E'], [1, True, 'A']]}

    for step in range(12683008):
        instruction = states[state][tape[cursor]]
        tape[cursor] = instruction[0]
        if instruction[1]:
            cursor += 1
            if cursor == len(tape):
                tape.append(0)
        else:
            if cursor == 0:
                tape.insert(0, 0)
            else:
                cursor -= 1
        state = instruction[2]

    n = 0
    for i in tape:
        if i == 1:
            n += 1
    print(n)



if __name__ == '__main__':
    main()
