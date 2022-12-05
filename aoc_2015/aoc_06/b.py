def aoc_2015_06_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    arr_size_y = 1000
    arr_size_x = 1000
    arr = [[0 for i in range(arr_size_x)] for j in range(arr_size_y)]

    for line in lines:

        neki = line.split(" through ")

        if "turn off" in line:
            neki1 = neki[0].split("turn off ")
        if "turn on" in line:
            neki1 = neki[0].split("turn on ")
        if "toggle" in line:
            neki1 = neki[0].split("toggle ")

        min_x, min_y = neki1[1].split(",")
        max_x, max_y = neki[1].split(",")
        min_x, min_y, max_x, max_y = int(min_x), int(min_y), int(max_x), int(max_y)
        # print(min_x, min_y, max_x, max_y)

        if "turn off" in line:
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    arr[y][x] -= 1
                    if arr[y][x] < 0:
                        arr[y][x] = 0
            pass
        if "turn on" in line:
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    arr[y][x] += 1
        if "toggle" in line:
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    arr[y][x] += 2

    count = 0
    for y in range(arr_size_y):
        for x in range(arr_size_x):
            count += arr[y][x]
    return count


if __name__ == '__main__':
    print(aoc_2015_06_b())
