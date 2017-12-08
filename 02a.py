#!/usr/bin/python3


if __name__ == '__main__':
    sentinel = ''
    sumAll = 0

    for line in iter(input, sentinel):
        intLine = [int(s) for s in line.split()]
        print(intLine)
        minimum = intLine[0]
        maximum = intLine[0]
        for num in intLine:
            if minimum > num:
                minimum = num
            if maximum < num:
                maximum = num

        sumAll += maximum - minimum

    print(sumAll)
