def aoc_2015_01_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        line = f.read().splitlines()[0]

    return line.count('(') - line.count(')')


if __name__ == '__main__':
    print(aoc_2015_01_a())
