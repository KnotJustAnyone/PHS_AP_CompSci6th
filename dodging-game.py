import random

class dodge_game:
    size = 0
    position = [0,0]
    grid = []
    dead = False
    score = 0

    def __init__(self, size):
        self.size = size
        self.make_grid()
        print("welcome! press w for up, s for down, a for left, and d for right.")
        while self.dead != True:
            mvm = input()
            if mvm == "w":
                self.move_player(0,-1)
            elif mvm == "s":
                self.move_player(0,1)
            elif mvm == "a":
                self.move_player(-1,0)
            elif mvm == "d":
                self.move_player(1,0)
            else:
                print("please enter a valid key")
            self.score += 1

    def make_grid(self):
        i = 0
        j = 0
        while i < self.size:
            self.grid.append([])
            while j < self.size:
                self.grid[i].append("O")
                j += 1
            i += 1
            j = 0
        self.grid[0][0] = "P"
        self.print_grid()
    
    def print_grid(self):
        print("score: " + str(self.score))
        for i in range(0,self.size):
            print(" ".join(self.grid[i]))
    
    def move_player(self, x, y):
        self.grid[self.position[1]][self.position[0]] = "O"
        self.position[0] += x
        if self.position[0] < 0 or self.position[0] >= self.size:
            print("you hit a wall!")
            self.position[0] -= x
        self.position[1] += y
        if self.position[1] < 0 or self.position[1] >= self.size:
            print("you hit a wall!")
            self.position[1] -= y
        self.grid[self.position[1]][self.position[0]] = "P"
        self.move_asteroids()
        self.make_asteroid(random.randint(0,self.size-1))
        self.print_grid()
    
    def make_asteroid(self,y):
        if self.grid[y][self.size-1] == "P":
            self.kill_player()
            self.grid[y][self.size-1] = "R"
        else:
            self.grid[y][self.size-1] = "X"
        
    
    def move_asteroids(self):
        for y in self.grid:
            for x in range(0,len(y)):
                if y[x] == "X":
                    y[x] = "O"
                    if y[x-1] == "O":
                        y[x-1] = "X"
                    if y[x-1] == "P":
                        self.kill_player()
                        y[x-1] = "R"

    def kill_player(self):
        print("You have died!")
        self.dead = True

dodge_game(8)