#!/usr/bin/env python3
import sys

def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    ans = 0
    dial = 50

    for line in lines:
        direction = line[0]
        assert direction in 'LR'

        delta = int(line[1:])
        assert delta >= 0

        dial = (dial + (-1 if direction == 'L' else 1) * delta + 100) % 100
        # print(direction, delta, dial)

        if dial == 0:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
