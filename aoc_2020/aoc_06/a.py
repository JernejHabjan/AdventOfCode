def aoc_2020_06_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().split("\n\n")

    total = 0
    for group in lines:
        another_split = group.split("\n")
        items = set()
        for e in another_split:
            for chr in e:
                items.add(chr)
        total += len(items)

    return total


if __name__ == '__main__':
    print(aoc_2020_06_a())
