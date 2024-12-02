#!/usr/bin/env python3
import sys

from itertools import pairwise


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    safe = 0

    for line in lines:
        diffs = [(a - b) for (a,b) in pairwise(map(int, line.split(' ')))]
        safe += all(1 <= n <= 3 for n in diffs) or all(-3 <= n <= -1 for n in diffs)

    # part one
    print(safe)


if __name__ == '__main__':
    main()
