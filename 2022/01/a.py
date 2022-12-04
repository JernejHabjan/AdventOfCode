with open('input.txt', "r") as f: lines = f.read().splitlines()


sums = []
currentSum = 0
for line in lines:
    if line == "":
        sums.append(currentSum)
        currentSum = 0
    else:
        currentSum += int(line)

print(max(sums))
