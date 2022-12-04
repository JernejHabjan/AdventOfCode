# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
lines = file.read().splitlines()

# close the file
file.close()

print(lines)
sums = []
currentSum = 0
for line in lines:
    if line == "":
        sums.append(currentSum)
        currentSum = 0
    else:
        currentSum += int(line)
sums.sort()
print(sums[len(sums)-1] + sums[len(sums)-2] + sums[len(sums)-3])