fin = open("input.txt", "r")
lines = fin.readlines()

maxi = []
s = 0
for line in lines:
    if line == '\n':
        maxi.append(s)
        s = 0
    else:
        s += int(line)

maxi.sort(reverse=True)

fout = open("output.txt", "w")
fout.write(str(sum(maxi[:3])))
