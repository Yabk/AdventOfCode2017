#!/usr/bin/python3

def main():
    judge = 0
    a_current = 65
    b_current = 8921

    a_factor = 16807
    b_factor = 48271

    for i in range(5000000):
        a_current = next_a(a_current, a_factor)
        b_current = next_b(b_current, b_factor)

        if is_good(a_current, b_current):
            judge += 1

    print(judge)


def is_good(a, b):
    bin_a = bin(a)[2:].zfill(16)
    bin_b = bin(b)[2:].zfill(16)

    return bin_a[-16:] == bin_b[-16:]


def next_a(current, factor):
    while True:
        current = (current*factor)%2147483647
        if current%4 == 0:
            return current


def next_b(current, factor):
    while True:
        current = (current*factor)%2147483647
        if current%8 == 0:
            return current


if __name__ == '__main__':
    main()
