import math

# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
lines = file.read().splitlines()

# close the file
file.close()
all = 0
for line in lines:

    vowels = line.count("a") + line.count("e") + line.count("i") + line.count("o") + line.count("u")
    if vowels < 3:
        continue

    invalid_chars = False

    contains_double_letter = False
    prev_chr = None

    for chr in line:
        if prev_chr is None:
            prev_chr = chr
            continue

        if prev_chr == "a" and chr == "b" or prev_chr == "c" and chr == "d" or prev_chr == "p" and chr == "q" or prev_chr == "x" and chr == "y":
            invalid_chars = True
            break

        if prev_chr == chr:
            contains_double_letter = True
        prev_chr = chr

    if invalid_chars:
        continue
    if not contains_double_letter:
        continue


    all += 1
print(all)
