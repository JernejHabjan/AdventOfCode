file = open('input.txt', mode='r')
all_of_it = file.read().splitlines()
file.close()

num_trees = 0
curr_x = 0
curr_y = 0
for _ in range(len(all_of_it)):

    if all_of_it[curr_y][curr_x] == "#":
        num_trees += 1

    # move forwards
    curr_y += 1
    curr_x += 3

    # check if we checked all the rows already
    if curr_y == len(all_of_it):
        break

    # don't forget to reset x if it's greater than length
    if curr_x >= len(all_of_it[curr_y]):
        curr_x -= len(all_of_it[curr_y])

print(num_trees)
