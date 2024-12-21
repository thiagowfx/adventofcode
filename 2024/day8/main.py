#!/usr/bin/env python3
from collections import defaultdict
from itertools import combinations

import sys

def within_bounds(x, y, height, width):
    return 0 <= x < height and 0 <= y < width


def compute_antinodes(coord1, coord2, height, width, unbounded=False):
    x1, y1 = coord1
    x2, y2 = coord2

    dx = x2 - x1
    assert dx >= 0

    dy = y2 - y1

    if unbounded:
        antinodes = ((x1, y1), (x2, y2))
    else:
        antinodes = ()

    for (x0, y0, direction) in ((x1, y1, -1), (x2, y2, +1)):
        steps = 1
        while True:
            x, y = x0 + direction * steps * dx, y0 + direction * steps * dy
            if within_bounds(x, y, height, width):
                antinodes += ((x, y),)
                steps += 1
            else:
                break

    return antinodes


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    # {'0': ((1,8), ...)}
    freq_map = defaultdict(tuple)
    for x, line in enumerate(lines):
        for y, field in enumerate(line):
            if field.isalnum():
                freq_map[field] += ((x, y),)

    antinodes = set()

    for all_coords in freq_map.values():
        for coord1, coord2 in combinations(all_coords, 2):
            antinodes.update(compute_antinodes(coord1, coord2, len(lines), len(lines[0])))

    # part one
    print(len(antinodes))

    antinodes = set()

    for all_coords in freq_map.values():
        for coord1, coord2 in combinations(all_coords, 2):
            antinodes.update(compute_antinodes(coord1, coord2, len(lines), len(lines[0]), unbounded=True))

    # part two
    print(len(antinodes))

if __name__ == '__main__':
    main()
