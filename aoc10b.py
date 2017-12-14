#!/usr/bin/python3
#35b028fe2c958793f7d5a61d7a08c8

def main():
    raw_input = input()
    lenghts = [ord(x) for x in raw_input] + [17, 31, 73, 47, 23]
    print(len(raw_input))
    print(len(lenghts))
    l = [x for x in range(256)]
    current = 0
    skip_size = 0

    for round in range(64):
        for lenght in lenghts:
            reverse(l, lenght, current)
            current = (current+lenght+skip_size)%len(l)
            skip_size += 1

    dense = reduce(l)

    out = to_hex(dense)

    print(out)


def to_hex(l):
    s = ''
    for n in l:
        helper = hex(n)[2:]
        if len(helper) == 1:
            s += '0'
        s+= helper

    return s


def reduce(l):
    d = []
    for i in range(16):
        element = 0
        for j in range(16):
            element = element ^ l[16*i +j]
        d.append(element)

    return d


def reverse(l, lenght, current):
    if current + lenght <= len(l):
        if current == 0:
            l[:lenght] = l[lenght-1::-1]
        else:
            l[current:current+lenght] = l[current+lenght-1:current-1:-1]
        return

    len1 = len(l) - current
    len2 = lenght - len1

    sub_list = l[current:] + l[:len2]
    sub_list = list(reversed(sub_list))

    l[current:] = sub_list[:len1]
    l[:len2] = sub_list[len1:]

if __name__ == '__main__':
    main()