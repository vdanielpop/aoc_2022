class Node:
    def __init__(self, name: str, size: int, parent=None):
        self.size = size
        self.parent = parent
        self.name = name
        self.children = []

    def __repr__(self):
        return self.name + ' ' + str(self.size)

    def getChildByName(self, name: str):
        for child in self.children:
            if child.name == name:
                return child

    def getFullName(self):
        if self.parent is None:
            return self.name
        return self.parent.getFullName() + '/' + self.name


def readTree(lines):
    root = None
    cur = None
    for line in lines:
        if line.startswith('$ cd'):
            parts = line.split(' ')
            if parts[2][0] == '.':
                cur = cur.parent
            elif root is None:
                root = Node(parts[2], 0)
                cur = root
            else:
                cur = cur.getChildByName(parts[2])
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('dir'):
            parts = line.split(' ')
            n = Node(parts[1], 0, cur)
            cur.children.append(n)
        else:
            parts = line.split(' ')
            n = Node(parts[1], int(parts[0]), cur)
            cur.children.append(n)

    return root


def computeSizes(n: Node, sizes):
    if n.size != 0:
        return n.size
    else:
        size = 0
        for child in n.children:
            size += computeSizes(child, sizes)
        sizes[n.getFullName()] = size
        return size


fin = open("input.txt", "r")
lines = fin.read().splitlines()
root = readTree(lines)
sizes = {}
computeSizes(root, sizes)
# Cool stuff, for filtering dics
rootSize = sizes[root.name]
candidates = {k: v for k, v in sizes.items() if v >= 30_000_000 - (70_000_000 - rootSize)}
sortedCandidates = sorted(candidates.items(), key=lambda item: item[1])
dirsize = list(sortedCandidates)[0][1]

fout = open("output.txt", "w")
fout.write(str(dirsize))
