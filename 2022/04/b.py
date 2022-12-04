with open('input.txt', "r") as f: lines = f.read().splitlines()

total = 0
for line in lines:
    (first1, second1) = line.split(",")
    (a1, b1), (c1, d1) = first1.split("-"), second1.split("-")
    min1, max1, min2, max2 = int(a1), int(b1), int(c1), int(d1)
    # print(min1, max1, min2, max2)

    overlapFront = min1 <= min2 <= max1
    overlapBack = min2 <= min1 <= max2
    overlapA = min1 <= min2 and max1 >= max2
    overlapB = min2 <= min1 and max2 >= max1
    if overlapFront or overlapBack or overlapA or overlapB:
        total += 1
print(total)
