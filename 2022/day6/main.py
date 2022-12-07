#!/usr/bin/env python3
from collections import defaultdict
import sys


def all_different(window):
    hash = defaultdict(int)
    for el in window:
        hash[el] += 1
    return not any(map(lambda x: x > 1, hash.values()))


def find_marker(buffer, size):
    for i in range(len(buffer) - (size - 1)):
        window = buffer[i:i + size]
        if (all_different(window)):
            return i + size


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    buffer = lines[0]

    # Part 1
    print(find_marker(buffer, 4))

    # Part 2
    print(find_marker(buffer, 14))


if __name__ == '__main__':
    main()
