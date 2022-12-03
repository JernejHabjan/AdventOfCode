# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
lines = file.read().splitlines()

# close the file
file.close()
arr_size_y = 1000
arr_size_x = 1000
arr = [[False for i in range(arr_size_x)] for j in range(arr_size_y)]



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
    print(min_x, min_y, max_x, max_y)

    if "turn off" in line:
        for y in range(min_y,max_y+ 1):
            for x in range(min_x, max_x+ 1):
                arr[y][x]= False
        pass
    if "turn on" in line:
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x +1 ):
                arr[y][x] = True
    if "toggle" in line:
        for y in range(min_y, max_y+ 1):
            for x in range(min_x, max_x+ 1):
                arr[y][x] = not arr[y][x]

count = 0
for y in range(arr_size_y):
    for x in range(arr_size_x):
        if arr[y][x]:
            count+=1
print(count)
# print(arr)
