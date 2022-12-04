file = open('input.txt', mode='r')
lines = file.read().splitlines()
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
