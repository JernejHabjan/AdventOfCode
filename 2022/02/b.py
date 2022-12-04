file = open('input.txt', mode='r')
lines = file.read().splitlines()
file.close()

lost = 0
draw = 3
win = 6

opponent = ["A", "B", "C"]
me = ["X", "Y", "Z"]
total = 0
for line in lines:
    (a, b) = tuple(line.split(' '))
    idxOpponent = opponent.index(a)

    if b == "X":
        # lost
        total += lost
        shouldBeMyIndex = idxOpponent - 1

    elif b == "Y":
        # draw
        total += draw
        shouldBeMyIndex = idxOpponent

    else:
        # win
        total += win
        shouldBeMyIndex = idxOpponent + 1

    if shouldBeMyIndex == -1:
        shouldBeMyIndex = len(me) - 1
    elif shouldBeMyIndex == len(me):
        shouldBeMyIndex = 0

    total += shouldBeMyIndex + 1

print(total)
