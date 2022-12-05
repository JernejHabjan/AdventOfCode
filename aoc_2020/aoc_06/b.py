def aoc_2020_06_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().split("\n\n")

    total = 0
    for group in lines:
        another_split = group.split("\n")
        items = None
        for e in another_split:
            items_current_line = set()
            for chr in e:
                items_current_line.add(chr)

            if items is None:
                items = items_current_line
            else:
                items = items.intersection(items_current_line)
        total += len(items)

    return total


if __name__ == '__main__':
    print(aoc_2020_06_b())
