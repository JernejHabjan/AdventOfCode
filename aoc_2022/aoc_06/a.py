def get_marker(nr):
    from queue import Queue
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        line = f.read().splitlines()[0]

    current_stream = Queue(maxsize=nr)
    res = "NOT_FOUND"
    for i, character in enumerate(line):
        current_stream.put(character)
        if current_stream.qsize() < nr:
            continue

        test_set = set(current_stream.queue)
        if len(test_set) == nr:
            res = i + 1
            break
        else:
            # remove ele from queue
            current_stream.get()
    return res


def aoc_2022_06_a():
    return get_marker(4)


if __name__ == '__main__':
    print(aoc_2022_06_a())
