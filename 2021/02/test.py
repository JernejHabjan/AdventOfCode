# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
lines = file.read().splitlines()

# close the file
file.close()

vec = dict(x=0, y=0)
for line in lines:
    splitLine = line.split(" ")
    direction = splitLine[0]
    amount = int(splitLine[1])
    if direction == "up":
        vec["y"] -= amount
    elif direction == "down":
        vec["y"] += amount
    elif direction == "forward":
        vec["x"] += amount
print(vec['x'] * vec['y'])