fin = open("input.txt", "r")
scores = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

result = sum(map(lambda x: scores[x],fin.read().splitlines()))
fout = open("output.txt", "w")
fout.write(str(result))
