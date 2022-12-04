file = open('input.txt', mode='r')
all_of_it = file.read()
file.close()

numCorrectPasswords = 0
split_by_line = all_of_it.split("\n")
for line in split_by_line:

    neki = line.split("-")
    num_min = int(neki[0])
    remainder = neki[1]

    neki2 = remainder.split(": ")
    remainder2 = neki2[0]
    password = neki2[1]

    neki3 = remainder2.split(" ")
    num_max = int(neki3[0])
    character = neki3[1]

    print(num_min, num_max, character, password)

    index_min = num_min - 1
    index_max = num_max - 1
    print(password[index_min], password[index_max])

    min_contains_char = password[index_min] == character
    max_contains_char = password[index_max] == character

    if min_contains_char != max_contains_char:
        numCorrectPasswords += 1

print(numCorrectPasswords)
