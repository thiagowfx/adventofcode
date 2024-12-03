#!/usr/bin/env python3
import re
import sys


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    prod = 0

    for memory in lines:
        matches = re.findall(r'mul\(\d+,\d+\)', memory)

        for match in matches:
            (f1, f2) = map(int, re.findall(r'\d+', match))
            prod += f1 * f2

    print(prod)


if __name__ == '__main__':
    main()
