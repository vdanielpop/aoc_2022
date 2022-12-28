import numpy as np


class Point:
    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.val = val


def processElement(val, i, j, visibles, oppositeVisibles):
    if len(visibles) == 0 or val > visibles[-1].val:
        curr = Point(i, j, val)
        visibles.append(curr)

        while len(oppositeVisibles) > 0:
            oppositeVisibles.pop()
        oppositeVisibles.append(curr)
    else:
        while len(oppositeVisibles) > 0 and oppositeVisibles[-1].val <= val:
            oppositeVisibles.pop()
        oppositeVisibles.append(Point(i, j, val))

def fillInMask(mask, list):
    for el in list:
        if mask[el.i][el.j] == 0:
            mask[el.i][el.j] = 1

fin = open("input.txt", "r")
lines = fin.read().splitlines()

numbers = []
for line in lines:
    n = len(line)
    parts = list(map(lambda x: int(x), [*line]))
    size = len(parts)
    numbers.append(parts)
matrix = np.array(numbers)
mask = np.empty([size, size])
mask.fill(0)

for i in range(0, size):
    visibleRow = []
    visibleCol = []
    oppositeVisibleRow = []
    oppositeVisibleCol = []
    for j in range(0, size):
        processElement(matrix[i][j], i, j, visibleRow, oppositeVisibleRow)
        processElement(matrix[j][i], j, i, visibleCol, oppositeVisibleCol)
    fillInMask(mask, visibleRow)
    fillInMask(mask, visibleCol)
    fillInMask(mask, oppositeVisibleRow)
    fillInMask(mask, oppositeVisibleCol)

count = 0
for i in range(0, size):
    for j in range(0, size):
        if mask[i][j] == 1:
            count += 1

fout = open("output.txt", "w")
fout.write(str(count))
