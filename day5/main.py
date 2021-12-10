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

def fill_part1(floor, first, second):
    [x1, y1] = first
    [x2, y2] = second

    # vertical line
    if x1 == x2:
        for y in list(range(*sorted([y1, y2]))) + [max(y1, y2)]:
            floor[(x1, y)] += 1

    # # horizontal line
    elif y1 == y2:
        for x in list(range(*sorted([x1, x2]))) + [max(x1, x2)]:
            floor[(x, y1)] += 1

def fill_part2(floor, first, second):
    [x1, y1] = first
    [x2, y2] = second

    for x, y in islice(zip(count(start = x1, step = direction(x1, x2)), count(start = y1, step = direction(y1, y2))), max(abs(x2 - x1), abs(y2 - y1)) + 1):
        floor[(x, y)] += 1

def part1():
    floor = defaultdict(int)

    for line in lines:
        first, second = [pair.split(',') for pair in line.split(' -> ')]

        first = list(map(int, first))
        second = list(map(int, second))

        fill_part1(floor, first, second)

    print(sum(el >= 2 for el in floor.values()))

def part2():
    floor = defaultdict(int)

    for line in lines:
        first, second = [pair.split(',') for pair in line.split(' -> ')]

        first = list(map(int, first))
        second = list(map(int, second))

        fill_part2(floor, first, second)

    print(sum(el >= 2 for el in floor.values()))

part1()
part2()
