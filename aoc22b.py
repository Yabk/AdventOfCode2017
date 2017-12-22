#!/usr/bin/python3

import fileinput


def main():
    grid = []
    bursts = 10000000

    for line in fileinput.input():
        if line == '\n':
            break
        grid.append(line.split()[0])

    posx = (len(grid)-1)//2
    posy = (len(grid)-1)//2
    up = True
    down = False
    left = False
    right = False

    infections = 0
    for burst in range(bursts):
        if grid[posy][posx] == '#':
            grid[posy] = grid[posy][:posx] + 'F' + grid[posy][posx+1:]
            if up:
                up = False
                right = True
            elif down:
                down = False
                left = True
            elif left:
                left = False
                up = True
            elif right:
                right = False
                down = True
        elif grid[posy][posx] == '.':
            grid[posy] = grid[posy][:posx] + 'W' + grid[posy][posx + 1:]
            if up:
                up = False
                left = True
            elif down:
                down = False
                right = True
            elif left:
                left = False
                down = True
            elif right:
                right = False
                up = True
        elif grid[posy][posx] == 'W':
            grid[posy] = grid[posy][:posx] + '#' + grid[posy][posx + 1:]
            infections += 1
        elif grid[posy][posx] == 'F':
            grid[posy] = grid[posy][:posx] + '.' + grid[posy][posx + 1:]
            if up:
                up = False
                down = True
            elif down:
                down = False
                up = True
            elif left:
                left = False
                right = True
            elif right:
                right = False
                left = True

        if up:
            if posy == 0:
                new_row = '.'*len(grid[0])
                grid.insert(0, new_row)
            else:
                posy -= 1
        elif down:
            posy += 1
            if posy == len(grid):
                new_row = '.'*len(grid[0])
                grid.append(new_row)
        elif left:
            if posx == 0:
                for i in range(len(grid)):
                    grid[i] = '.' + grid[i]
            else:
                posx -= 1
        elif right:
            posx += 1
            if posx == len(grid[0]):
                for i in range(len(grid)):
                    grid[i] += '.'

    print(infections)


if __name__ == '__main__':
    main()
