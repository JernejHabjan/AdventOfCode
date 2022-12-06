def get_hash(nr):
    import hashlib

    key = "iwrupvqb"
    i = 1
    nr_zeroes = "0" * nr
    while True:
        h = hashlib.md5((key + str(i)).encode('utf-8')).hexdigest()
        if h[:nr] == nr_zeroes:
            res = i
            break
        i += 1
    return res


def aoc_2015_04_a():
    return get_hash(5)


if __name__ == '__main__':
    print(aoc_2015_04_a())
