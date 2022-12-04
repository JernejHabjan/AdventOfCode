file = open('input.txt', mode='r')
all_of_it = file.read().split("\n\n")
file.close()

num_correct_passport = 0
for passport in all_of_it:
    another_split = passport.split("\n")
    items = dict()
    for e in another_split:
        itemsList = e.split(" ")
        for item in itemsList:
            key, val = item.split(":")
            items[key] = val
    print(items)
    if len(items) == 8:
        num_correct_passport += 1
    if len(items) == 7 and "cid" not in items:
        num_correct_passport += 1
print(num_correct_passport)
