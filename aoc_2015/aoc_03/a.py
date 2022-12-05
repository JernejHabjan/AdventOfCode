def aoc_2015_03_a():
    import collections

    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        line = f.read().splitlines()[0]

    curr_x = 0
    curr_y = 0

    visited_count = collections.defaultdict(int)
    visited_count[str(curr_x) + "_" + str(curr_y)] += 1
    for chr in line:

        if chr == ">":
            curr_x += 1
        if chr == "<":
            curr_x -= 1
        if chr == "^":
            curr_y -= 1
        if chr == "v":
            curr_y += 1

        visited_count[str(curr_x) + "_" + str(curr_y)] += 1

    count = 0
    for key, val in visited_count.items():
        if val > 0:
            count += 1
    return count


if __name__ == '__main__':
    print(aoc_2015_03_a())
