import random

ROWS = 6
COLUMNS = 7

import connect_4 as c_4

def play_game():
    strats = {}
    for player in ['X','O']:
        print(f"Who will be playing as {player}?")
        print("1) Human")
        print("2) Random")
        print("Any other key to return to main menu")
        choice = input()
        if choice == '1':
            strats[player] = human_input
        elif choice == '2':
            strats[player] = computer_0
        else:
            return None
    print("Begining Game...")
    board = c_4.create_board()
    current_player = 'X'
    game_on = True
    attempts = 0
    while game_on and attempts < 10:
        column = strats[current_player](board,current_player)
        if type(column) != type(0):
            print(f"{current_player} did not give a column, trying again...")
            attempts += 1
        elif column < 0 or column >= COLUMNS:
            print(f"{current_player} attempted to play off board, trying again...")
            attempts += 1
        elif not c_4.valid_move(board, column):
            print(f"{current_player} attempted to play in a full column, trying again...")
            attempts += 1
        else:
            c_4.play_piece(board, column, current_player)
            if c_4.check_winner(board, current_player):
                c_4.print_board(board)
                print("Player", current_player, "wins! :D")
                game_on = False
            elif c_4.board_full(board):
                c_4.print_board(board)
                print("It's a tie! :O")
                game_on = False
            attempts = 0
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
    return None

def human_input(board, current_player):
    c_4.print_board(board)
    print(f"Player {current_player}, which column do you want to play in?")
    column = int(input("Choose a column (1-7):"))-1
    return column

def computer_0(board, current_player):
    return random.randint(0,6)

def main_menu():
    choice = None
    while choice != 2:
        print("What would you like to do?")
        print("1) New Game")
        print("2) Quit")
        choice = input()
        if choice == "1":
            play_game()
        elif choice == "2":
            print("Thanks for playing")
            exit()
        else:
            print("Invalid Choice.")
        

main_menu()