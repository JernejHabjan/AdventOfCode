# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
lines = file.read().splitlines()

# close the file
file.close()

initialDepth = None
counter = 0
for line in lines:
    if initialDepth is not None and int(line) > initialDepth:
        counter += 1
    initialDepth = int(line)

print(counter)
