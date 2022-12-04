file = open('input.txt', mode='r')
lines = file.read().splitlines()
file.close()


def getIndex(ch):
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
    print(firstHalf, secondHalf)

    # for i in range(len(firstHalf)-1):
    #     charA = getIndex(firstHalf[i])
    #     charB = getIndex(secondHalf[i])
    #     print(firstHalf[i], secondHalf[i], charA, charB)
    #     if charA == charB:
    #         print("same char", charA)
    #         total += charA
    inBoth = set()
    for ch in firstHalf:
        if ch in secondHalf:
            print(ch)
            charA = getIndex(ch)
            inBoth.add(charA)
    total+= sum(inBoth)


print(total)