def aoc_2022_07_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    res = "NOT_FOUND"
    return res


if __name__ == '__main__':
    print(aoc_2022_07_b())
