#!/usr/bin/env python3
import sys

DIRECTIONS = {
    'L': (-1, 0),  # left
    'R': (+1, 0),  # right
    'D': (0, -1),  # down
    'U': (0, +1),  # up
}


def execute_move(H, T, direction, num_moves, visited):
    for _ in range(num_moves):
        # overlappping: only move head
        if H == T:
            H = (H[0] + DIRECTIONS[direction][0],
                 H[1] + DIRECTIONS[direction][1])
        # next to each other in a '+' fashion: move T only if H moves in the same direction
        elif abs(H[0] - T[0]) + abs(H[1] - T[1]) == 1:
            H = (H[0] + DIRECTIONS[direction][0],
                 H[1] + DIRECTIONS[direction][1])
            if abs(H[0] - T[0]) == 2 or abs(H[1] - T[1]) == 2:
                T = (T[0] + DIRECTIONS[direction][0],
                     T[1] + DIRECTIONS[direction][1])
                visited.add(T)
        # next to each other in a 'x' fashion: move T only if H moves farther away
        else:
            H_prev = H
            H = (H[0] + DIRECTIONS[direction][0],
                 H[1] + DIRECTIONS[direction][1])
            if (abs(H[0] - T[0]) + abs(H[1] - T[1])) == 3:
                T = H_prev
                visited.add(T)

    return H, T, visited


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    # Initial position of Head and Tail.
    H = T = (0, 0)

    # Tuple with (x, y) coordinates, assume (0, 0) is the starting point.
    visited = {(0, 0)}

    for line in lines:
        direction, num_moves = line.split(' ')
        H, T, visited = execute_move(H, T, direction, int(num_moves), visited)

    # Part 1
    print(len(visited))


if __name__ == '__main__':
    main()
