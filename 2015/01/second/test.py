# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
all_of_it = file.read().splitlines()[0]

# close the file
file.close()
current_floor = 0
for step, char in enumerate(all_of_it):
    if char == "(":
        current_floor += 1
    if char == ")":
        current_floor -= 1
    if current_floor < 0:
        print(step + 1)
        break
