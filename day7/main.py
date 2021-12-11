#!/usr/bin/env python3
import statistics
import sys

with open(sys.argv[1]) as input:
    numbers = list(map(int, input.read().split(',')))

median = int(statistics.median(numbers))
fuel = sum(abs(median - number) for number in numbers)

print(fuel)
