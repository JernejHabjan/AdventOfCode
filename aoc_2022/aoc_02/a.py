def aoc_2022_02_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    lost = 0
    draw = 3
    win = 6

    me = ["X", "Y", "Z"]
    total = 0
    for line in lines:
        (a, b) = tuple(line.split(' '))
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
    return total


if __name__ == '__main__':
    print(aoc_2022_02_a())
