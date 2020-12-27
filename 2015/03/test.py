import math
import collections

# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
line = file.read().splitlines()[0]

# close the file
file.close()

curr_x = 0
curr_y = 0

visited_count = collections.defaultdict(int)
visited_count[str(curr_x)+"_"+str(curr_y)] += 1
for chr in line:

    if chr == ">":
        curr_x +=1
    if chr == "<":
        curr_x -= 1
    if chr == "^":
        curr_y -=1
    if chr == "v":
        curr_y +=1

    visited_count[str(curr_x)+"_"+str(curr_y)] +=1

count = 0
for key,val in visited_count.items():
    if val >0:
        count+=1
print(count)