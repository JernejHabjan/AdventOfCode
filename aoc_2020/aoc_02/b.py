def aoc_2020_02_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    numCorrectPasswords = 0
    for line in lines:

        neki = line.split("-")
        num_min = int(neki[0])
        remainder = neki[1]

        neki2 = remainder.split(": ")
        remainder2 = neki2[0]
        password = neki2[1]

        neki3 = remainder2.split(" ")
        num_max = int(neki3[0])
        character = neki3[1]

        # print(num_min, num_max, character, password)

        index_min = num_min - 1
        index_max = num_max - 1
        # print(password[index_min], password[index_max])

        min_contains_char = password[index_min] == character
        max_contains_char = password[index_max] == character

        if min_contains_char != max_contains_char:
            numCorrectPasswords += 1

    return numCorrectPasswords


if __name__ == '__main__':
    print(aoc_2021_02_b())
