import random

class dodge_game:
    size = 0
    position = [0,0]
    grid = []
    dead = False
    score = 0
    spawn_rate = 0

    def __init__(self):
        print("how large would you like the playing field to be?")
        while self.size == 0:
            try:
                size_choice = int(input())
            except:
                print("please enter a valid number")
            else:
                if size_choice > 0:
                    self.size = size_choice
                else:
                    print("please enter a positive integer")
        print("What would you like the spawn rate to be?")
        while self.spawn_rate == 0:
            try:
                rate_choice = int(input())
            except:
                print("please enter a valid number")
            else:
                if rate_choice > 0 and rate_choice <= self.size:
                    self.spawn_rate = rate_choice
                else:
                    print("please enter a positive integer smaller than the size you chose.")
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
        self.move_asteroids()
        self.make_asteroids()
        if self.dead == False:
            self.grid[self.position[1]][self.position[0]] = "O"
            self.position[0] += x
            if self.position[0] < 0 or self.position[0] >= self.size:
                print("you hit a wall!")
                self.position[0] -= x
            self.position[1] += y
            if self.position[1] < 0 or self.position[1] >= self.size:
                print("you hit a wall!")
                self.position[1] -= y
            if self.grid[self.position[1]][self.position[0]] == "O":
                self.grid[self.position[1]][self.position[0]] = "P"
            elif self.grid[self.position[1]][self.position[0]] == "X":
                self.grid[self.position[1]][self.position[0]] = "R"
                self.kill_player()
            self.print_grid()
        
    
    def make_asteroids(self):
        positions = []
        while len(positions) < self.spawn_rate:
            rand_choice = random.randint(0,self.size-1)
            already_chosen = False
            for i in positions:
                if i == rand_choice:
                    already_chosen = True
            if already_chosen == False:
                positions.append(rand_choice)

        for y in positions:
            if self.grid[y][self.size-1] == "P":
                self.grid[y][self.size-1] = "R"
                self.kill_player()
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
                        y[x-1] = "R"
                        self.kill_player()

    def kill_player(self):
        print("You have died!")
        self.dead = True
        self.print_grid()

dodge_game()