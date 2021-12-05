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


winner = 0
winningBoard = None
for nr in nrInput:
    # print("next nr", nr)
    if winner != 0:
        break
    for i in range(0, len(boards)):
        for j in range(0, len(boards[i])):
            for k in range(0, len(boards[i][j])):
                if boards[i][j][k] == nr:
                    boards[i][j][k] = None
    for board in boards:
        if validate(board):
            winner = int(nr)
            winningBoard = board
            print("winner", board, "nr", nr)
            break

sumUnmarked = 0

for line in winningBoard:
    for nr in line:
        if nr is not None:
            sumUnmarked += int(nr)
print(sumUnmarked * winner)
