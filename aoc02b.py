#!/usr/bin/python3

if __name__ == '__main__':
    sentinel = ''
    sumall = 0

    for line in iter(input, sentinel):
        intLine = [int(s) for s in line.split()]
        print(intLine)

        found = False
        for i in range(len(intLine)):
            for j in range(i):
                if intLine[i]%intLine[j] == 0:
                    sumall += int(intLine[i]/intLine[j])
                    found = True
                    break
            if found:
                found = False
                break
            for j in range(i+1, len(intLine)):
                if intLine[i]%intLine[j] == 0:
                    sumall += int(intLine[i]/intLine[j])
                    break

    print(sumall)
