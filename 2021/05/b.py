file = open('input.txt', mode='r')
lines = file.read().splitlines()
file.close()

# find max nr
totalMaxX = 0
totalMaxY = 0
for b in lines:
    first, second = b.split(" -> ")
    x1str, y1str = first.split(",")
    x2str, y2str = second.split(",")
    x1, y1, x2, y2 = int(x1str), int(y1str), int(x2str), int(y2str)
    if (max(x1, x2) > totalMaxX):
        totalMaxX = max(x1, x2)
    if (max(y1, y2) > totalMaxY):
        totalMaxY = max(y1, y2)

# initialize empty array
arr = []
for i in range(0, totalMaxX + 1):
    arr.append([])
    for j in range(0, totalMaxY + 1):
        arr[i].append(0)

# iterate
for b in lines:
    first, second = b.split(" -> ")
    x1str, y1str = first.split(",")
    x2str, y2str = second.split(",")
    x1, y1, x2, y2 = int(x1str), int(y1str), int(x2str), int(y2str)
    miny = min(y1, y2)
    maxy = max(y1, y2)
    minx = min(x1, x2)
    maxx = max(x1, x2)
    if x1 == x2:
        # vertical line
        for i in range(miny, maxy + 1):
            arr[x1][i] += 1
            # print("increased x")
    elif y1 == y2:
        # vertical line
        for i in range(minx, maxx + 1):
            arr[i][y1] += 1
            # print("increased y")
    else:
        print("diagonal", x1, y1, x2, y2)
        currX = minx
        currY = miny
        for i in range(minx, maxx + 1):
            arr[currX][currY] += 1
            print("increased", currX, currY)
            currY += 1
            currX += 1

            # debug print
            for l in arr:
                print(("".join(str(x) for x in l)).replace("0", "."))

summo = 0
for l in arr:
    for l1 in l:
        if l1 >= 2:
            summo += 1
        # print(l1)
    # print(("".join(str(x) for x in l)).replace("0","."))
print(summo)
