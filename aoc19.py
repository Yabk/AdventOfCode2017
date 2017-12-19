#!/usr/bin/python3

import fileinput


def main():
    diagram = []
    letters = []

    for line in fileinput.input():
        if line == '\n':
            break
        diagram.append(line)

    currentx = diagram[0].index('|')
    currenty = 0
    goingDown = True
    goingUp = False
    goingLeft = False
    goingRight = False
    n = 0


    while True:
        n += 1

        if diagram[currenty][currentx] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            letters.append(diagram[currenty][currentx])
            if goingDown and diagram[currenty+1][currentx] == ' ':
                break
            if goingUp and diagram[currenty-1][currentx] == ' ':
                break
            if goingLeft and diagram[currenty][currentx-1] == ' ':
                break
            if goingRight and diagram[currenty][currentx+1] == ' ':
                break

        if goingDown:
            currenty += 1
            if diagram[currenty][currentx] == '+':
                goingDown = False
                if diagram[currenty][currentx-1] not in '|+ ':
                    goingLeft = True
                else:
                    goingRight = True
        elif goingUp:
            currenty -= 1
            if diagram[currenty][currentx] == '+':
                goingUp = False
                if diagram[currenty][currentx-1] not in '|+ ':
                    goingLeft = True
                else:
                    goingRight = True
        elif goingLeft:
            currentx -= 1
            if diagram[currenty][currentx] == '+':
                goingLeft = False
                if diagram[currenty-1][currentx] not in '-+ ':
                    goingUp = True
                else:
                    goingDown = True
        elif goingRight:
            currentx += 1
            if diagram[currenty][currentx] == '+':
                goingRight = False
                if diagram[currenty-1][currentx] not in '-+ ':
                    goingUp = True
                else:
                    goingDown = True

    print(''.join(letters))
    print('steps: {}'.format(n))


if __name__ == '__main__':
    main()
