# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
all_of_it = file.read().splitlines()

# close the file
file.close()


def neki(y_move: int, x_move: int) -> int:
    num_trees = 0
    curr_x = 0
    curr_y = 0
    for _ in range(len(all_of_it)):

        if all_of_it[curr_y][curr_x] == "#":
            num_trees += 1

        # move forwards
        curr_y += y_move
        curr_x += x_move

        # check if we checked all the rows already
        if curr_y >= len(all_of_it):
            break

        # don't forget to reset x if it's greater than length
        if curr_x >= len(all_of_it[curr_y]):
            curr_x -= len(all_of_it[curr_y])
    return num_trees


print(neki(1, 1) * neki(1, 3) * neki(1, 5) * neki(1, 7) * neki(2, 1))
