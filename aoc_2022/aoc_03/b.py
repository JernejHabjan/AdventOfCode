def aoc_2022_03_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    def get_index(character):
        if character.islower():
            ord_index = ord(character) - 96
        else:
            ord_index = ord(character) - 64 + 26
        return ord_index

    total = 0
    for i in range(0, len(lines), 3):
        line1 = lines[i]
        line2 = lines[i + 1]
        line3 = lines[i + 2]
        # print(line1, line2, line3)

        in_both = set()
        for ch in line1:
            if ch in line2 and ch in line3:
                # print(ch)
                charA = get_index(ch)
                in_both.add(charA)
        total += sum(in_both)

    return total


if __name__ == '__main__':
    print(aoc_2022_03_b())
