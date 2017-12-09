#!/usr/bin/python3


def main():
    stream = input()
    clean, n_removed = remove_garbage(stream)
    print(clean)
    print(rec(clean, 1))
    print("removed: ", n_removed)


def remove_garbage(stream):
    chars1= []
    skipped = 0

    skip = False
    for char in stream:
        if skip:
            skip = False
            continue

        if char == '!':
            skip = True
            continue

        chars1.append(char)

    chars2 = []
    garbage = False
    for char in chars1:
        if garbage:
            if char == '>':
                garbage = False
                continue
            else:
                skipped += 1
                continue
        else:
            if char == '<':
                garbage = True
                continue
            else:
                chars2.append(char)

    return ''.join(list(filter(None, ''.join(chars2).split(',')))), skipped


def rec(group, level):
    #print(''.join(group))
    #print(level)
    sum = level

    subgroup = []
    counter = 0
    #print(group)
    for char in group[1:-1]:
        if counter == 0:
            if char == '{':
                subgroup.append('{')
                counter += 1
            else:
                print("wat?")
        else:
            if char == '{':
                counter += 1
                subgroup.append(char)
            elif char == '}':
                subgroup.append(char)
                counter -= 1
                #print("oduzeo: ", counter)
                if counter == 0:
                    sum += rec(subgroup, level+1)
                    subgroup = []

    return sum


if __name__ == '__main__':
    main()