import threading

thread_res = None


def get_hash(nr, start_i, nr_threads):
    import hashlib
    global thread_res

    key = "iwrupvqb"
    i = start_i
    nr_zeroes = "0" * nr
    while True:
        if thread_res is not None:
            return thread_res
        h = hashlib.md5((key + str(i)).encode('utf-8')).hexdigest()
        if h[:nr] == nr_zeroes:
            res = i
            break
        i += nr_threads
    if thread_res is None or i < thread_res:
        thread_res = i
    return res


# note that this multi-threading may find thread_res larger than min possible,
# because some other thread might execute and find bigger res prior the one, that should find the result
def get_hash_multithread(nr, nr_threads):
    threads = []
    for i in range(nr_threads):
        t = threading.Thread(target=get_hash, args=(nr, i, nr_threads))
        t.start()
        threads.append(t)
    for i in range(nr_threads):
        threads[i].join()

    return thread_res


def aoc_2015_04_a():
    return get_hash_multithread(5, 1)


if __name__ == '__main__':
    print(aoc_2015_04_a())
