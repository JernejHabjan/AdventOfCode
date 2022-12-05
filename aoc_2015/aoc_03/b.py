def _exec_present(chr, curr_x, curr_y, visited_count):
    if chr == ">":
        curr_x += 1
    if chr == "<":
        curr_x -= 1
    if chr == "^":
        curr_y -= 1
    if chr == "v":
        curr_y += 1

    visited_count[str(curr_x) + "_" + str(curr_y)] += 1
    return curr_x, curr_y


def aoc_2015_03_b():
    import collections

    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        line = f.read().splitlines()[0]

    curr_x = 0
    curr_y = 0

    curr_x_robot = 0
    curr_y_robot = 0

    visited_count = collections.defaultdict(int)
    visited_count[str(curr_x) + "_" + str(curr_y)] += 1

    for i in range(0, len(line), 2):
        curr_x, curr_y = _exec_present(line[i], curr_x, curr_y, visited_count)
        curr_x_robot, curr_y_robot = _exec_present(line[i + 1], curr_x_robot, curr_y_robot, visited_count)

    count = 0
    for key, val in visited_count.items():
        if val > 0:
            count += 1
    return count


if __name__ == '__main__':
    print(aoc_2015_03_b())
