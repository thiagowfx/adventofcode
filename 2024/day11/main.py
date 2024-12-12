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

def dp_blink(stones, times):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(stone: int, times: int) -> int:
        if times == 0:
            return 1

        return sum([dp(stone, times - 1) for stone in blink([stone])])

    return sum([dp(stone, times) for stone in stones])


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    stones = [int(stone) for stone in lines[0].split()]

    for _ in range(25):
        stones = blink(stones)

    # part one
    print(len(stones))

    # This is very slow, with an exponential complexity runtime.
    # What did you expect?
    #
    # for i in range(50):  # 50 = 75 - 25
    #     print(i)
    #     stones = blink(stones)

    # # part two
    # print(len(stones))

    stones = [int(stone) for stone in lines[0].split()]

    # part two
    print(dp_blink(stones, 75))


if __name__ == '__main__':
    main()
