#!/usr/bin/python3

import math


def main():
    target = input()

    mem = Memory(Memory.get_size(int(target)), int(target))
    print(mem.size)
    print(mem.first)


def get_sqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2

    if x*x == n:
        return x


class Memory():

    def __init__(self, size, target):
        self.target = target
        self.first = 0
        self.size = size
        self.grid = []*size
        for i in range(size):
            self.grid.append([0]*size)
        self.center = size//2

        self.grid[self.center][self.center] = 1
        for loop in range(1, size//2+1):
            i = self.center + loop - 1
            j = self.center + loop

            while i > self.center - loop:
                self.grid[i][j] = self.get_adj_sum(i, j)
                i -= 1

            while j > self.center - loop:
                self.grid[i][j] = self.get_adj_sum(i, j)
                j -= 1

            while i < self.center + loop:
                self.grid[i][j] = self.get_adj_sum(i, j)
                i += 1

            while j <= self.center + loop:
                self.grid[i][j] = self.get_adj_sum(i, j)
                j += 1

    def get_adj_sum(self, i, j):
        sum = 0

        if j > 0:
            sum += self.grid[i][j-1]
            if i < self.size-1:
                sum += self.grid[i+1][j-1]
            if i > 0:
                sum += self.grid[i-1][j-1]

        if i > 0:
            sum += self.grid[i-1][j]

        if j < self.size-1:
            sum += self.grid[i][j+1]
            if i > 0:
                sum += self.grid[i-1][j+1]
            if i < self.size-1:
                sum += self.grid[i+1][j+1]

        if i < self.size-1:
            sum += self.grid[i+1][j]

        if self.first == 0 and sum > self.target:
            self.first = sum

        return sum

    def get_size(target):
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