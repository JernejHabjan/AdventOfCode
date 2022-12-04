with open('input.txt', "r") as f: lines = f.read().splitlines()

mostCommonBits = []
leastCommonBits = []

for i in range(0, len(lines[0])):
    bits1 = 0
    bits0 = 0
    for line in lines:
        bit = int(line[i])
        if bit == 1:
            bits1 += 1
        else:
            bits0 += 1
    if bits1 > bits0:
        mostCommonBits.append("1")
        leastCommonBits.append("0")
    else:
        mostCommonBits.append("0")
        leastCommonBits.append("1")
a = int("".join(mostCommonBits), 2)
b = int("".join(leastCommonBits), 2)

print(a * b)
