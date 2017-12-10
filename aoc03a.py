#!/usr/bin/python3

import math


def main():
    target = input()

    mem = Memory(Memory.get_size(int(target)))
    l = mem.get_lenght(int(target))
    print(l)


def get_sqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2

    if x*x == n:
        return x


class Memory():
    """Class representing a piece of memory from day 3 advent of code 2017

    Attributes:
        size (int): Size of 2D array grid
        grid (:obj:`list` of :obj:`str`): 2D int array representing the piece of memory
        center (int): x and y coordinate of starting point in the memory (number 1)"""

    def __init__(self, size):

        self.size = size
        self.grid = []*size
        for i in range(size):
            self.grid.append([0]*size)
        self.center = size//2

        self.grid[self.center][self.center] = 1
        next = 2
        for loop in range(1, size//2+1):
            i = self.center + loop - 1
            j = self.center + loop

            while i > self.center - loop:
                self.grid[i][j] = next
                i -= 1
                next += 1

            while j > self.center - loop:
                self.grid[i][j] = next
                next += 1
                j -= 1

            while i < self.center + loop:
                self.grid[i][j] = next
                next += 1
                i += 1

            while j <= self.center + loop:
                self.grid[i][j] = next
                next += 1
                j += 1

    def get_size(target):
        """Method for getting the size of smallest 2D grid in memory that contains the given number

        Args:
            target (int): Number that has to be included in 2D array

        Returns:
            int: size of the smallest 2D grid in memory containing target number"""

        size = 1
        max_num = 1

        while max_num < target:
            size += 2
            max_num = max_num + get_sqrt(max_num)*4 + 4

        return size

    def get_pos(self, target):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == target:
                    return (i, j)

    def get_lenght(self, target):
        i, j = self.get_pos(target)
        start_i, start_j = self.get_pos(1)

        return abs(i-start_i) + abs(j-start_j)


if __name__ == '__main__':
    main()