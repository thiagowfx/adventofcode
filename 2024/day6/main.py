#!/usr/bin/env python3
import sys


def find(lines, c):
    for i, line in enumerate(lines):
        if c in line:
            return i, line.index(c)
    raise ValueError(f'Could not find {c} in lines')


def move(pos, dir, lines, visited):
    dirs_clockwise = ((1, 0), (0, -1), (-1, 0), (0, 1))

    while True:
        next_pos = pos[0] + dir[0], pos[1] + dir[1]

        if next_pos[0] < 0 or next_pos[0] >= len(lines) or next_pos[1] < 0 or next_pos[1] >= len(lines[0]):
            break

        if lines[next_pos[0]][next_pos[1]] in '.^':
            pos = next_pos
            visited.add(pos)
        elif lines[next_pos[0]][next_pos[1]] == '#':
            dir = dirs_clockwise[(dirs_clockwise.index(dir) + 1) % 4]

def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    pos = find(lines, '^')
    dir = (-1, 0)  # up

    visited = set((pos,))

    move(pos, dir, lines, visited)

    # part one
    print(len(visited))


if __name__ == '__main__':
    main()
