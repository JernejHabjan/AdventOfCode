def aoc_2022_03_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    def get_index(ch):
        if ch.islower():
            ordIndex = ord(ch) - 96
        else:
            ordIndex = ord(ch) - 64 + 26
        return ordIndex

    total = 0
    for line in lines:
        halfLength = int(len(line) / 2)
        first_half = line[0:halfLength]
        second_half = line[halfLength:len(line)]

        inBoth = set()
        for character in first_half:
            if character in second_half:
                char_a = get_index(character)
                inBoth.add(char_a)
        total += sum(inBoth)

    return total


if __name__ == '__main__':
    print(aoc_2022_03_a())
