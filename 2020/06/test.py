# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
lines = file.read().split("\n\n")

# close the file
file.close()

all = 0
for group in lines:
    another_split = group.split("\n")
    items = set()
    for e in another_split:
        for chr in e:
            items.add(chr)
    all += len(items)

print(all)
