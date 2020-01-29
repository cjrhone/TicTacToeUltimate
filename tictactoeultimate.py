board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

maxTurns = 9

# Compare board to 8 win conditions

# def turn():
#     #player1 = "X"
#     #player2 = "O"
#     pass

def gameBoard(XorO):
    userInput = input("Choose between 0-8\n")
    placePiece = int(userInput) #parsing userInput to integer
    board[placePiece] = XorO # locating userInput on board
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

for currentTurn in range(maxTurns):
    player = (currentTurn + 1) % 2
    if player == 0:
        piece = "O"
    else:
        piece = "X"

    gameBoard(piece) # We need something to pass X or O into gameboard
    print(currentTurn)

    #Something that switches between player 1 and player 2