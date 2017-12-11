#/usr/bin/python3

from collections import Counter


def main():
    path = input().split(',')
    print(get_steps(path))

def get_steps(path):
    c = shorten(path)
    n = 0

    for v in c.values():
        n += v

    return n

def shorten(path):
    c = Counter(path)

    remove_opposite(c, 'n', 's')
    remove_opposite(c, 'ne', 'sw')
    remove_opposite(c, 'se', 'nw')

    transform(c, 'n', 'se', 'ne')
    transform(c, 'ne', 's', 'se')
    transform(c, 'se', 'sw', 's')
    transform(c, 's', 'nw', 'sw')
    transform(c, 'sw', 'n', 'nw')
    transform(c, 'nw', 'ne', 'n')
    return c


def remove_opposite(c, side1, side2):
    if (c[side1] > c[side2]):
        c[side1] = c[side1] - c[side2]
        c[side2] = 0
    else:
        c[side2] = c[side2] - c[side1]
        c[side1] = 0

def transform(c, side1, side2, side3):
    n = min(c[side1], c[side2])
    c[side1] -= n
    c[side2] -= n
    c[side3] += n


if __name__ == '__main__':
    main()