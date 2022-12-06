def aoc_2020_01_b():
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
            if two > nr:
                continue
            if one + two > nr:
                continue
            for three_str in lines:
                three = int(three_str)
                if one + two + three == nr:
                    res = one * two * three
                    break
    return res


if __name__ == '__main__':
    print(aoc_2020_01_b())
