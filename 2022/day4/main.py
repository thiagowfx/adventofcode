#!/usr/bin/env python3
import sys


def eitherContains(e1, e2):
    if e1[0] >= e2[0] and e1[1] <= e2[1]:
        return 1
    elif e2[0] >= e1[0] and e2[1] <= e1[1]:
        return 1
    else:
        return 0


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    total = 0

    for line in lines:
        # [['2', '4'], ['6', '8']]
        [e1, e2] = [el.split('-') for el in line.split(',')]
        # [2, 4], [6, 8]
        e1, e2 = list(map(int, e1)), list(map(int, e2))

        total += eitherContains(e1, e2)

    print(total)


if __name__ == '__main__':
    main()
