#!/usr/bin/env python3
import sys

with open(sys.argv[1]) as input:
    lines = input.readlines()

numbers = [int(line.strip()) for line in lines]

# Part 1
print(sum(y > x for x, y in zip(numbers[:-1], numbers[1:])))

# Part 2
print(sum(y > x for x, y in zip(numbers[:-3], numbers[3:])))
