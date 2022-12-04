file = open('input.txt', mode='r')
lines = file.read().split("\n\n")
file.close()

total = 0
for group in lines:
    another_split = group.split("\n")
    items = set()
    for e in another_split:
        for chr in e:
            items.add(chr)
    total += len(items)

print(total)
