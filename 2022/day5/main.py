#!/usr/bin/env python3
import itertools
import sys
from copy import deepcopy


def parse_input(crates_unparsed):
    """
    Returns a dictionary in the following form:

    {
      1: 'ZN',
      2: 'MCD',
      3: 'P',
    }
    """

    crates = {}

    num_stacks = (len(crates_unparsed[0]) + 1) // 4
    max_height = len(crates_unparsed) - 1

    for i_stack in range(1, num_stacks + 1):
        stack_xaxis = 4 * (i_stack - 1) + 1

        # List comprehension version, not super readable:
        # crates[i_stack] = ''.join(list(filter(lambda x: x != ' ', [crates_unparsed[max_height - i][stack_xaxis]
        #                                                            for i in range(1, max_height + 1)])))

        crates[i_stack] = ''
        for i in range(1, max_height + 1):
            crate = crates_unparsed[max_height - i][stack_xaxis]
            if crate != ' ':
                crates[i_stack] += crate

    return crates


def move_crates(moves_unparsed, crates, *, reverse):
    for move_unparsed in moves_unparsed:
        _, quantity, _, src, _, dst = move_unparsed.split(' ')
        quantity, src, dst = int(quantity), int(src), int(dst)
        move_crate(crates, quantity, src, dst, reverse)
    return crates


def move_crate(crates, quantity, src, dst, reverse):
    if reverse:
        crates[dst] += crates[src][(-1) * quantity:][::-1]
    else:
        crates[dst] += crates[src][(-1) * quantity:]
    crates[src] = crates[src][:(-1) * quantity]


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    crates_unparsed, moves_unparsed = [list(group) for key, group in itertools.groupby(
        lines, lambda a: a == "") if not key]

    crates = parse_input(crates_unparsed)

    # Part 1
    crates_part1 = move_crates(moves_unparsed, deepcopy(crates), reverse=True)
    print(''.join([value[-1] for value in crates_part1.values()]))

    # Part 2
    crates_part2 = move_crates(moves_unparsed, deepcopy(crates), reverse=False)
    print(''.join([value[-1] for value in crates_part2.values()]))


if __name__ == '__main__':
    main()
