# Open a file: file
import collections

file = open('input.txt', mode='r')

# read all lines at once
all_of_it = file.read().split("\n\n")

# close the file
file.close()


def is_valid(key, val) -> bool:
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

    if key == "byr":
        if not val.isnumeric():
            return False
        if len(val) != 4:
            return False
        val1 = int(val)
        return 1920 <= val1 <= 2002
    elif key == "iyr":
        if not val.isnumeric():
            return False
        if len(val) != 4:
            return False
        val1 = int(val)
        return 2010 <= val1 <= 2020
    elif key == "eyr":
        if not val.isnumeric():
            return False
        if len(val) != 4:
            return False
        val1 = int(val)
        return 2020 <= val1 <= 2030
    elif key == "hgt":
        if len(val)< 4:
            return False
        val1 = val[:-2]
        if not val1.isnumeric():
            return False
        val1 = int(val1)
        if val[-2:] == "in":
            return 59 <= val1 <= 76
        elif val[-2:] == "cm":
            return 150 <= val1 <= 193
        return False
    elif key == "hcl":
        if len(val) != 7:
            return False
        if val[0] != "#":
            return False
        val1 = val[1:6]
        neki = ["a", "b", "c", "d", "e", "f"]
        for ch in val1:
            if not ch.isnumeric() and ch not in neki:
                return False
        return True
    elif key == "ecl":
        neki = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return val in neki
    elif key == "pid":
        if len(val) != 9:
            return False
        return val.isnumeric()
    elif key == "cid":
        return True


num_correct_passport = 0
for passport in all_of_it:
    another_split = passport.split("\n")
    items = dict()
    for e in another_split:
        itemsList = e.split(" ")
        for item in itemsList:
            key, val = item.split(":")
            if is_valid(key, val):
                items[key] = val
    print(collections.OrderedDict(sorted(items.items())).keys())

    if len(items) == 8:
        num_correct_passport += 1
    if len(items) == 7 and "cid" not in items:
        num_correct_passport += 1
print(num_correct_passport)
