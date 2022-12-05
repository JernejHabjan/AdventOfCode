def aoc_2021_01_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    initial_depth = None
    counter = 0
    for line in lines:
        if initial_depth is not None and int(line) > initial_depth:
            counter += 1
        initial_depth = int(line)

    return counter


if __name__ == '__main__':
    print(aoc_2021_01_a())
