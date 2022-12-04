file = open('input.txt', mode='r')
lines = file.read().splitlines()
file.close()

# print(lines)
sums = []
currentSum = 0
for line in lines:
    if line == "":
        sums.append(currentSum)
        currentSum = 0
    else:
        currentSum += int(line)

print(max(sums))