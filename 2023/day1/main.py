#!/usr/bin/env python3
import sys


def get_calibration_value(line: str) -> int:
    """
    Extract the first and the last digit from the string, and return a number
    composed by them, in that order.
    '1abc2' -> 12
    """
    digits = [c for c in line if c.isdigit()]
    return int(digits[0] + digits[-1])


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    # Part I
    print(sum([get_calibration_value(line) for line in lines]))


if __name__ == '__main__':
    main()
