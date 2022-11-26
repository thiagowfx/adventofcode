#!/usr/bin/env python3
from collections import defaultdict
from itertools import count, islice
import sys

with open(sys.argv[1]) as input:
    lines = input.read().splitlines()

def direction(a, b):
    """
    3, 5 => +1
    5, 3 => -1
    5, 5 => 0
    """
    return 1 if b > a else -1 if a > b else 0

def fill(floor, x1, y1, x2, y2):
    for x, y in islice(zip(count(start = x1, step = direction(x1, x2)), count(start = y1, step = direction(y1, y2))), max(abs(x2 - x1), abs(y2 - y1)) + 1):
        floor[(x, y)] += 1

def part1():
    floor = defaultdict(int)

    for line in lines:
        (x1, y1), (x2, y2) = _, _ = [list(map(int, pair.split(','))) for pair in line.split(' -> ')]
        if x1 == x2 or y1 == y2:
            fill(floor, x1, y1, x2, y2)

    print(sum(el >= 2 for el in floor.values()))

def part2():
    floor = defaultdict(int)

    for line in lines:
        (x1, y1), (x2, y2) = _, _ = [list(map(int, pair.split(','))) for pair in line.split(' -> ')]
        fill(floor, x1, y1, x2, y2)

    print(sum(el >= 2 for el in floor.values()))

part1()
part2()
