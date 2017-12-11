# /usr/bin/python3

import aoc11a

def main():
    path = input().split(',')
    smaller = []

    max_distance = 0

    for step in path:
        smaller.append(step)
        n = aoc11a.get_steps(smaller)
        if n > max_distance:
            max_distance = n

    print(max_distance)


if __name__ == '__main__':
    main()