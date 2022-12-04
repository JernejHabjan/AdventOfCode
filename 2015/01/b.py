file = open('input.txt', mode='r')
line = file.read().splitlines()[0]
file.close()

current_floor = 0
for step, char in enumerate(line):
    if char == "(":
        current_floor += 1
    if char == ")":
        current_floor -= 1
    if current_floor < 0:
        print(step + 1)
        break
