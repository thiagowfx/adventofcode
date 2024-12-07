#!/usr/bin/env python3
from collections import defaultdict
import sys


def is_correct(update, edges):
    position = defaultdict(lambda: sys.maxsize, {node: i for (i, node) in enumerate(update)})

    for (first, second) in edges:
        if first in update and second in update and position[first] > position[second]:
            return False
    return True

def toposort(update, edges):
    position = defaultdict(lambda: sys.maxsize, {node: i for (i, node) in enumerate(update)})

    change = True
    while change:
        change = False
        for (first, second) in edges:
            if first in update and second in update and position[first] >= position[second]:
                position[first] = position[second] - 1
                change = True

    return sorted(update, key=lambda x: position[x])

def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    edges = []
    updates = []

    for line in lines:
        if "|" in line:
            edges.append(list(map(int, line.split("|"))))
        elif len(line) == 0:
            continue
        else:
            updates.append(list(map(int, line.split(","))))

    total_one = total_two = 0
    for update in updates:
        if is_correct(update, edges):
            total_one += update[len(update) // 2]
        else:
            sorted_update = toposort(update, edges)
            total_two += sorted_update[len(sorted_update) // 2]

    # part one
    print(total_one)

    # part two
    print(total_two)


if __name__ == '__main__':
    main()
