#!/usr/bin/env python3
import sys


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    X = 1
    cycle = 1
    cycle_to_X = {cycle: X}

    for line in lines:
        if line == 'noop':
            cycle += 1
        else:
            increment = int(line.split(' ')[1])
            X += increment
            cycle += 2
        cycle_to_X[cycle] = X

    strength = 0

    for multiple in range(20, max(cycle_to_X.keys()), 40):
        if multiple in cycle_to_X:
            strength += multiple * cycle_to_X[multiple]
        else:
            predecessor = max(
                [key for key in cycle_to_X.keys() if key < multiple])
            strength += multiple * cycle_to_X[predecessor]

    # Part 1
    print(strength)


if __name__ == '__main__':
    main()
