#!/usr/bin/python3
#99, 127, 0, 129

import fileinput
from queue import Queue
import threading
from time import sleep

print_lock = threading.Lock()


def main():
    instructions = []

    for line in fileinput.input():
        if line == '\n':
            break
        instructions.append(line.split())

    q0 = Queue()
    q1 = Queue()

    waiting = [False, False]
    sent = [0, 0]
    received = [0, 0]
    prog_a = threading.Thread(target=worker, args=(instructions, 0, q0, q1, waiting, sent, received))
    prog_b = threading.Thread(target=worker, args=(instructions, 1, q1, q0, waiting, sent, received))

    prog_a.start()
    prog_b.start()

    #for i in range(20):
    #    print(sent)
    #    print(received)
    #    print()
    #    sleep(5)

    prog_a.join()
    prog_b.join()

    print(sent)
    print(received)


def worker(instructions, id, receive, send, is_waiting, times_sent, times_received):
    i = 0
    registers = {'p': id}

    while (i >= 0) and (i < len(instructions)):
        instruction = instructions[i][0]
        first = instructions[i][1]
        if first not in registers:
            registers[first] = 0
        if len(instructions[i]) == 3:
            second = instructions[i][2]
            try:
                value = int(second)
            except ValueError:
                if second not in registers:
                    registers[second] = 0
                value = None

        if instruction == 'snd':
            #with print_lock:
            #    print("id: {} sending reg {} with value {}".format(id, first, registers[first]))
            send.put(registers[first])
            times_sent[id] += 1
        elif instruction == 'set':
            if value is not None:
                registers[first] = value
            else:
                registers[first] = registers[second]
        elif instruction == 'add':
            if value is not None:
                registers[first] += value
            else:
                registers[first] += registers[second]
        elif instruction == 'mul':
            if value is not None:
                registers[first] *= value
            else:
                registers[first] *= registers[second]
        elif instruction == 'mod':
            if value is not None:
                registers[first] %= value
            else:
                registers[first] %= registers[second]
        elif instruction == 'rcv':
            #with print_lock:
            #    print("id: {} receiving reg {}".format(id, first))
            if receive.empty() and is_waiting[1-id] and send.empty():
                is_waiting[id] = True
                send.put(False)
                return
            is_waiting[id] = True
            got = receive.get()
            is_waiting[id] = False
            if got is False:
                return
            registers[first] = got
            times_received[id] += 1
            #with print_lock:
            #    print("id: {} received reg {} value {}".format(id, first, got))
        elif (instruction == 'jgz') and ((representsInt(first) and (int(first) > 0)) or ((first in registers) and (registers[first] > 0))):
            #old = i
            if value is not None:
                i += value - 1
            else:
                i += registers[second] - 1
            #with print_lock:
            #    print("id: {} jumping from {} to {}".format(id, old, i+1))
            #sleep(1)
        i += 1

    send.put(False)

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    main()
