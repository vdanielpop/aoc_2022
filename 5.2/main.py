def addLineToList(stackList: list, line: str):
    maxStackLength = int(len(line) / 4)
    currentStackLength = len(stackList)
    if (currentStackLength < maxStackLength):
        for l in range(currentStackLength, maxStackLength):
            stackList.append([])

    for i in range(1, len(line), 4):
        if line[i] != ' ':
            stackList[int(i / 4)] = [line[i]] + stackList[int(i / 4)]


def processMove(stackList: list, line: str):
    parts = line.split(' ')
    moveCount = int(parts[1])
    source = int(parts[3]) - 1
    dest = int(parts[5]) - 1
    if moveCount == 1:
        el = stackList[source].pop()
        stackList[dest].append(el)
    else:
        temp = []
        for move in range(0, moveCount):
            el = stackList[source].pop()
            temp = [el] + temp
        stackList[dest] = stackList[dest] + temp


fin = open("input.txt", "r")
lines = fin.readlines()

stackList = []
for k, line in enumerate(lines):
    if line[0] == 'm':
        processMove(stackList, line)
    elif line.__contains__('['):
        addLineToList(stackList, line)


res = ''
for stack in stackList:
    res = res + stack.pop()

fout = open("output.txt", "w")
fout.write(res)
