class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def isTouching(self, p):
        return self.x == p.x or self.y == p.y

    def toString(self):
        return str(self.x) + str(self.y)

    def maxDistanceFrom(self, p):
        return max(abs(self.x - p.x), abs(self.y - p.y))

    def __repr__(self):
        return str(self.x) + ',' + str(self.y)


fin = open("input.txt", "r")
lines = fin.read().splitlines()

head = Point()
tail = Point()

positions = {'00'}
for line in lines:
    parts = line.split(' ')
    moves = int(parts[1])
    while moves > 0:
        if parts[0] == 'U':
            head.y += 1
            if head.maxDistanceFrom(tail) == 2:
                tail.x = head.x
                tail.y += 1
                positions.add(tail.toString())
        elif parts[0] == 'D':
            head.y -= 1
            if head.maxDistanceFrom(tail) == 2:
                tail.x = head.x
                tail.y -= 1
                positions.add(tail.toString())
        elif parts[0] == 'L':
            head.x -= 1
            if head.maxDistanceFrom(tail) == 2:
                tail.y = head.y
                tail.x -= 1
                positions.add(tail.toString())
        elif parts[0] == 'R':
            head.x += 1
            if head.maxDistanceFrom(tail) == 2:
                tail.y = head.y
                tail.x += 1
                positions.add(tail.toString())
        moves -= 1

fout = open("output.txt", "w")
fout.write(str(len(positions)))
