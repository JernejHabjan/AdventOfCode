with open('input.txt', "r") as f: lines = f.read().splitlines()

initialDepth = None
depthSums = [None, None]
counter = 0
for i in range(2, len(lines)):
    a = int(lines[i - 2])
    b = int(lines[i - 1])
    c = int(lines[i])
    depthSums.append(a + b + c)
for depthSum in depthSums:
    if initialDepth is not None and depthSum is not None and depthSum > initialDepth:
        counter += 1
    initialDepth = depthSum

print(counter)
