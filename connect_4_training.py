import random

ROWS = 6
COLUMNS = 7

import connect_4 as c_4

def play_game():
    print("Who will be playing as X?")
    print("1) Human")
    print("Any other key to return to main menu")
    choice = input()
    if choice == '1':
        x_strat = human_input
    else:
        return None
    print("Who will be playing as y?")
    print("1) Human")
    print("Any other key to return to main menu")
    choice = input()
    if choice == '1':
        o_strat = human_input
    print("Begining Game...")
    board = c_4.create_board()
    current_player = 'X'
    game_on = True
    while game_on:
        game_on = False #Development paused here
    return None

def human_input(board):
    print("Human Strategy not Ready")
    return None

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