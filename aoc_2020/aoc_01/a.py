def aoc_2020_01_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()
    res = None
    nr = 2020
    for one_str in lines:
        one = int(one_str)
        if one > nr:
            continue
        for two_str in lines:
            two = int(two_str)
            if one + two == nr:
                res = one * two
                break
    return res


if __name__ == '__main__':
    print(aoc_2020_01_a())
