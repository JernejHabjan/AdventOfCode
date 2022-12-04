file = open('input.txt', mode='r')
lines = file.read().splitlines()
file.close()

dict1 = dict()


def handle_overflow(var_name):
    # todo
    # binary = bin(dict1[var_name])[2:]
    # trimmed = binary[-16:]
    # print(binary,trimmed, int("0b" + trimmed, 2))
    # dict1[var_name] = int("0b" + trimmed, 2)
    if dict1[var_name] < 0:
        print("This is probably not correct " + var_name + " " + str(dict1[var_name]))
    pass


for line in lines:
    left_side, var_name = line.split(" -> ")

    # assignment
    if left_side.isnumeric():
        dict1[var_name] = int(left_side)

    if "AND" in left_side:
        from_var_name, to_var_name = left_side.split(" AND ")
        dict1[var_name] = dict1[from_var_name] & dict1[to_var_name]
        handle_overflow(var_name)

    if "OR" in left_side:
        from_var_name, to_var_name = left_side.split(" OR ")
        dict1[var_name] = dict1[from_var_name] | dict1[to_var_name]
        handle_overflow(var_name)

    if "LSHIFT" in left_side:
        from_var_name, amount = left_side.split(" LSHIFT ")
        dict1[var_name] = dict1[from_var_name] << int(amount)
        handle_overflow(var_name)

    if "RSHIFT" in left_side:
        from_var_name, amount = left_side.split(" RSHIFT ")
        dict1[var_name] = dict1[from_var_name] >> int(amount)
        handle_overflow(var_name)

    if "NOT" in left_side:
        from_var_name = left_side.split("NOT ")[1]
        dict1[var_name] = ~dict1[from_var_name]
        handle_overflow(var_name)

print(dict1)
