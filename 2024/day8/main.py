#!/usr/bin/env python3
from collections import defaultdict
from itertools import combinations

import sys


def compute_antinodes(coord1, coord2, height, width):
    x1, y1 = coord1
    x2, y2 = coord2

    dx = x2 - x1
    assert dx >= 0

    dy = y2 - y1

    x3, y3 = x1 - dx, y1 - dy
    x4, y4 = x2 + dx, y2 + dy

    antinodes = ()

    if 0 <= x3 < height and 0 <= y3 < width:
        antinodes += ((x3, y3),)

    if 0 <= x4 < height and 0 <= y4 < width:
        antinodes += ((x4, y4),)

    return antinodes


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    antinodes = set()

    # {'0': ((1,8), ...)}
    freq_map = defaultdict(tuple)
    for x, line in enumerate(lines):
        for y, field in enumerate(line):
            if field.isalnum():
                freq_map[field] += ((x, y),)

    for all_coords in freq_map.values():
        for coord1, coord2 in combinations(all_coords, 2):
            antinodes.update(compute_antinodes(coord1, coord2, len(lines), len(lines[0])))

    # part one
    print(len(antinodes))


if __name__ == '__main__':
    main()
