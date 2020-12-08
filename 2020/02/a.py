#!/usr/bin/env python3

import re, sys

for line in sys.stdin.readlines():
    m = re.match(r"([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)$", line)
    rule = "^[^%s]*(%s[^%s]*){%s,%s}$" % (m.group(3), m.group(3), m.group(3),
                                          m.group(1), m.group(2))
    if re.match(rule, m.group(4)) is not None:
        print(line.strip())
