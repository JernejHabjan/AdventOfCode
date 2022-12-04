file = open('input.txt', mode='r')
lines = file.read().split("\n\n")
file.close()

total = 0
for group in lines:
    another_split = group.split("\n")
    items = None
    for e in another_split:
        items_current_line = set()
        for chr in e:
            items_current_line.add(chr)

        if items is None:
            items = items_current_line
        else:
            items = items.intersection(items_current_line)
    total += len(items)

print(total)
