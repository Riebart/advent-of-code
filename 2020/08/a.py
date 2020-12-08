#!/usr/bin/env python3

import sys

program = [line.strip() for line in sys.stdin.readlines()]
runs = [0 for _ in range(len(program))]

acc = 0
loop = True

instruction = 0
while runs[instruction] <= 1:
    i = program[instruction]
    try:
        arg = int(i.split(" ")[1])
    except:
        arg = None

    if i.startswith("acc"):
        acc += arg
        instruction += 1
    elif i.startswith("nop"):
        instruction += 1
    elif i.startswith("jmp"):
        instruction += arg

    if instruction >= len(program):
        loop = False
        break
    elif instruction < 0:
        break

    runs[instruction] += 1

print(acc)
exit(loop)  # Python treats True as an exit code 1
