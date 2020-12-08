#!/usr/bin/env python3

import sys

directions = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}

paths = [
    line.strip().split(",") for line in sys.stdin.readlines()
    if line.strip() != ""
]

path_points = list()
for path in paths:
    trail = list()
    path_points.append(trail)
    position = [0, 0]
    for part in path:
        direction = directions[part[0]]
        length = int(part[1:])
        for _ in range(1, length + 1):
            position[0] += direction[0]
            position[1] += direction[1]
            trail.append(tuple(position))

print(
    min([
        sum(p) for p in set(path_points[0]).intersection(set(path_points[1]))
    ]))

steps = dict()
for p in set(path_points[0]).intersection(set(path_points[1])):
    steps[p] = list()
    for t in path_points:
        i = 0
        while t[i] != p:
            i += 1
        steps[p].append(i + 1)

print(min([sum(v) for k, v in steps.items()]))
