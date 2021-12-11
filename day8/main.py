#!/usr/bin/env python3
import sys

with open(sys.argv[1]) as input:
    lines = input.read().splitlines()

def part1():
    total = 0

    for line in lines:
        outputs = line.split(' | ')[1].split(' ')
        total += sum(len(output) in [2, 3, 4, 7] for output in outputs)

    print(total)

part1()
