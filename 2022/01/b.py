with open('input.txt', "r") as f: lines = f.read().splitlines()

sums = []
currentSum = 0
for line in lines:
    if line == "":
        sums.append(currentSum)
        currentSum = 0
    else:
        currentSum += int(line)
sums.sort()
print(sums[len(sums) - 1] + sums[len(sums) - 2] + sums[len(sums) - 3])
