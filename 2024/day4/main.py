#!/usr/bin/env python3
import sys

def search_horizontal(matrix, keyword):
    return sum((True for row in matrix for i in range(len(row) - len(keyword) + 1) if "".join(row[i:i + len(keyword)]) in [keyword, keyword[::-1]]))

def search_vertical(matrix, keyword):
    return search_horizontal(zip(*matrix), keyword)

def search_diagonal(matrix, keyword):
    rows = len(matrix)
    cols = len(matrix[0])

    count = 0

    for i in range(rows):
        for j in range(cols):
            if i + len(keyword) <= rows and j + len(keyword) <= cols:
                if "".join(matrix[i + k][j + k] for k in range(len(keyword))) in [keyword, keyword[::-1]]:
                    count += 1
            if i + len(keyword) <= rows and j - len(keyword) >= -1:
                if "".join(matrix[i + k][j - k] for k in range(len(keyword))) in [keyword, keyword[::-1]]:
                    count += 1

    return count


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    keyword = "XMAS"

    # ['abcd', 'efgh', 'ijkl'] -> [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l']]
    matrix = [list(line) for line in lines]

    count = 0

    count += search_horizontal(matrix, keyword) + search_vertical(matrix, keyword) + search_diagonal(matrix, keyword)

    # part one
    print(count)


if __name__ == '__main__':
    main()
