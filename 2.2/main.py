fin = open("input.txt", "r")
scores = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

result = sum(map(lambda x: scores[x],fin.read().splitlines()))
fout = open("output.txt", "w")
fout.write(str(result))
