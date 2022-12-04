file = open('input.txt', mode='r')
line = file.read().splitlines()[0]
file.close()

print(line.count('(') - line.count(')'))
