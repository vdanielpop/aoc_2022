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

crt = ''
reg = 0
for k, cycle in enumerate(cycles):
    reg += cycle
    if reg - 1 <= k % 40 <= reg + 1:
        crt += '#'
    else:
        crt += '.'

fout = open("output.txt", "w")
for i in range(0, len(crt), 40):
    fout.write(crt[i:i + 40])
    fout.write('\n')
