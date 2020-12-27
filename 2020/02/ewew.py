# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
all_of_it = file.read()

# close the file
file.close()

numCorrectPasswords = 0
split_by_line = all_of_it.split("\n")
for line in split_by_line:

    neki = line.split("-")
    num_min = neki[0]
    remainder = neki[1]

    neki2 = remainder.split(": ")
    remainder2 = neki2[0]
    password = neki2[1]

    neki3 = remainder2.split(" ")
    num_max = neki3[0]
    character = neki3[1]

    print(num_min, num_max, character, password)
    numCharactersInPassword = [ch for ch in password if ch == character]

    if int(num_min) <= len(numCharactersInPassword) <= int(num_max):
        numCorrectPasswords += 1

print(numCorrectPasswords)
