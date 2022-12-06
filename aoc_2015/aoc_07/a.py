def _handle_overflow(var_name, dict1):
    # todo
    # binary = bin(dict1[var_name])[2:]
    # trimmed = binary[-16:]
    # print(binary,trimmed, int("0b" + trimmed, 2))
    # dict1[var_name] = int("0b" + trimmed, 2)
    if dict1[var_name] < 0:
        pass
        # print("This is probably not correct " + var_name + " " + str(dict1[var_name]))
    pass


# todo not finished yet
def aoc_2015_07_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    dict1 = dict()

    for line in lines:
        left_side, var_name = line.split(" -> ")

        # assignment
        if left_side.isnumeric():
            dict1[var_name] = int(left_side)

        if "AND" in left_side:
            from_var_name, to_var_name = left_side.split(" AND ")
            dict1[var_name] = dict1[from_var_name] & dict1[to_var_name]
            _handle_overflow(var_name, dict1)

        if "OR" in left_side:
            from_var_name, to_var_name = left_side.split(" OR ")
            dict1[var_name] = dict1[from_var_name] | dict1[to_var_name]
            _handle_overflow(var_name, dict1)

        if "LSHIFT" in left_side:
            from_var_name, amount = left_side.split(" LSHIFT ")
            dict1[var_name] = dict1[from_var_name] << int(amount)
            _handle_overflow(var_name, dict1)

        if "RSHIFT" in left_side:
            from_var_name, amount = left_side.split(" RSHIFT ")
            dict1[var_name] = dict1[from_var_name] >> int(amount)
            _handle_overflow(var_name, dict1)

        if "NOT" in left_side:
            from_var_name = left_side.split("NOT ")[1]
            dict1[var_name] = ~dict1[from_var_name]
            _handle_overflow(var_name, dict1)

    return dict1


if __name__ == '__main__':
    print(aoc_2015_07_a())
