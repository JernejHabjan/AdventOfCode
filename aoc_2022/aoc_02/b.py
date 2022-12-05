def aoc_2022_02_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

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
            should_be_my_index = idxOpponent - 1

        elif b == "Y":
            # draw
            total += draw
            should_be_my_index = idxOpponent

        else:
            # win
            total += win
            should_be_my_index = idxOpponent + 1

        if should_be_my_index == -1:
            should_be_my_index = len(me) - 1
        elif should_be_my_index == len(me):
            should_be_my_index = 0

        total += should_be_my_index + 1

    return total


if __name__ == '__main__':
    print(aoc_2022_02_b())
