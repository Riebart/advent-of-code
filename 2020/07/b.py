#!/usr/bin/env python3

import sys, re

start_bag = sys.argv[1]

edges = dict()

for line in sys.stdin.readlines():
    if line.strip() == "":
        continue
    container = re.match(r"^(.*) bags contain", line).group(1)
    contents = re.findall(r"([0-9]+) ([a-z -]*) bag", line)

    if container not in edges:
        edges[container] = dict()

    for bag in contents:
        edges[container][bag[1]] = int(bag[0])


def f(bag):
    return 1 + sum([v * f(k) for k, v in edges[bag].items()])


print(f(start_bag) - 1)
