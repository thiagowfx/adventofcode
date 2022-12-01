#!/usr/bin/env python3
import itertools
import sys


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    # ['1', '2', '', '3'] -> [1, 2, '', 3]
    lines = [int(line) if line != "" else line for line in lines]

    # [1, 2, '', 3] -> [[1, 2], [3]]
    groups = [list(group) for key, group in itertools.groupby(
        lines, lambda a: a == "") if not key]

    # Part 1
    calories = [sum(group) for group in groups]

    print(max(calories))

    # Part 2
    print(sum(sorted(calories, reverse=True)[:3]))


if __name__ == '__main__':
    main()
