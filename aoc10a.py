#!/usr/bin/python3

def main():
    raw_input = input().split(',')
    lenghts = [int(x) for x in raw_input]
    l = [x for x in range(256)]
    current = 0
    skip_size = 0

    for lenght in lenghts:
        reverse(l, lenght, current)
        current = (current+lenght+skip_size)%len(l)
        skip_size += 1

    print(str(l[0]*l[1]))



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