file = open('input.txt', mode='r')
lines = file.read().splitlines()
file.close()


def get_index(ch):
    if ch.islower():
        ordIndex = ord(ch) - 96
    else:
        ordIndex = ord(ch) - 64 + 26
    return ordIndex


total = 0
for line in lines:
    halfLength = int(len(line) / 2)
    # print(halfLength)
    firstHalf = line[0:halfLength]
    secondHalf = line[halfLength:len(line)]
    # print(firstHalf, secondHalf)

    inBoth = set()
    for ch in firstHalf:
        if ch in secondHalf:
            # print(ch)
            charA = get_index(ch)
            inBoth.add(charA)
    total += sum(inBoth)

print(total)
