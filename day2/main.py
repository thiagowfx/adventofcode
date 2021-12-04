#!/usr/bin/env python3
import sys

with open(sys.argv[1]) as input:
    lines = input.readlines()

units = [line.split(' ') for line in lines]

# Part 1
x = sum(int(unit[1]) for unit in units if unit[0] == 'forward')
y = sum(int(unit[1]) if unit[0] == 'down' else (-1) * int(unit[1]) if unit[0] == 'up' else 0 for unit in units)

print(x * y)

# Part 2
x = 0
y = 0
aim = 0

for unit in units:
    instruction = unit[0]
    distance = int(unit[1])

    if instruction == 'forward':
        x += distance
        y += aim * distance
    elif instruction == 'up':
        aim -= distance
    elif instruction == 'down':
        aim += distance

print(x * y)
