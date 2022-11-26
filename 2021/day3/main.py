#!/usr/bin/env python3
import numpy as np
import sys

with open(sys.argv[1]) as input:
    lines = input.readlines()

lines = [list(line.strip()) for line in lines]

# Part 1
transposed = np.array(lines).T.tolist()

gamma_str = ''.join(['1' if col.count('1') > col.count('0') else '0' for col in transposed])
gamma = int(gamma_str, base = 2)

epsilon_str = ''.join(['0' if c == '1' else '1' for c in gamma_str])
epsilon = int(epsilon_str, base = 2)

print(gamma * epsilon)

# Part 2
def oxygen(lines, depth = 0):
    if len(lines) == 1:
        return int(''.join(lines[0]), base = 2)

    transposed = np.array(lines).T.tolist()

    most_common = '1' if transposed[depth].count('1') >= transposed[depth].count('0') else '0'

    return oxygen([line for line in lines if line[depth] == most_common], depth + 1)

def co2(lines, depth = 0):
    if len(lines) == 1:
        return int(''.join(lines[0]), base = 2)

    transposed = np.array(lines).T.tolist()

    most_common = '1' if transposed[depth].count('1') < transposed[depth].count('0') else '0'

    return co2([line for line in lines if line[depth] == most_common], depth + 1)

print(oxygen(lines) * co2(lines))
