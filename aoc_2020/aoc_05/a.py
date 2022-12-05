def _get_row(line, low_idx, high_idx, back_letter, front_letter, math):
    # print(line, low_idx, high_idx)
    if len(line) == 0:
        return low_idx
    if line[0] == back_letter:
        # print("moving back")
        return _get_row(line[1:], math.ceil((low_idx + high_idx) / 2), high_idx, back_letter,
                        front_letter, math)  # upper half

    if line[0] == front_letter:
        # print("moving front")
        return _get_row(line[1:], low_idx, math.floor((low_idx + high_idx) / 2), back_letter,
                        front_letter, math)  # lower half


def _get_col(line, low_idx, high_idx):
    # print(line, low_idx, high_idx)
    # if line[0] == "R":
    #        return get_col(line, len(line)/2, ) # upper half

    pass


def aoc_2020_05_a():
    import math

    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    highest_seat_id = 0
    for line in lines:
        row = _get_row(line[:7], 0, 127, "B", "F", math)
        col = _get_row(line[-3:], 0, 7, "R", "L", math)

        if highest_seat_id < row * 8 + col:
            highest_seat_id = row * 8 + col

    return highest_seat_id


if __name__ == '__main__':
    print(aoc_2020_05_a())
