#!/usr/bin/env python3
import sys

def calibrate_one(test_value, operands):
    def dp_calibrate(acc, operands):
        if acc == test_value and len(operands) == 0:
            return True

        if acc > test_value or len(operands) == 0:
            return False

        return dp_calibrate(acc + operands[0], operands[1:]) or dp_calibrate(acc * operands[0], operands[1:])

    return dp_calibrate(operands[0], operands[1:])


def calibrate_two(test_value, operands):
    def dp_calibrate(acc, operands):
        if acc == test_value and len(operands) == 0:
            return True

        if acc > test_value or len(operands) == 0:
            return False

        return dp_calibrate(acc + operands[0], operands[1:]) or dp_calibrate(acc * operands[0], operands[1:]) or dp_calibrate(int(str(acc) + str(operands[0])), operands[1:])

    return dp_calibrate(operands[0], operands[1:])


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    total_one = total_two = 0

    for line in lines:
        test_value, operands = line.split(':')
        test_value = int(test_value)
        operands = [int(x) for x in operands.split()]

        if calibrate_one(test_value, operands):
            total_one += test_value

        if calibrate_two(test_value, operands):
            total_two += test_value

    # part one
    print(total_one)

    # part two
    print(total_two)


if __name__ == '__main__':
    main()
