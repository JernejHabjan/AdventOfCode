# todo not finished yet
def aoc_2015_05_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    total = 0
    for line in lines:

        prev_prev_chr = None
        prev_chr = None
        two_pairs = []
        for chr in line:

            if prev_prev_chr is not None and prev_chr is not None:
                if prev_prev_chr == chr:
                    pass
                    # print("OK")

            # print(prev_prev_chr)

            # TODO weird instructions

            prev_prev_chr = prev_chr
            prev_chr = chr

        total += 1
    return total


if __name__ == '__main__':
    print(aoc_2015_05_b())
