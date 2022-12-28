import numpy as np
import math


class Point:
    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.val = val


def computeScenicScore(i, j, matrix):
    val = matrix[i][j]
    size = int(math.sqrt(matrix.size))
    score = 1
    count = 0

    a = i - 1
    while a >= 0:
        count += 1
        if matrix[a][j] >= val:
            break
        a -= 1
    score *= count

    count = 0
    a = i + 1
    while a <= size - 1:
        count += 1
        if matrix[a][j] >= val:
            break
        a += 1
    score *= count

    count = 0
    a = j - 1
    while a >= 0:
        count += 1
        if matrix[i][a] >= val:
            break
        a -= 1
    score *= count

    count = 0
    a = j + 1
    while a <= size - 1:
        count += 1
        if matrix[i][a] >= val:
            break
        a += 1
    score *= count

    return score


fin = open("input.txt", "r")
lines = fin.read().splitlines()

numbers = []
for line in lines:
    n = len(line)
    parts = list(map(lambda x: int(x), [*line]))
    size = len(parts)
    numbers.append(parts)
matrix = np.array(numbers)

maxScore = 0
for i in range(1, size - 1):
    for j in range(1, size - 1):
        score = computeScenicScore(i, j, matrix)
        if score > maxScore:
            maxScore = score

fout = open("output.txt", "w")
fout.write(str(maxScore))
