def neki(y_move: int, x_move: int, lines) -> int:
    num_trees = 0
    curr_x = 0
    curr_y = 0
    for _ in range(len(lines)):

        if lines[curr_y][curr_x] == "#":
            num_trees += 1

        # move forwards
        curr_y += y_move
        curr_x += x_move

        # check if we checked all the rows already
        if curr_y >= len(lines):
            break

        # don't forget to reset x if it's greater than length
        if curr_x >= len(lines[curr_y]):
            curr_x -= len(lines[curr_y])
    return num_trees


def aoc_2020_03_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()
    return neki(1, 1, lines) * neki(1, 3, lines) * neki(1, 5, lines) * neki(1, 7, lines) * neki(2, 1, lines)


if __name__ == '__main__':
    print(aoc_2020_03_b())
