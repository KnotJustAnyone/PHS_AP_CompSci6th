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

print_board(board)
column = int(input("Choose a column (1-7):"))-1
#asks user to choose a column to drop the play piece

def play_piece(board, column, symbol):
    for row in range(ROWS-1,-1,-1):
        if board[row][column] == ".":
            board[row][column] = symbol
            return
    #plays the piece by dropping it the selected column
        
play_piece(board, column, "X")
print_board(board)

