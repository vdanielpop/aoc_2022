class Point:
    def __init__(self, next, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.next = next
        self.positions = {'00'}

    def toString(self):
        return str(self.x) + str(self.y)

    def drag(self):
        if self.next is None:
            return

        dx = self.x - self.next.x
        dy = self.y - self.next.y
        if (abs(dx) == 2 or abs(dy) == 2) and dx != 0 and dy != 0:
            self.next.moveDia(int(dx / abs(dx)), int(dy / abs(dy)))
            self.next.drag()
        elif abs(dx) == 2:
            self.next.moveHor(int(dx / abs(dx)))
            self.next.drag()
        elif abs(dy) == 2:
            self.next.moveVer(int(dy / abs(dy)))
            self.next.drag()

    def moveHor(self, i):
        self.x = self.x + i
        self.positions.add(self.toString())

    def moveVer(self, i):
        self.y = self.y + i
        self.positions.add(self.toString())

    def moveDia(self, i, j):
        self.x += i
        self.y += j
        self.positions.add(self.toString())

    def __repr__(self):
        return str(self.name) + ':' + str(self.x) + ',' + str(self.y)


fin = open("input.txt", "r")
lines = fin.read().splitlines()

prev = None
for i in range(10, 0, -1):
    head = Point(prev, i)
    prev = head

for line in lines:
    parts = line.split(' ')
    moves = int(parts[1])
    while moves > 0:
        if parts[0] == 'U':
            head.moveVer(1)
        elif parts[0] == 'D':
            head.moveVer(-1)
        elif parts[0] == 'L':
            head.moveHor(-1)
        elif parts[0] == 'R':
            head.moveHor(1)
        head.drag()
        moves -= 1

while head.next is not None:
    head = head.next

fout = open("output.txt", "w")
fout.write(str(len(head.positions)))
