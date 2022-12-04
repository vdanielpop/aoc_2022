fin = open("input.txt", "r")
lines = fin.read().splitlines()

res = sum(map(
    lambda x: x-96 if (97 <= x <= 122) else x - 38,
    map(lambda x: ord(list(set(x[int(len(x)/2):]).intersection(set(x[:int(len(x)/2)])))[0]), lines)
))

fout = open("output.txt", "w")
fout.write(str(res))
