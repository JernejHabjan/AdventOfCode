with open('input.txt', "r") as f: lines = f.read().splitlines()

lost = 0
draw = 3
win = 6

opponent = ["A", "B", "C"]
me = ["X", "Y", "Z"]
total = 0
for line in lines:
    (a, b) = tuple(line.split(' '))
    idxOpponent = opponent.index(a)
    idxMe = me.index(b)
    total += idxMe + 1

    if a == "A" and b == "X" or a == "B" and b == "Y" or a == "C" and b == "Z":
        # tie
        total += draw
    elif a == "A" and b == "Z" or a == "B" and b == "X" or a == "C" and b == "Y":
        # lose
        total += lost
    else:
        # won
        total += win
print(total)
