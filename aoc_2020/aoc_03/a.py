def aoc_2020_03_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    num_trees = 0
    curr_x = 0
    curr_y = 0
    for _ in range(len(lines)):

        if lines[curr_y][curr_x] == "#":
            num_trees += 1

        # move forwards
        curr_y += 1
        curr_x += 3

        # check if we checked all the rows already
        if curr_y == len(lines):
            break

        # don't forget to reset x if it's greater than length
        if curr_x >= len(lines[curr_y]):
            curr_x -= len(lines[curr_y])

    return num_trees


if __name__ == '__main__':
    print(aoc_2020_03_a())
