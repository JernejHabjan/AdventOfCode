def aoc_2021_05_a():
    import pathlib

    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    # find max nr
    total_max_x = 0
    total_max_y = 0
    for b in lines:
        first, second = b.split(" -> ")
        x1str, y1str = first.split(",")
        x2str, y2str = second.split(",")
        x1, y1, x2, y2 = int(x1str), int(y1str), int(x2str), int(y2str)
        if max(x1, x2) > total_max_x:
            total_max_x = max(x1, x2)
        if max(y1, y2) > total_max_y:
            total_max_y = max(y1, y2)

    # initialize empty array
    arr = []
    for i in range(0, total_max_x + 1):
        arr.append([])
        for j in range(0, total_max_y + 1):
            arr[i].append(0)

    # iterate
    for b in lines:
        first, second = b.split(" -> ")
        x1str, y1str = first.split(",")
        x2str, y2str = second.split(",")
        x1, y1, x2, y2 = int(x1str), int(y1str), int(x2str), int(y2str)
        if x1 == x2:
            # vertical line
            miny = min(y1, y2)
            maxy = max(y1, y2)
            for i in range(miny, maxy + 1):
                arr[x1][i] += 1
                # print("increased x")
        if y1 == y2:
            # vertical line
            minx = min(x1, x2)
            maxx = max(x1, x2)
            for i in range(minx, maxx + 1):
                arr[i][y1] += 1
                # print("increased y")
    summo = 0
    for l in arr:
        for l1 in l:
            if l1 >= 2:
                summo += 1
            # print(l1)
        # print(("".join(str(x) for x in l)).replace("0", "."))
    return summo


if __name__ == '__main__':
    print(aoc_2021_05_a())
