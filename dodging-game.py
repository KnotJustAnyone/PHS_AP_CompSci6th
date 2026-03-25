import random

class dodge_game:
    size = 0
    position = [0,0]
    grid = []
    dead = False
    score = 0
    spawn_rate = 0

    def __init__(self):
        self.double_move = False
        self.hammer = False
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
        print("welcome! press w for up, s for down, a for left, d for right, and space to stay still.")
        print("P is the player, O is open space, and X is an asteroid.")
        print("touching an arrow (>) allows you to move an extra space on the next move.")
        print("a hammer (H) allows you to destroy the next asteroid you touch.")
        print("a bomb (B) destroys all asteroids currently on the board.")
        while self.dead != True:
            mvm = input()
            mvm_num = 1
            if self.double_move == True:
                mvm_num = 2
            print(mvm_num)
            if mvm == "w":
                self.move_player(0,-mvm_num)
            elif mvm == "s":
                self.move_player(0,mvm_num)
            elif mvm == "a":
                self.move_player(-mvm_num,0)
            elif mvm == "d":
                self.move_player(mvm_num,0)
            elif mvm == " ":
                self.move_asteroids()
                self.make_asteroids()
                self.print_grid()
            else:
                print("please enter a valid key")
            self.score += 1
            self.double_move = False

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
            rand_choice_two = random.randint(1,15)
            already_chosen = False
            for i in positions:
                if i == rand_choice:
                    already_chosen = True
            if already_chosen == False:
                positions.append([rand_choice, rand_choice_two])

        for y in positions:
            if self.grid[y[0]][self.size-1] == "P":
                if y[1] >= 1 and y[1] <= 12:
                    if self.hammer == False:
                        self.grid[y[0]][self.size-1] = "R"
                        self.kill_player()
                    else:
                        self.grid[y[0]][self.size-1] = "P"
                        self.hammer = False
                if y[1] == 13:
                    self.grid[y[0]][self.size-1] = "P"
                    self.double_move = True
                    print("you gained a double move powerup!")
                if y[1] == 14:
                    self.grid[y[0]][self.size-1] = "P"
                    self.Hammer = True
                    print("you picked up a hammer.")
                if y[1] == 15:
                    self.grid[y[0]][self.size-1] = "P"
                    for u in self.grid:
                        for v in range(0,len(u)):
                            if u[v] == "X":
                                u[v] = "O"
                    print("kaboom")
            else:
                if y[1] >= 1 and y[1] <= 12:
                    self.grid[y[0]][self.size-1] = "X"
                elif y[1] == 13:
                    self.grid[y[0]][self.size-1] = ">"
                elif y[1] == 14:
                    self.grid[y[0]][self.size-1] = "H"
                elif y[1] == 15:
                    self.grid[y[0]][self.size-1] = "B"
        
    
    def move_asteroids(self):
        for y in self.grid:
            for x in range(0,len(y)):
                if y[x] == "X" or y[x] == ">" or y[x] == "H" or y[x] == "B":
                    obj_type = y[x]
                    y[x] = "O"
                    if y[x-1] == "O":
                        y[x-1] = obj_type
                    if y[x-1] == "P":
                        if obj_type == "X":
                            if self.hammer == False:
                                print("it was false")
                                y[x-1] = "R"
                                self.kill_player()
                            else:
                                print("it was true")
                                y[x-1] = "P"
                                self.hammer = False
                        elif obj_type == ">":
                            y[x-1] = "P"
                            self.double_move = True
                            print("you gained a double move powerup!")
                        elif obj_type == "H":
                            y[x-1] = "P"
                            self.Hammer = True
                            print("you picked up a hammer.")
                        elif obj_type == "B":
                            y[x-1] = "P"
                            for u in self.grid:
                                for v in range(0,len(u)):
                                    if u[v] == "X":
                                        u[v] = "O"
                            print("kaboom")


                        

    def kill_player(self):
        print("You have died!")
        self.dead = True
        self.print_grid()

dodge_game()