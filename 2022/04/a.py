with open('input.txt', "r") as f: lines = f.read().splitlines()

total = 0
for line in lines:
    (first1, second1) = line.split(",")
    (a1, b1), (c1, d1) = first1.split("-"), second1.split("-")
    a, b, c, d = int(a1), int(b1), int(c1), int(d1)
    # print(a, b, c, d)
    if a <= c and b >= d or c <= a and d >= b:
        total += 1
print(total)
