def aoc_2021_01_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    initial_depth = None
    depth_sums = [None, None]
    counter = 0
    for i in range(2, len(lines)):
        a = int(lines[i - 2])
        b = int(lines[i - 1])
        c = int(lines[i])
        depth_sums.append(a + b + c)
    for depthSum in depth_sums:
        if initial_depth is not None and depthSum is not None and depthSum > initial_depth:
            counter += 1
        initial_depth = depthSum

    return counter


if __name__ == '__main__':
    print(aoc_2021_01_b())
