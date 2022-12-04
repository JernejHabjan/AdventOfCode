file = open('input.txt', mode='r')
lines = file.read().splitlines()
file.close()

initialDepth = None
counter = 0
for line in lines:
    if initialDepth is not None and int(line) > initialDepth:
        counter += 1
    initialDepth = int(line)

print(counter)
