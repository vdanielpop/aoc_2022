fin = open("input.txt", "r")
lines = fin.read().splitlines()

sum = 0
for i in range(int(len(lines)/3)):
    x = ord(list(set(lines[i*3]).intersection(set(lines[i*3+1])).intersection(set(lines[i*3+2])))[0])
    sum += x-96 if (97 <= x <= 122) else x - 38

fout = open("output.txt", "w")
fout.write(str(sum))

