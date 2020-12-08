#!/usr/bin/env python3
import math, sys


def fuel_required(mass):
    return math.floor(mass / 3) - 2


def fuel_required2(mass):
    fuel = 0
    next_fuel = fuel_required(mass)
    while next_fuel > 0:
        fuel += next_fuel
        next_fuel = fuel_required(next_fuel)
    return fuel


lines = sys.stdin.readlines()

fuel = sum([fuel_required(int(l.strip())) for l in lines])
print(fuel)

fuel = sum([fuel_required2(int(l.strip())) for l in lines])
print(fuel)
