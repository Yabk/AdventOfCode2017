#!/usr/bin/python3

import threading
from queue import Queue


def main():
    judge = 0
    qa = Queue()
    qb = Queue()

    gen_a = threading.Thread(target=generator, args=(65, 16807, 4, 5000000, qa))
    gen_b = threading.Thread(target=generator, args=(8921, 48271, 8, 5000000, qb))

    gen_a.start()
    gen_b.start()

    for i in range(5000000):
        a = qa.get()
        b = qb.get()

        if is_good(a, b):
            judge += 1

    gen_a.join()
    gen_b.join()

    print(judge)


def generator(current, factor, mod, n, q):

    for i in range(n):
        while True:
            current = (current*factor)%2147483647
            if current%mod == 0:
                q.put(current)
                break


def is_good(a, b):
    bin_a = bin(a)[2:].zfill(16)
    bin_b = bin(b)[2:].zfill(16)

    return bin_a[-16:] == bin_b[-16:]


if __name__ == '__main__':
    main()
