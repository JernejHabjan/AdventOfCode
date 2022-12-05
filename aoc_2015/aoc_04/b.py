def aoc_2015_04_b():
    import hashlib

    key = "iwrupvqb"
    i = 1
    while True:
        h = hashlib.md5((key + str(i)).encode('utf-8')).hexdigest()
        if h[:6] == "000000":
            res = i
            break
        i += 1
    return res


if __name__ == '__main__':
    print(aoc_2015_04_b())
