#!/usr/bin/python3


def main():
    inp = input()

    programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    moves = inp.split(',')
    previous = []

    parsed = parse_moves(moves)

    for iteration in range(1000000000):
        i = 0
        order = ''.join(programs)
        if order not in previous:
            previous.append(order)
        else:
            final = previous[1000000000 % iteration]
            break

        while i < len(parsed):
            if parsed[i] == 's':
                programs = programs[-parsed[i+1]:] + programs[:-parsed[i+1]]
                i += 2

            elif parsed[i] == 'x':
                programs[parsed[i+1]], programs[parsed[i+2]] = programs[parsed[i+2]], programs[parsed[i+1]]
                i += 3

            elif parsed[i] == 'p':
                first = parsed[i+1]
                second = parsed[i+2]

                a, b = programs.index(first), programs.index(second)
                programs[a], programs[b] = programs[b], programs[a]
                i += 3

    print(final)


def parse_moves(moves):
    l = []

    for move in moves:
        if move[0] == 's':
            l.append('s')
            l.append(int(move[1:]))
        elif move[0] == 'x':
            l.append('x')
            l.append(int(move[1:].split('/')[0]))
            l.append(int(move[1:].split('/')[1]))
        elif move[0] == 'p':
            l.append('p')
            l.append(move[1])
            l.append(move[3])

    return l


if __name__ == '__main__':
    main()

