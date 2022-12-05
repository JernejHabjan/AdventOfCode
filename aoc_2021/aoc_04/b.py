def _all_nones_in_vec(arr):
    for r in arr:
        if r is not None:
            return False
    return True


def _validate(board):
    for currColumnIndex in range(0, len(board)):
        col_vec = []
        for currentRowIndex in range(0, len(board[currColumnIndex])):
            col_vec.append(board[currentRowIndex][currColumnIndex])
            if _all_nones_in_vec(board[currColumnIndex]):
                return True
        if _all_nones_in_vec(col_vec):
            return True

    return False


def _get_winner(boards, nr_input):
    winner = 0
    winning_board = None
    for nr in nr_input:
        # print("next nr", nr)
        if winner != 0:
            break
        for i in range(0, len(boards)):
            for j in range(0, len(boards[i])):
                for k in range(0, len(boards[i][j])):
                    if boards[i][j][k] == nr:
                        boards[i][j][k] = None
        for board in boards:
            if _validate(board):
                winner = int(nr)
                winning_board = board
                # print("winner", board, "nr", nr)
                break
    return winning_board, winner


def aoc_2021_04_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    nr_input = lines[0].split(",")
    boards = []
    for i in range(1, len(lines)):
        line = lines[i]
        if line == "":
            boards.append([])
            continue
        line = line.lstrip().replace("  ", " ")
        boards[len(boards) - 1].append(line.split(" "))

    last_winning = None
    last_nr = None
    while len(boards):
        winning, nr = _get_winner(boards, nr_input)
        last_winning = winning.copy()
        last_nr = nr
        del boards[boards.index(winning)]
        # print(nr)

    sumUnmarked = 0

    for line in last_winning:
        for nr in line:
            if nr is not None:
                sumUnmarked += int(nr)
    return sumUnmarked * last_nr


if __name__ == '__main__':
    print(aoc_2021_04_b())
