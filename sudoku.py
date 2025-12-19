import numpy
import random
import sudokuboards as sb
class sudoku_board:
    def __init__(self):
        print("What difficulty do you want to play at? (easy, medium, or hard)")
        sudoku_boards={"easy":sb.easy,"medium":sb.medium,"hard":sb.hard}
        difficulty=input()
        self.chosenboard=sudokuboards[difficulty][random.randrange(len(sudokuboards[difficulty]))]
        self.gameover=False
    def sudokuprint(self):
        for n in range(9):
            string=""
            for m in range(9):
                string+=str(self.chosenboard[0][n][m])+" "
                if m==2 or m==5:
                    string+="| "
            print(string)
            if n==2 or n==5:
                print("— — — — — — — — — — —")
    def guess(self):
        self.sudokuprint()
        print("What is your guess?")
        z=int(input())
        print("Where do you want to put it? (x-coordinate, 1-9)")
        x=int(input())-1
        print("Where do you want to put it? (y-coordinate, 1-9)")
        y=int(input())-1
        self.chosenboard[0][y][x]=z
    def check(self,x,y):
        if self.chosenboard[0][l][k]==self.chosenboard[1][l][k]:
            return True
        else:
            return False
    def congrats(self):
        j=0
        i=0
        x=0
        while j <9:
            while i<9:
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
                if self.chosenboard[0][k][l]==self.chosenboard[1][k][l]:
                    print("This space is correct.")
                else:
                    print("Not quite right.")
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

game = sudoku_board()
game.gameplay()

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

testforguess()
