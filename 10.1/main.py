fin = open("input.txt", "r")
lines = fin.read().splitlines()

cycles = [1]
for line in lines:
    parts = line.split(' ')
    if parts[0] == 'noop':
        cycles.append(0)
    else:
        cycles.append(0)
        cycles.append(int(parts[1]))

checkpoints = [20, 60, 100, 140, 180, 220]
res = sum(map(lambda x: x * sum(cycles[:x]), checkpoints))

fout = open("output.txt", "w")
fout.write(str(res))
