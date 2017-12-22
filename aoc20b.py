#!/usr/bin/python3
#0

import fileinput
import sys
import re


def main():
    iterations = 100
    i = 0
    particlesID = []
    particles = []

    for line in fileinput.input():
        if line == '\n':
            break
        particlesID.append(i)
        i += 1

        split = re.search('p=<(.*),(.*),(.*)>, v=<(.*),(.*),(.*)>, a=<(.*),(.*),(.*)>', line)
        particles.append([int(split.group(1)), int(split.group(2)), int(split.group(3)), int(split.group(4)),
                          int(split.group(5)), int(split.group(6)), int(split.group(7)), int(split.group(8)), int(split.group(9))])

    for iter in range(iterations):
        toDelete = set()
        for i in range(len(particlesID)):
            for j in range(i+1, len(particlesID)):
                if (particles[i][0] == particles[j][0]) and (particles[i][1] == particles[j][1]) and (particles[i][2] == particles[j][2]):
                    toDelete.add(particlesID[i])
                    toDelete.add(particlesID[j])

        for part in toDelete:
            index = particlesID.index(part)
            del(particlesID[index])
            del(particles[index])

        for i in range(len(particlesID)):
            particles[i][3] += particles[i][6]
            particles[i][4] += particles[i][7]
            particles[i][5] += particles[i][8]

            particles[i][0] += particles[i][3]
            particles[i][1] += particles[i][4]
            particles[i][2] += particles[i][5]

    print(len(particlesID))

if __name__ == '__main__':
    main()
