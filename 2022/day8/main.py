#!/usr/bin/env python3
import itertools
import sys

DIRECTIONS = [
    [-1, 0],  # left
    [+1, 0],  # right
    [0, -1],  # down
    [0, +1],  # up
]


def is_visible(lines, x, y, is_scenic):
    this_tree = lines[y][x]
    scenic = 1

    for direction in DIRECTIONS:
        visible = True

        step = 1
        while True:
            next_x = x + step * direction[0]
            next_y = y + step * direction[1]

            if 0 <= next_x < len(lines[0]) and 0 <= next_y < len(lines):
                next_tree = lines[next_y][next_x]
                if next_tree >= this_tree:
                    visible = False
                    break
                step += 1
            else:
                step -= 1
                break

        scenic *= step

        if visible and not is_scenic:
            return visible

    return scenic if is_scenic else visible


def compute_inner_visible_trees(lines, *, is_scenic):
    """
    Cartesian product: [y][x]
    0 ---> x
    |
    |
  y v
    """
    if is_scenic:
        return max(int(is_visible(lines, x, y, is_scenic)) for (x, y) in itertools.product(range(1, len(lines[0]) - 1), range(1, len(lines) - 1)))
    else:
        return sum(int(is_visible(lines, x, y, is_scenic)) for (x, y) in itertools.product(range(1, len(lines[0]) - 1), range(1, len(lines) - 1)))


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    outer_visible_trees = 2 * (len(lines) + len(lines[0])) - 4

    # Part 1
    print(outer_visible_trees + compute_inner_visible_trees(lines, is_scenic=False))

    # Part 2
    print(compute_inner_visible_trees(lines, is_scenic=True))


if __name__ == '__main__':
    main()
