#!/usr/bin/env python3
from collections import defaultdict
import sys


def exec_cd(directory, pwd):
    if directory == '..':
        pwd = '/'.join(pwd.split('/')[:-2]) + '/'
    elif directory == '/':
        pwd = '/'
    else:
        pwd += directory + '/'
    return pwd


def parse_line(line, FILE_TO_SIZE, pwd):
    if line.startswith('$ cd '):
        dir = line.split('$ cd ')[1]
        pwd = exec_cd(dir, pwd)
    elif line.startswith('$ ls'):
        pass
    elif line.startswith('dir '):
        dir = pwd + line.split('dir ')[1]
    else:
        size, file_basename = line.split(' ')
        file = pwd + file_basename
        FILE_TO_SIZE[file] = int(size)
    return pwd


def parse_input(lines, *, FILE_TO_SIZE, pwd):
    for line in lines:
        pwd = parse_line(line, FILE_TO_SIZE, pwd)
    return FILE_TO_SIZE


def main():
    with open(sys.argv[1]) as input:
        lines = input.read().splitlines()

    FILE_TO_SIZE = parse_input(lines, FILE_TO_SIZE={}, pwd='/')
    # DIRECTORIES = list(set(['/'.join(file.split('/')[:-1]) +
    #                         '/' for file in FILE_TO_SIZE.keys()]))
    DIRECTORY_TO_SIZE = defaultdict(int)

    for file, size in FILE_TO_SIZE.items():
        components = file.split('/')[:-1]
        for i in range(1, len(components) + 1):
            directory = '/'.join(components[:i])
            DIRECTORY_TO_SIZE[directory] += FILE_TO_SIZE[file]

    # Minor fixes for '/' canonicalization
    DIRECTORY_TO_SIZE['/'] = DIRECTORY_TO_SIZE['']
    del DIRECTORY_TO_SIZE['']

    # Part 1
    print(sum([value for value in DIRECTORY_TO_SIZE.values() if value <= 100000]))

    # Part 2
    TOTAL_DISK = 70000000
    USED_DISK = DIRECTORY_TO_SIZE['/']
    AVAILABLE_DISK = TOTAL_DISK - USED_DISK

    print(next(value for value in sorted(DIRECTORY_TO_SIZE.values())
          if (AVAILABLE_DISK + value) >= 30000000))


if __name__ == '__main__':
    main()
