#!/usr/bin/env python3
import sys


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    print(lines)


if __name__ == '__main__':
    main()
