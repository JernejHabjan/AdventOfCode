def aoc_2020_02_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    numCorrectPasswords = 0
    for line in lines:

        neki = line.split("-")
        num_min = neki[0]
        remainder = neki[1]

        neki2 = remainder.split(": ")
        remainder2 = neki2[0]
        password = neki2[1]

        neki3 = remainder2.split(" ")
        num_max = neki3[0]
        character = neki3[1]

        # print(num_min, num_max, character, password)
        numCharactersInPassword = [ch for ch in password if ch == character]

        if int(num_min) <= len(numCharactersInPassword) <= int(num_max):
            numCorrectPasswords += 1

    return numCorrectPasswords


if __name__ == '__main__':
    print(aoc_2020_02_a())
