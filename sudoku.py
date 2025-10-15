import numpy
import random
class sudoku_board:
    def __init__(self):
        sudoku_boards={"easy":[],"medium":[],"hard":[]}
        self.board=numpy.full(81,0).reshape(9,9)
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
        #if everything is right, good job, pat on the back
        pass
