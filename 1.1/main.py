fin = open("input.txt", "r")
lines = fin.readlines()

max = sum = 0
for line in lines:
    if line == '\n':
        if sum > max:
            max = sum
        sum = 0
    else:
        sum += int(line)


fout = open("output.txt", "w")
fout.write(str(max))