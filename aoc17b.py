#!/usr/bin/python3
#This is not completely correct solution.
#You should be checking if some element gets inserted at index 0.
#In that case your 0 gets shifted right.
#For my input this solution worked, just because nothing got inserted at index 0.

def main():
    steps = int(input())
    size = 1
    pos = 0
    nexto0 = None

    for i in range (1, 50000000):
        pos = (pos+steps) % size + 1
        if pos == 1:
            nexto0 = i
        size += 1

    print(nexto0)


if __name__ == '__main__':
    main()
