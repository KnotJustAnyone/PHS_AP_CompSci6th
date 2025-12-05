import numpy
import random

sudoku_boards={"easy":{"start":[
                                [0,0,0,2,6,0,7,0,1],
                                [6,8,0,0,7,0,0,9,0],
                                [1,9,0,0,0,4,5,0,0],
                                [8,2,0,1,0,0,0,4,0],
                                [0,0,4,6,0,2,9,0,0],
                                [0,5,0,0,0,3,0,2,8],
                                [0,0,9,3,0,0,0,7,4],
                                [0,4,0,0,5,0,0,3,6],
                                [7,0,3,0,1,8,0,0,0]],
                       "answer":[
                                [4,3,5,2,6,9,7,8,1],
                                [6,8,2,5,7,1,4,9,3],
                                [1,9,7,8,3,4,5,6,2],
                                [8,2,6,1,9,5,3,4,5],
                                [3,7,4,6,8,2,9,1,5],
                                [9,5,1,7,4,3,6,2,8],
                                [5,1,9,3,2,6,8,7,4],
                                [2,4,8,9,5,7,1,3,6],
                                [7,6,3,4,1,8,2,5,9]
                       ]},"medium":[],"hard":[]}

class sudoku_board:
    def __init__(self):
        difficulty = None
        while not difficulty:
            print("What difficulty do you want to play at? (easy, medium, or hard)")
            difficulty=input()
            if difficulty not in sudoku_boards.keys() or len(sudoku_boards[difficulty]) == 0:
                print("No boards available of that difficulty, try another")
                difficulty = None
        board=sudoku_boards[difficulty][random.randrange(len(sudoku_boards[difficulty]))]
        self.answer = board['answer']
        self.start = board['start']
        self.current = [[n for n in row] for row in board['start']]
        self.gameover=False
    def guess(self):
        print("What is your guess?")
        z=int(input())
        print("Where do you want to put it? (x-coordinate, 1-9)")
        x=int(input())-1
        print("Where do you want to put it? (y-coordinate, 1-9)")
        y=9-int(input())
        self.board[y][x]=z
    def check(self,x,y):
        pass
    def congrats(self):
        j=1
        i=1
        x=0
        while j <10:
            while i<10:
                if self.check(i,j)==True:
                    x=x+1
                    i=i+1
                else:
                    i=i+1
            i=0
            j=j+1
        if x==81:
            print("Congratulations! You won!")
            self.gameover=True
        else:
            print("Do you want to check any spaces? (y/N)")
            check=input()
            if check=="y" or check=="Y":
                self.check()
    def gameplay(self):
        while self.gameover==False:
            self.guess()
            self.congrats()
def testcheck():
    board1=sudoku_board()
    board1.one_sudoku_board = [[7,5,0,0,5,0,0,3,1],[0,9,1,0,0,4,2,7,6],[0,0,3,7,0,2,4,0,0],[2,0,0,0,0,0,0,4,7],[0,7,9,4,6,0,1,0,3],[4,0,0,3,0,0,6,8,9],[0,6,0,0,4,3,7,"Frank",2],[0,0,4,2,0,0,0,0,0],[0,0,0,0,0,9,3,0,4]]
    board1.done_sudoku_board = [[7,4,2,9,5,6,8,3,1],[5,9,1,8,3,4,2,7,6],[6,8,3,7,1,2,4,9,5],[2,3,6,1,9,8,5,4,7],[8,7,9,4,6,5,1,2,3],[4,1,5,3,2,7,6,8,9],[9,6,8,5,4,3,7,1,2],[3,5,4,2,7,1,9,6,8],[1,2,7,6,8,9,3,5,4]]
    test=[[2,9,False],[3,7,True],[1,1,False],[8,3,False]]
    errortest=[["Frank","Sally","Error: list index out of range"],[0,0,"Error: list index out of range"]]

def testforguess():
    print("This is the test for the guess function. To test the code out, you will have to input values.")
    print("In this segment, I will tell you what to input")
    print("This is the format for the values, (x,y,z)")
    print("Input #1: (2,4,5)")
    print("Input #2: (four, 2, 3)")
    print("Input #3: (4,5,three)")
    print("Input #4: (4,alice,4)")
    print("Input #5: (three, bob, pizza")
    print("If the code works correctly, only the first input should work.")
