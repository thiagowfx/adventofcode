#!/usr/bin/env python3
import sys

from itertools import pairwise


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    safe = 0
    safe_damp = 0

    def is_safe(diffs):
        return all(1 <= n <= 3 for n in diffs) or all(-3 <= n <= -1 for n in diffs)

    for line in lines:
        l = list(map(int, line.split(' ')))
        diffs = [(b - a) for (a,b) in pairwise(l)]

        is_this_safe = is_safe(diffs)
        if is_this_safe:
            safe += 1
            safe_damp += 1
            continue

        for i in range(len(l)):
            if i == 0:
                if is_safe(diffs[1:]):
                    safe_damp += 1
                    break
            elif i == len(l) - 1:
                if is_safe(diffs[:-1]):
                    safe_damp += 1
                    break
            else:
                if is_safe(diffs[:i-1] + [l[i+1] - l[i-1]] + diffs[i+1:]):
                    safe_damp += 1
                    break

    # part one
    print(safe)

    # part two
    print(safe_damp)


if __name__ == '__main__':
    main()
