#!/usr/bin/env python3
from collections import Counter
import sys

with open(sys.argv[1]) as input:
    numbers = list(map(int, input.read().split(',')))

fish = Counter(numbers)

for _ in range(80):
    next_fish = Counter()
    for timer, count in fish.items():
        if timer == 0:
            next_fish[8] += fish[timer]
            next_fish[6] += fish[timer]
        else:
            next_fish[timer - 1] += fish[timer]
    fish = next_fish

print(len(list(fish.elements())))
