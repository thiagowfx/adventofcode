#!/usr/bin/env python3
import sys


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    a, b, c = [int(line.split()[2]) for line in lines[0:3]]
    program = [int(op) for op in lines[4].split()[1].split(",")]
    ip = 0
    stdout = []

    def combo(operand):
        assert 0 <= operand < 7

        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return a
        elif operand == 5:
            return b
        elif operand == 6:
            return c

    while ip < len(program) - 1:
        opcode = program[ip]
        operand = program[ip + 1]

        # adv, division
        if opcode == 0:
            numerator = a
            denominator = 2 ** combo(operand)
            a = numerator // denominator
        # bxl, bitwise xor
        elif opcode == 1:
            b ^= operand
        # bst, modulo
        elif opcode == 2:
            b = combo(operand) % 8
        # jnz
        elif opcode == 3:
            if a != 0:
                ip = operand
                continue
        # bxc, bitwise xor
        elif opcode == 4:
            b ^= c
        # out
        elif opcode == 5:
            stdout.append(combo(operand) % 8)
        # bdv
        elif opcode == 6:
            numerator = a
            denominator = 2 ** combo(operand)
            b = numerator // denominator
        # cdv
        elif opcode == 7:
            numerator = a
            denominator = 2 ** combo(operand)
            c = numerator // denominator

        ip += 2

    # part one
    print(",".join(map(str, stdout)))


if __name__ == '__main__':
    main()
