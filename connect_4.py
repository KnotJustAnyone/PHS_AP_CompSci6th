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

def play_piece(board, column, current_player):
    for row in range(ROWS-1,-1,-1):
        if board[row][column] == ".":
            board[row][column] = current_player
            return
    #plays the piece by dropping it the selected column
def valid_move(board,column):
    return board[0][column]=="."
    #checks if the selected column is full

def check_winner(board, current_player):
    #Horizontal 
    for r in range(ROWS):
        for c in range(COLUMNS-3):
            if board[r][c]==current_player and board[r][c+1]==current_player and board[r][c+2]==current_player and board[r][c+3]==current_player:
                return True
    #Vertical
    for r in range(ROWS-3):
        for c in range(COLUMNS):
            if board[r][c]==current_player and board[r+1][c]==current_player and board[r+2][c]==current_player and board[r+3][c]==current_player:
                return True
    #Diagonal down-right
    for r in range(ROWS-3):
        for c in range(COLUMNS-3):
            if board[r][c]==current_player and board[r+1][c+1]==current_player and board[r+2][c+2]==current_player and board[r+3][c+3]==current_player:
                return True
    #Diagonal up-right
    for r in range(3,ROWS):
        for c in range(COLUMNS-3):
            if board[r][c]==current_player and board[r-1][c+1]==current_player and board[r-2][c+2]==current_player and board[r-3][c+3]==current_player:
                return True
            
    return False


#Player X is player 1, Player O is player 2
current_player = "X"

while True:
    print_board(board)
    print("Player", current_player, "turn")

    column = int(input("Choose a column (1-7):"))-1
    #asks user to choose a column to drop the play piece
    if column <0 or column >= COLUMNS:
        print("Invalid column. Try again. :]")
        continue
    if not valid_move(board, column):
        print("That column is full. Try again :/")
        continue

    play_piece(board, column, current_player)

    #Check for winner
    if check_winner(board, current_player):
        print_board(board)
        print("Player", current_player, "wins! :D")
        break

    #switch players
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
