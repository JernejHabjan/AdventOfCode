def aoc_2022_01_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    sums = []
    current_sum = 0
    for line in lines:
        if line == "":
            sums.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line)
    sums.sort()
    return sums[len(sums) - 1] + sums[len(sums) - 2] + sums[len(sums) - 3]


if __name__ == '__main__':
    print(aoc_2022_01_b())
