#!/usr/bin/env python3
import sys

def blink(stones):
    stones_next = []

    for stone in stones:
        s = str(stone)

        if stone == 0:
            stones_next.append(1)

        elif len(s) % 2 == 0:
            index = len(s) // 2
            stones_next.append(int(s[:index]))
            stones_next.append(int(s[index:]))

        else:
            stones_next.append(stone * 2024)

    return stones_next


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    stones = [int(stone) for stone in lines[0].split()]

    for _ in range(25):
        stones = blink(stones)

    # part one
    print(len(stones))


if __name__ == '__main__':
    main()
