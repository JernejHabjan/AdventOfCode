import re


def aoc_2015_05_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    total = 0
    for line in lines:

        prev_prev_chr = None
        prev_chr = None
        has_char_between = False
        contains_multiple_pairs = False
        for character in line:

            if prev_chr is not None:
                # checking for contains_multiple_pairs
                substring = prev_chr + character
                if len(re.findall(substring, line)) > 1:
                    contains_multiple_pairs = True
                    # print("contains_multiple_pairs")

                # checking for has_char_between
                if prev_prev_chr is not None:
                    if prev_prev_chr == character:
                        has_char_between = True
                        # print("has_char_between")
            prev_prev_chr = prev_chr
            prev_chr = character
        if has_char_between and contains_multiple_pairs:
            total += 1
    return total


if __name__ == '__main__':
    print(aoc_2015_05_b())
