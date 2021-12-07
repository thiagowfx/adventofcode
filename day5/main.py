#!/usr/bin/env python3
from collections import defaultdict
import sys

with open(sys.argv[1]) as input:
    lines = input.read().splitlines()

def fill(floor, first, second):
    if first[0] == second[0]:
        # print('vertical line:', f'first, second = {first}, {second}')

        for j in range(*[el + 1 if i == 1 else el for i, el in enumerate(sorted([first[1], second[1]]))]):
            # print(f'fill: <{first[0]}, {j}>')
            floor[(first[0], j)] += 1
    elif first[1] == second[1]:
        # print('horizontal line:', f'first, second = {first}, {second}')
        for i in range(*[el + 1 if i == 1 else el for i, el in enumerate(sorted([first[0], second[0]]))]):
            # print(f'fill: <{i}, {first[1]}>')
            floor[(i, first[1])] += 1

floor = defaultdict(int)

for line in lines:
    first, second = [pair.split(',') for pair in line.split(' -> ')]

    first = list(map(int, first))
    second = list(map(int, second))

    fill(floor, first, second)

print(sum(el >= 2 for el in list(floor.values())))
