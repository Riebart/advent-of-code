#!/usr/bin/env python3

import sys, json


class IntcodeComputer(object):
    class Op(object):
        def __init__(self, code, nparams):
            self.code = code
            self.nparams = nparams

    class AddOp(Op):
        def do(self, position, program):
            program[program[position + 3]] = program[program[
                position + 1]] + program[program[position + 2]]
            return position + self.nparams + 1

    class MultOp(Op):
        def do(self, position, program):
            program[program[position + 3]] = program[program[
                position + 1]] * program[program[position + 2]]
            return position + self.nparams + 1

    class StopOp(Op):
        def do(self, position, program):
            return None

    def __init__(self, program):
        self.program = program
        self.ops = {
            1: self.AddOp(1, 3),
            2: self.MultOp(2, 3),
            99: self.StopOp(99, 0)
        }

    def run(self, maxsteps=float("inf")):
        numsteps = 0
        position = 0
        while numsteps <= maxsteps and \
            position is not None and \
            0 <= position and \
            position < len(self.program):
            position = self.ops[self.program[position]].do(
                position, self.program)
            numsteps += 1


target = int(sys.argv[1])

program = [
    int(op.strip()) for op in sys.stdin.read().split(",") if op.strip() != ""
]

copy = [m for m in program]
copy[1] = 12
copy[2] = 2

computer = IntcodeComputer(copy)
computer.run()
print(copy[0])

for noun in range(0, 100):
    for verb in range(0, 100):
        copy = [m for m in program]
        copy[1] = noun
        copy[2] = verb
        computer = IntcodeComputer(copy)

        try:
            computer.run()
        except:
            pass

        if copy[0] == target:
            print(100 * noun + verb)
