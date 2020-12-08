#!/usr/bin/env python3

import re, sys

for line in sys.stdin.readlines():
    m = re.match(r"([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)$", line)
    i1 = int(m.group(1))
    i2 = int(m.group(2))

    try:
        if (m.group(4)[i1 - 1] == m.group(3)) ^ (m.group(4)[i2 - 1]
                                                 == m.group(3)):
            print(line.strip())
    except:
        pass
