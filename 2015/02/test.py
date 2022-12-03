# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
lines = file.read().splitlines()

# close the file
file.close()
all = 0
for line in lines:

    l,w,h = line.split("x")
    l,w,h = int(l), int(w), int(h)
    one = 2 * l * w
    two = 2 * w * h
    three = 2 * h * l
    all+= one+two + three + min(one, two, three)/2

print(all)