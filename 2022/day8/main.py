#!/usr/bin/env python3
import itertools
import sys

DIRECTIONS = [
    [-1, 0],
    [+1, 0],
    [0, -1],
    [0, +1],
]


def is_visible(lines, x, y):
    this_tree = lines[x][y]

    for direction in DIRECTIONS:
        visible = True

        step = 1
        while True:
            next_x = x + step * direction[0]
            next_y = y + step * direction[1]

            if 0 <= next_x < len(lines[0]) and 0 <= next_y < len(lines):
                next_tree = lines[next_x][next_y]
                if next_tree >= this_tree:
                    visible = False
                    break
                step += 1
            else:
                break

        if visible:
            return True

    return False


def compute_inner_visible_trees(lines):
    """
    Cartesian product:
    0 ---> x
    |
    |
  y v
    """
    return sum(int(is_visible(lines, x, y)) for (x, y) in itertools.product(range(1, len(lines[0]) - 1), range(1, len(lines) - 1)))


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    outer_visible_trees = 2 * (len(lines) + len(lines[0])) - 4
    inner_visible_trees = compute_inner_visible_trees(lines)

    # Part 1
    print(outer_visible_trees + inner_visible_trees)


if __name__ == '__main__':
    main()
