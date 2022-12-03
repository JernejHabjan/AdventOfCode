import collections

# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
line = file.read().splitlines()[0]

# close the file
file.close()

curr_x = 0
curr_y = 0

curr_x_robot = 0
curr_y_robot = 0


visited_count = collections.defaultdict(int)
visited_count[str(curr_x)+"_"+str(curr_y)] += 1

def exec_present(chr, curr_x, curr_y):
    if chr == ">":
        curr_x +=1
    if chr == "<":
        curr_x -= 1
    if chr == "^":
        curr_y -=1
    if chr == "v":
        curr_y +=1

    visited_count[str(curr_x)+"_"+str(curr_y)] +=1
    return curr_x, curr_y


for i in range(0, len(line), 2):
    curr_x, curr_y = exec_present(line[i], curr_x, curr_y)
    curr_x_robot, curr_y_robot = exec_present(line[i+1], curr_x_robot, curr_y_robot)

count = 0
for key,val in visited_count.items():
    if val >0:
        count+=1
print(count)