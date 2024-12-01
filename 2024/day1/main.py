#!/usr/bin/env python3
import sys

from collections import Counter


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    left = []
    right = []

    for line in lines:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()

    # part one
    print(sum(abs(l - r) for (l, r) in zip(left, right)))

    freqs = Counter(right)

    # part two
    print(sum(l * freqs[l] for l in left))


if __name__ == '__main__':
    main()
