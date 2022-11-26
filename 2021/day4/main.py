#!/usr/bin/env python3
import re
import sys

with open(sys.argv[1]) as input:
    lines = input.readlines()

draws = list(map(int, lines[0].strip().split(',')))

num_boards = len(lines) // 6

boards = [[[[int(el), False] for el in re.split(r'[ ]+', r.strip())] for r in board] for board in [lines[(6 * n + 2) : 6 * n + 7] for n in range(num_boards)]]

def mark_board(board, draw):
    for row in board:
        for el in row:
            if el[0] == draw:
                el[1] = True
                return

def check_rows(board):
    for row in board:
        if all(marked for _, marked in row):
            return True
    return False

def check_cols(board):
    for col in zip(*board):
        if all(marked for _, marked in col):
            return True
    return False

def check_board(board):
    return check_rows(board) or check_cols(board)

def score(board, draw):
    return sum([n for n, marked in sum(board, []) if not marked]) * draw

def part1(boards, draws):
    for draw in draws:
        for board in boards:
            mark_board(board, draw)
            if check_board(board):
                print(score(board, draw))
                return

def part2(boards, draws):
    finished = [False] * len(boards)

    for draw in draws:
        for i, board in enumerate(boards):
            if finished[i]:
                continue
            mark_board(board, draw)
            if check_board(board):
                finished[i] = True
                if all(finished):
                    print(score(board, draw))
                    return

part1(boards, draws)
part2(boards, draws)
