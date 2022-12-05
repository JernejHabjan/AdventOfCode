def aoc_2020_04_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().split("\n\n")

    num_correct_passport = 0
    for passport in lines:
        another_split = passport.split("\n")
        items = dict()
        for e in another_split:
            itemsList = e.split(" ")
            for item in itemsList:
                key, val = item.split(":")
                items[key] = val
        # print(items)
        if len(items) == 8:
            num_correct_passport += 1
        if len(items) == 7 and "cid" not in items:
            num_correct_passport += 1
    return num_correct_passport


if __name__ == '__main__':
    print(aoc_2020_04_a())
