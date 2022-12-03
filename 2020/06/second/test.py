# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
lines = file.read().split("\n\n")

# close the file
file.close()

all = 0
for group in lines:
    another_split = group.split("\n")
    items = None
    for e in another_split:
        items_current_line = set()
        for chr in e:
            items_current_line.add(chr)

        if items == None:
            items = items_current_line
        else:
            items = items.intersection(items_current_line)
    all += len(items)

print(all)
