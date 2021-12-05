# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
lines = file.read().splitlines()

# close the file
file.close()


def getMostAndLeastCommonBitsOfIndex(i, arr):
    bits1 = 0
    bits0 = 0
    for line in arr:
        bit = int(line[i])
        if bit == 1:
            bits1 += 1
        else:
            bits0 += 1
    return (bits1, bits0)


# most1, least1 = getMostAndLeastCommonBitsOfIndex()
# most2, least2 = getMostAndLeastCommonBitsOfIndex()

a = lines.copy()


def oxygen_something(i, arr):
    if len(arr) == 1 or i == len(arr[0]):
        return arr
    bits1, bits0 = getMostAndLeastCommonBitsOfIndex(i, arr)
    # print("oxy", bits1 >= bits0, arr)

    if bits1 >= bits0:
        new_list = list(filter(lambda line: int(line[i]) != 0, arr))
    else:
        new_list = list(filter(lambda line: int(line[i]) != 1, arr))
    return oxygen_something(i + 1, new_list)


def succ_something(i, arr):
    if len(arr) == 1 or i == len(arr[0]):
        return arr
    bits1, bits0 = getMostAndLeastCommonBitsOfIndex(i, arr)
    # print("succ", bits0 >= bits1, arr)
    if bits0 <= bits1:
        new_list = list(filter(lambda line: int(line[i]) != 1, arr))
    else:
        new_list = list(filter(lambda line: int(line[i]) != 0, arr))
    return succ_something(i + 1, new_list)


oxy = int(oxygen_something(0, a.copy())[0], 2)
succ = int(succ_something(0, a.copy())[0], 2)

print(oxy * succ)
