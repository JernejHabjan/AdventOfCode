import aoc_2015.aoc_04.a as aoc_04_a


def aoc_2015_04_b():
    return aoc_04_a.get_hash_multithread(6, 1)  # todo increase thread count - but it's unsafe


if __name__ == '__main__':
    print(aoc_2015_04_b())
