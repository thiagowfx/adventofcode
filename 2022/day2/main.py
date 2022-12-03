#!/usr/bin/env python3
import sys

MOVE_SCORE = {
    # theirs
    'A': 1,  # rock
    'B': 2,  # paper
    'C': 3,  # scissors

    # mine
    'X': 1,  # rock
    'Y': 2,  # paper
    'Z': 3,  # scissors
}


def battle(theirs, mine):
    if (theirs, mine) in [('A', 'X'), ('B', 'Y'), ('C', 'Z')]:
        return 3  # draw
    elif (theirs, mine) in [('A', 'Z'), ('B', 'X'), ('C', 'Y')]:
        return 0  # defeat
    else:
        return 6  # victory


def strategy(theirs, mine):
    if mine == 'Y':  # draw
        return chr(ord(theirs) + (ord('X') - ord('A')))
    elif mine == 'X':  # lose
        return {'A': 'Z', 'B': 'X', 'C': 'Y'}[theirs]
    else:  # win
        assert mine == 'Z'
        return {'A': 'Y', 'B': 'Z', 'C': 'X'}[theirs]


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    score1, score2 = 0, 0

    for line in lines:
        theirs, mine = line.split(' ')

        score1 += MOVE_SCORE[mine] + battle(theirs, mine)

        mine = strategy(theirs, mine)
        score2 += MOVE_SCORE[mine] + battle(theirs, mine)

    print(score1)
    print(score2)


if __name__ == '__main__':
    main()
