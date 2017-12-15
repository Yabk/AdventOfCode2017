#!/usr/bin/python3


def main():
    judge = 0
    a_current = 703
    b_current = 516

    a_factor = 16807
    b_factor = 48271

    for i in range(40000000):
        a_current = next(a_current, a_factor)
        b_current = next(b_current, b_factor)

        if is_good(a_current, b_current):
            judge += 1

    print(judge)


def is_good(a, b):
    bin_a = bin(a)[2:].zfill(16)
    bin_b = bin(b)[2:].zfill(16)

    return bin_a[-16:] == bin_b[-16:]

def next(current, factor):
    return (current*factor)%2147483647


if __name__ == '__main__':
    main()
