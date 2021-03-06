import math

# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
all_of_it = file.read().splitlines()

# close the file
file.close()


def get_row(line, low_idx, high_idx, back_letter, front_letter):
    # print(line, low_idx, high_idx)
    if len(line) == 0:
        return low_idx
    if line[0] == back_letter:
        #print("moving back")
        return get_row(line[1:], math.ceil((low_idx+high_idx) / 2), high_idx, back_letter, front_letter)  # upper half

    if line[0] == front_letter:
        #print("moving front")
        return get_row(line[1:], low_idx, math.floor((low_idx+high_idx) / 2), back_letter, front_letter)  # lower half

def get_col(line, low_idx, high_idx):
    #print(line, low_idx, high_idx)
    # if line[0] == "R":
    #        return get_col(line, len(line)/2, ) # upper half

    pass


highest_seat_id = 0
for line in all_of_it:
    row = get_row(line[:7], 0, 127, "B", "F")
    col = get_row(line[-3:], 0, 7, "R", "L")

    if highest_seat_id < row*8+ col:
        highest_seat_id = row*8+ col


print(highest_seat_id)