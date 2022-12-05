def aoc_2021_03_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    most_common_bits = []
    least_common_bits = []

    for i in range(0, len(lines[0])):
        bits1 = 0
        bits0 = 0
        for line in lines:
            bit = int(line[i])
            if bit == 1:
                bits1 += 1
            else:
                bits0 += 1
        if bits1 > bits0:
            most_common_bits.append("1")
            least_common_bits.append("0")
        else:
            most_common_bits.append("0")
            least_common_bits.append("1")
    a = int("".join(most_common_bits), 2)
    b = int("".join(least_common_bits), 2)

    return a * b


if __name__ == '__main__':
    print(aoc_2021_03_a())
