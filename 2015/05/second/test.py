# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
lines = file.read().splitlines()

# close the file
file.close()
all = 0
for line in lines:

    prev_prev_chr = None
    prev_chr = None
    two_pairs = []
    for chr in line:

        if prev_prev_chr is not None and prev_chr is not None:
            if prev_prev_chr == chr:
                print("OK")

        print(prev_prev_chr)

        # TODO weird instructions

        prev_prev_chr = prev_chr
        prev_chr = chr

    all += 1
print(all)
