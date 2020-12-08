#!/usr/bin/env python3

import sys

right = int(sys.argv[1])
down = int(sys.argv[2])
sentinel = sys.argv[3]

layout = [
    list(line.strip()) for line in sys.stdin.readlines() if line.strip != ""
]

pos = [0, 0]

while pos[1] < len(layout):
    if layout[pos[1]][pos[0]] == sentinel:
        print(pos)
    pos[0] = (pos[0] + right) % len(layout[0])
    pos[1] += down
