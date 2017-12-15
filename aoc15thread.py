#!/usr/bin/python3

import threading
import time


def main():
    judge = 0

    la = 5000000 * [0]
    lb = 5000000 * [0]

    gen_a = threading.Thread(target=generator, args=(65, 16807, 4, 5000000, la))
    gen_b = threading.Thread(target=generator, args=(8921, 48271, 8, 5000000, lb))

    start = time.time()

    gen_a.start()
    gen_b.start()

    gen_a.join()
    gen_b.join()

    for i in range(5000000):
        a = la[i]
        b = lb[i]

        if is_good(a, b):
            judge += 1

    end = time.time()

    print(judge)
    print(end - start)


def generator(current, factor, mod, n, l):

    for i in range(n):
        while True:
            current = (current*factor)%2147483647
            if current%mod == 0:
                l[i] = current
                break


def is_good(a, b):
    bin_a = bin(a)[2:].zfill(16)
    bin_b = bin(b)[2:].zfill(16)

    return bin_a[-16:] == bin_b[-16:]


if __name__ == '__main__':
    main()
