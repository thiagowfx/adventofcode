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


def search_double_mas(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    count = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if matrix[i][j] != 'A':
                continue

            # look at a QWERTY keyboard to make sense of these variable names
            q = matrix[i - 1][j - 1]
            e = matrix[i - 1][j + 1]
            z = matrix[i + 1][j - 1]
            c = matrix[i + 1][j + 1]
            edges = [q, e, z, c]

            if edges.count('M') != 2 or edges.count('S') != 2:
                continue

            if q == e or q == z:
                count += 1

    return count



def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    keyword = "XMAS"

    # ['abcd', 'efgh', 'ijkl'] -> [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l']]
    matrix = [list(line) for line in lines]

    # part one
    print(search_horizontal(matrix, keyword) + search_vertical(matrix, keyword) + search_diagonal(matrix, keyword))

    # part two
    print(search_double_mas(matrix))


if __name__ == '__main__':
    main()
