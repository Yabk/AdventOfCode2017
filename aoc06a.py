#!/usr/bin/python3


def main():
    raw_input = input()
    blocks = list(map(int, raw_input.split()))
    mem = Memory(blocks)

    print(mem.get_period())


class Memory:

    def __init__(self, blocks):
        self.blocks = blocks
        self.prev_states = set()

    def get_period(self):
        t = 0
        state = ' '.join(map(str, self.blocks))

        while state not in self.prev_states:
            self.prev_states.add(state)
            t += 1

            i = self.get_biggest_block()
            n = self.blocks[i]
            self.blocks[i] = 0

            while n > 0:
                i = (i+1)%len(self.blocks)
                self.blocks[i] += 1
                n -= 1

            state = ' '.join(map(str, self.blocks))

        return t

    def get_biggest_block(self):
        biggest = -1

        for i in range(len(self.blocks)):
            if self.blocks[i] > biggest:
                biggest = self.blocks[i]
                index = i

        return index

if __name__ == '__main__':
    main()