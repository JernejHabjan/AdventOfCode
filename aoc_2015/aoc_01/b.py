def aoc_2015_01_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        line = f.read().splitlines()[0]

    current_floor = 0
    res = None
    for step, char in enumerate(line):
        if char == "(":
            current_floor += 1
        if char == ")":
            current_floor -= 1
        if current_floor < 0:
            res = step + 1
            break
    return res


if __name__ == '__main__':
    print(aoc_2015_01_b())
