def aoc_2015_02_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()
    total = 0
    for line in lines:
        l, w, h = line.split("x")
        l, w, h = int(l), int(w), int(h)
        # one = l * w
        # two = w * h
        # three = h * l

        # print(l,w,h)
        # print(one, two ,three)

        a, b, c = 2 * (h + l), 2 * (l + w), 2 * (h + w)

        obseg = min(a, b, c)
        bow = w * h * l
        # print(obseg)
        total += obseg + bow

        # total += one+two + three + min(one, two, three)/2

    return total


if __name__ == '__main__':
    print(aoc_2015_02_b())
