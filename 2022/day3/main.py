#!/usr/bin/env python3
import sys


def priority(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        assert item.isupper()
        return ord(item) - ord('A') + 27


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    total_priority = 0

    for line in lines:
        c1 = line[:len(line)//2]
        c2 = line[len(line)//2:]
        item = next(iter(set(c1).intersection(c2)))
        total_priority += priority(item)

    print(total_priority)


if __name__ == '__main__':
    main()
