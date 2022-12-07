#!/usr/bin/env python3
from collections import defaultdict
import sys


def all_different(window):
    hash = defaultdict(int)
    for el in window:
        hash[el] += 1
    return not any(map(lambda x: x > 1, hash.values()))


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    buffer = lines[0]

    for i in range(len(buffer) - 3):
        window = buffer[i:i + 4]
        if (all_different(window)):
            # Part 1
            print(i + 4)
            break


if __name__ == '__main__':
    main()
