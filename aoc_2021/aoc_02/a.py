def aoc_2021_02_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    vec = dict(x=0, y=0)
    for line in lines:
        split_line = line.split(" ")
        direction = split_line[0]
        amount = int(split_line[1])
        if direction == "up":
            vec["y"] -= amount
        elif direction == "down":
            vec["y"] += amount
        elif direction == "forward":
            vec["x"] += amount
    return vec['x'] * vec['y']


if __name__ == '__main__':
    print(aoc_2021_02_a())
