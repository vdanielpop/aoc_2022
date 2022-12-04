fin = open("input.txt", "r")
lines = fin.read().splitlines()

cnt = 0
for line in lines:
    elves = line.split(',')
    parts = list(map(int, elves[0].split('-')))
    first = set(range(parts[0], parts[1]+1))
    parts = list(map(int, elves[1].split('-')))
    second = set(range(parts[0], parts[1]+1))
    inters = first.intersection(second)
    if inters.__eq__(first) or inters.__eq__(second):
        cnt += 1


fout = open("output.txt", "w")
fout.write(str(cnt))

