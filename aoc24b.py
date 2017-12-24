#!/usr/bin/python3

import fileinput


class Component:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.sum = side1 + side2

    def __lt__(self, other):
        return self.sum < other.sum

    def has(self, n):
        return (self.side1 == n) or (self.side2 == n)


def main():
    components = []
    for line in fileinput.input():
        if line == '\n':
            break
        data = line.split('/')
        components.append(Component(int(data[0]), int(data[1])))

    bridge = []
    current = 0

    print(buildrec(components, current, bridge))


def buildrec(components, current, bridge):
    stack = []
    for comp in components:
        if comp.has(current) and comp not in bridge:
            stack.append(comp)

    if len(stack) == 0:
        brigde_sum = 0
        for comp in bridge:
            brigde_sum += comp.sum
        return len(bridge), brigde_sum

    l_max = 0
    s_max = 0
    while len(stack) > 0:
        new = stack.pop()
        if new.side1 != current:
            next_value = new.side1
        else:
            next_value = new.side2
        bridge.append(new)
        l, s = buildrec(components, next_value, bridge)
        if l > l_max:
            l_max = l
            s_max = s
        elif (l == l_max) and (s > s_max):
            l_max = l
            s_max = s
        bridge.pop()

    return l_max, s_max



def print_components(components):
    for i in components:
        print('{}/{}'.format(i.side1, i.side2))


def insert(components, component):
    for i in range(len(components)):
        if components[i] < component:
            components.insert(i, component)
            return
    components.append(component)


if __name__ == '__main__':
    main()