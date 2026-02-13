#make data structure and display board
#ask user what move they want to play & add symbol

ROWS = 6
COLUMNS = 7
#traditional game is 6 x 7

board =[]

for r in range(ROWS):
    row=[]
    for c in range(COLUMNS):
        row.append(".")
    board.append(row)

def print_board(board):
    for row in board:
        print("|", " ".join(row),"|")
    print("  1 2 3 4 5 6 7")
    #sets up display board, column numbers are listed underneath

def play_piece(board, column, symbol):
    for row in range(ROWS-1,-1,-1):
        if board[row][column] == ".":
            board[row][column] = symbol
            return
    #plays the piece by dropping it the selected column

#Player X is player 1, Player O is player 2
current_player = "X"
while True:
    print_board(board)
    print("Player", current_player, "turn")
    #asks user to choose a column to drop the play piece
    column = int(input("Choose a column (1-7):"))-1
    play_piece(board, column, current_player)

    #switch players
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print_board(board)
