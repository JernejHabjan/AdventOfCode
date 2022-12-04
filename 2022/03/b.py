with open('input.txt', "r") as f: lines = f.read().splitlines()


def getIndex(ch):
    if ch.islower():
        ordIndex = ord(ch) - 96
    else:
        ordIndex = ord(ch) - 64 + 26
    return ordIndex


total = 0
for i in range(0, len(lines), 3):
    line1 = lines[i]
    line2 = lines[i + 1]
    line3 = lines[i + 2]
    print(line1, line2, line3)

    inBoth = set()
    for ch in line1:
        if ch in line2 and ch in line3:
            print(ch)
            charA = getIndex(ch)
            inBoth.add(charA)
    total += sum(inBoth)

print(total)
