fin = open("input.txt", "r")
input = fin.readline()

length = len(input)

for i in range(0, length - 4):
    window: str = input[i:i+4]
    if len(set(window)) == len(window):
        res = i+4
        break

fout = open("output.txt", "w")
fout.write(str(res))
