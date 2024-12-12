#!/usr/bin/env python3
import sys

def calibrate(test_value, operands):
    def dp_calibrate(acc, operands):
        if acc == test_value and len(operands) == 0:
            return True

        if acc > test_value or len(operands) == 0:
            return False

        return dp_calibrate(acc + operands[0], operands[1:]) or dp_calibrate(acc * operands[0], operands[1:])

    return dp_calibrate(operands[0], operands[1:])


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    total = 0

    for line in lines:
        test_value, operands = line.split(':')
        test_value = int(test_value)
        operands = [int(x) for x in operands.split()]

        if calibrate(test_value, operands):
            total += test_value

    # part one
    print(total)

    # 945513094364


if __name__ == '__main__':
    main()
