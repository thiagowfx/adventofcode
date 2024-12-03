#!/usr/bin/env python3
import re
import sys


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    prod = prod_two = 0

    for memory in lines:
        ops = re.findall(r'mul\(\d+,\d+\)', memory)

        for op in ops:
            (f1, f2) = map(int, re.findall(r'\d+', op))
            prod += f1 * f2

    # part one
    print(prod)

    enabled = True
    for memory in lines:
        ops = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", memory)

        for op in ops:
            if "don't" in op:
                enabled = False
            elif "do" in op:
                enabled = True
            elif 'mul' in op:
                (f1, f2) = map(int, re.findall(r'\d+', op))

                if enabled:
                    prod_two += f1 * f2

    # part two
    print(prod_two)


if __name__ == '__main__':
    main()
