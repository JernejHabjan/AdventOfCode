# Open a file: file
file = open('input.txt', mode='r')

# read all lines at once
lines = file.read().splitlines()

# close the file
file.close()

nrInput = lines[0].split(",")
boards = []
for i in range(1, len(lines)):
    line = lines[i]
    if line == "":
        boards.append([])
        continue
    line = line.lstrip().replace("  ", " ")
    boards[len(boards) - 1].append(line.split(" "))


def allNonesInVec(arr):
    for r in arr:
        if r is not None:
            return False
    return True


def validate(board):
    for currColumnIndex in range(0, len(board)):
        colVec = []
        for currentRowIndex in range(0, len(board[currColumnIndex])):
            colVec.append(board[currentRowIndex][currColumnIndex])
            if allNonesInVec(board[currColumnIndex]):
                return True
        if allNonesInVec(colVec):
            return True

    return False


def getSumUnmarked(board):
    sumUnmarked = 0

    for line in board:
        for nr in line:
            if nr is not None:
                sumUnmarked += int(nr)
    return sumUnmarked


def validateAll(nr, totalWinners):
    winner = 0
    winningBoard = None
    for board in boards:
        if validate(board):
            winner = int(nr)
            winningBoard = board
            totalWinners += 1
            # print("winner", board, "nr", nr)
            break
    return winner, winningBoard, totalWinners


def bb():
    totalWinners = 0
    winner = 0
    winningBoard1 = None
    winningBoard = None
    nr1 = None
    for nr in nrInput:
        # print("nr unmarked1", nr)
        if totalWinners == len(boards):
            break
        for i in range(0, len(boards)):
            # print(getSumUnmarked(boards[i]))
            for j in range(0, len(boards[i])):
                for k in range(0, len(boards[i][j])):
                    if boards[i][j][k] == nr:
                        boards[i][j][k] = None
                        # print("nr unmarked2", nr)

                        # winner1, winningBoard1, totalWinners1 = validateAll(nr, totalWinners)
                        # if (totalWinners1 == len(boards)):
                        #     print("OK", nr)

        winner, winningBoard, totalWinners = validateAll(nr, totalWinners)
        # print("total winners", totalWinners, winningBoard)

        if (winningBoard in boards):
            winningBoard1 = winningBoard.copy()
            # print("OK IN", boards.index(winningBoard))
            del boards[boards.index(winningBoard)]
            nr1 = nr

    return nr1, winningBoard1


winner, winningBoard = bb()

sumUnmarked = getSumUnmarked(winningBoard)
print(int(sumUnmarked) * int(winner))
