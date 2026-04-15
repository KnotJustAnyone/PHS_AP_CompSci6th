import random
import json

ROWS = 6
COLUMNS = 7

import connect_4 as c_4

def human_input(board, current_player):
    c_4.print_board(board)
    print(f"Player {current_player}, which column do you want to play in?")
    column = int(input("Choose a column (1-7):"))-1
    return column

def computer_0(board, current_player):
    return random.randint(0,6)

try:
    with open('strategy1.json','r') as file:
        strategy_1 = json.load(file)
except:
    strategy_1 = [1 for _ in range(7)]
    json.dump(strategy_1,open('strategy1.json','w'), indent = 4)

def computer_1(board, current_player):
    return random.choices(range(7),weights = strategy_1,k=1)[0]

def choose_players():
    strats = {}
    for player in ['X','O']:
        print(f"Who will be playing as {player}?")
        print("1) Human")
        print("2) Random")
        print("3) Weighted Random")
        print("Any other key to return to main menu")
        choice = input()
        if choice == '1':
            strats[player] = human_input
        elif choice == '2':
            strats[player] = computer_0
        elif choice == '3':
            strats[player] = computer_1
        else:
            return None
    return strats

def play_game(strats):
    if strats == None:
        return None
    print("Begining Game...")
    board = c_4.create_board()
    current_player = 'X'
    game_on = True
    winner = None
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
                if human_input in strats.values():
                    c_4.print_board(board)
                print("Player", current_player, "wins!")
                winner = current_player
                game_on = False
            elif c_4.board_full(board):
                if human_input in strats.values():
                    c_4.print_board(board)
                print("It's a tie!")
                game_on = False
            attempts = 0
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
    if attempts == 10:
        print(f"{current_player} eliminated for excessive improper moves")
        if current_player == 'X':
            return 'O'
        else:
            return 'X'
    return winner

def training():
    print("Choose a training format")
    print("1) Gather Data, no change in behavior")
    choice = input()
    if choice == '1':
        gather_stats()
    return None

def gather_stats():
    strats = choose_players()
    print("How many games should they play?")
    try:
        rounds = int(input())
    except:
        print("Invalid round count")
        rounds = 0    
    outcomes = {'X':0,'O':0,None:0}
    for _ in range(rounds):
        outcomes[play_game(strats)] += 1
    print(outcomes)

def main_menu():
    choice = None
    while choice != 2:
        print("What would you like to do?")
        print("1) New Game")
        print("2) Train")
        print("3) Quit")
        choice = input()
        if choice == "1":
            players = choose_players()
            play_game(players)
        elif choice == "2":
            training()
        elif choice == "3":
            print("Thanks for playing")
            exit()
        else:
            print("Invalid Choice.")
        

main_menu()