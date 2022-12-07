import numpy as np


def get_tuples(lines):
    tuples = []
    for b in lines:
        first, second = b.split(" -> ")
        x1str, y1str = first.split(",")
        x2str, y2str = second.split(",")
        x1, y1, x2, y2 = int(x1str), int(y1str), int(x2str), int(y2str)
        tuples.append((x1, y1, x2, y2))
    return tuples


def find_max_x_y(tuples):
    # find max nr
    total_max_x = 0
    total_max_y = 0
    for x1, y1, x2, y2 in tuples:
        if max(x1, x2) > total_max_x:
            total_max_x = max(x1, x2)
        if max(y1, y2) > total_max_y:
            total_max_y = max(y1, y2)
    return total_max_x + 1, total_max_y + 1


def fill_array(array, tuples, diagonals: bool) -> None:
    for x1, y1, x2, y2 in tuples:
        if x1 == x2:
            # vertical line
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            for i in range(min_y, max_y + 1):
                array[i, x1] += 1
        elif y1 == y2:
            # vertical line
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            for i in range(min_x, max_x + 1):
                array[y1, i] += 1
        else:
            # diagonal
            if not diagonals:
                continue


def count_sum(array):
    overlap_nr = 2
    total = 0
    for row in array:
        for ele in row:
            if ele >= overlap_nr:
                total += 1
    return total


def read_file_and_get_total(diagonals):
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()
    tuples = get_tuples(lines)
    max_x, max_y = find_max_x_y(tuples)
    array = np.full((max_x, max_y), 0)
    fill_array(array, tuples, diagonals=diagonals)
    total = count_sum(array)
    return total


def aoc_2021_05_a():
    return read_file_and_get_total(diagonals=False)


if __name__ == '__main__':
    print(aoc_2021_05_a())
