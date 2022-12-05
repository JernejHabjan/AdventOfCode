def aoc_2015_02_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    total = 0
    for line in lines:
        l, w, h = line.split("x")
        l, w, h = int(l), int(w), int(h)
        one = 2 * l * w
        two = 2 * w * h
        three = 2 * h * l
        total += one + two + three + min(one, two, three) / 2

    return total


if __name__ == '__main__':
    print(aoc_2015_02_a())
