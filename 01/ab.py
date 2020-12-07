#!/usr/bin/env python3
import sys

target = int(sys.argv[1])
count = int(sys.argv[2])


def f(numbers, target, count):
    for i in range(len(numbers)):
        if numbers[i] <= target:
            if count == 1:
                if numbers[i] == target:
                    print(numbers[i])
                    return True
            else:
                if f(numbers[i + 1:], target - numbers[i], count - 1):
                    print(numbers[i])
                    return True

    if count == 1:
        return False


numbers = [int(l) for l in sys.stdin.readlines()]
f(numbers, target, count)
