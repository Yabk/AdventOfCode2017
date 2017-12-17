#!/usr/bin/python3


def main():
    steps = int(input())
    buffer = [0]
    pos = 0

    for i in range (1, 2018):
        pos = (pos+steps) % len(buffer) + 1
        buffer.insert(pos, i)

    print(buffer[pos+1])


if __name__ == '__main__':
    main()
