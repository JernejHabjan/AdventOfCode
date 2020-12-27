# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
line = file.read().splitlines()[0]

# close the file
file.close()



print(line.count('(') - line.count(')'))