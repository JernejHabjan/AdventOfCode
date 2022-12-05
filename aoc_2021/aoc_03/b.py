def _get_most_and_least_common_bits_of_index(i, arr):
    bits1 = 0
    bits0 = 0
    for line in arr:
        bit = int(line[i])
        if bit == 1:
            bits1 += 1
        else:
            bits0 += 1
    return bits1, bits0


def _oxygen_something(i, arr):
    if len(arr) == 1 or i == len(arr[0]):
        return arr
    bits1, bits0 = _get_most_and_least_common_bits_of_index(i, arr)
    # print("oxy", bits1 >= bits0, arr)

    if bits1 >= bits0:
        new_list = list(filter(lambda line: int(line[i]) != 0, arr))
    else:
        new_list = list(filter(lambda line: int(line[i]) != 1, arr))
    return _oxygen_something(i + 1, new_list)


def succ_something(i, arr):
    if len(arr) == 1 or i == len(arr[0]):
        return arr
    bits1, bits0 = _get_most_and_least_common_bits_of_index(i, arr)
    # print("succ", bits0 >= bits1, arr)
    if bits0 <= bits1:
        new_list = list(filter(lambda line: int(line[i]) != 1, arr))
    else:
        new_list = list(filter(lambda line: int(line[i]) != 0, arr))
    return succ_something(i + 1, new_list)


def aoc_2021_03_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    a = lines.copy()
    oxy = int(_oxygen_something(0, a.copy())[0], 2)
    succ = int(succ_something(0, a.copy())[0], 2)

    return oxy * succ


if __name__ == '__main__':
    print(aoc_2021_03_b())
