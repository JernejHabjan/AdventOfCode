def get_row(line, low_idx, high_idx, back_letter, front_letter, math):
    # print(line, low_idx, high_idx)
    if len(line) == 0:
        return low_idx
    if line[0] == back_letter:
        # print("moving back")
        return get_row(line[1:], math.ceil((low_idx + high_idx) / 2), high_idx, back_letter, front_letter,
                       math)  # upper half

    if line[0] == front_letter:
        # print("moving front")
        return get_row(line[1:], low_idx, math.floor((low_idx + high_idx) / 2), back_letter, front_letter,
                       math)  # lower half


def get_col(line, low_idx, high_idx):
    # print(line, low_idx, high_idx)
    # if line[0] == "R":
    #        return get_col(line, len(line)/2, ) # upper half

    pass


def aoc_2020_05_b():
    import math

    from numpy import sort

    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    all_ids = []
    for line in lines:
        row = get_row(line[:7], 0, 127, "B", "F", math)
        col = get_row(line[-3:], 0, 7, "R", "L", math)
        all_ids.append(row * 8 + col)

    all_ids = sort(all_ids)
    res = None
    for i in range(len(all_ids) - 2):
        if all_ids[i + 1] - all_ids[i] == 2:
            res = all_ids[i] + 1
            break
    return res


if __name__ == '__main__':
    print(aoc_2020_05_b())
