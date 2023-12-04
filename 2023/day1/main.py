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


SPELLINGS = {
    # 'zero': '0',  # not in the problem statement
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


# This attempt is incorrect because of the following test case:
#   eightwothree -> eigh23 -> 23
# Whereas it should have been 83.
def get_calibration_value_with_spellings_attempt_1(line: str) -> int:
    for spelling, digit in SPELLINGS.items():
        line = line.replace(spelling, digit)

    return get_calibration_value(line)


def get_calibration_value_with_spellings(line: str) -> int:
    targets = set(list(SPELLINGS.keys()) + list(SPELLINGS.values()))

    # from the left
    indices = {}
    for target in targets:
        index = line.find(target)
        if index != -1:
            indices[target] = index

    [target_min, _] = min(list(indices.items()), key=lambda x: x[1])

    # from the right
    indices = {}
    for target in targets:
        index = line.rfind(target)
        if index != -1:
            indices[target] = index

    [target_max, _] = max(list(indices.items()), key=lambda x: x[1])

    if target_min in SPELLINGS:
        target_min = SPELLINGS[target_min]

    if target_max in SPELLINGS:
        target_max = SPELLINGS[target_max]

    return int(target_min + target_max)


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    # Part I
    print(sum([get_calibration_value(line) for line in lines]))

    # Part II
    print(sum([get_calibration_value_with_spellings(line) for line in lines]))


if __name__ == '__main__':
    main()
