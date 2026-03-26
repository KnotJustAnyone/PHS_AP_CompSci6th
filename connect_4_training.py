import random

ROWS = 6
COLUMNS = 7

import connect_4 as c_4

def main_menu():
    choice = None
    while choice != 2:
        print("What would you like to do?")
        print("1) New Game")
        print("2) Quit")
        choice = input()
        if choice == "1":
            print("Still In Development, exiting")
        elif choice == "2":
            print("Thanks for playing")
            exit()
        else:
            print("Invalid Choice.")
        

main_menu()