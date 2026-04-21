import random

class dodge_game:
    size = 0
    position = [0,0]
    grid = []
    dead = False
    score = 0
    spawn_rate = 0
    mvm_amt = 1
    has_hammer = False

    def __init__(self):
        # Student developed list: stores data for each object that can appear
        # allows the make_objects function to choose randomly from this list
        # easy access to what happens when an object is touched
        # makes it easier to add other objects in any future development
        # makes the code cleaner
        self.objects = [
            ["X", self.kill_player, 12],
            [">", self.boost_movement, 13],
            ["H", self.hammer, 14],
            ["B", self.bomb, 15]
            # [object visual, function when touched, probability of appearing]
        ]

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
            print(self.mvm_amt)
            if mvm == "w":
                self.move_player(0,-self.mvm_amt)
            elif mvm == "s":
                self.move_player(0,self.mvm_amt)
            elif mvm == "a":
                self.move_player(-self.mvm_amt,0)
            elif mvm == "d":
                self.move_player(self.mvm_amt,0)
            elif mvm == " ":
                self.move_player(0,0)
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
        self.mvm_amt = 1
        self.grid = self.move_objects(self.grid)
        self.grid = self.make_objects(self.spawn_rate, self.grid) # calls the make_objects function to add objects to the grid before moving the player

        if (x != 0 or y != 0) and self.grid[self.position[1]][self.position[0]] == "P":
            self.grid[self.position[1]][self.position[0]] = "O"

        if self.position[0] + x >= 0 and self.position[0] + x <= self.size:
            self.position[0] += x
        
        if self.position[1] + y >= 0 and self.position[1] + y <= self.size:
            self.position[1] += y

        x_pos = self.position[0]
        y_pos = self.position[1]

        if self.grid[y_pos][x_pos] == "O":
            self.grid[y_pos][x_pos] = "P"
        else:
            for o in self.objects:
                if self.grid[y_pos][x_pos] == o[0]:
                    self.grid[y_pos][x_pos] = o[1]()
        
        self.print_grid()
        
    # Owen Carroll student developed procedure
    # Takes a number and spawns that number of randomly chosen object from the list of objects in a random position
    # Returns the grid with the number of objects added to the right end
    # Returns an error message if the right side of the list has any objects in it already
    def make_objects(self, num_objects, grid):
        new_grid = grid
        positions = []

        total_cases = 0
        for x in self.objects:
            total_cases = x[2]

        while len(positions) < num_objects:
            rand_choice = random.randint(0,self.size-1)
            rand_choice_two = random.randint(1,total_cases)
            already_chosen = False

            for i in positions:
                if i == rand_choice:
                    already_chosen = True
            if already_chosen == False:
                positions.append([rand_choice, rand_choice_two])

        for y in positions:
            chosen_object = -1
            for i in range(0,len(self.objects)):
                if y[1] <= self.objects[i][2] and chosen_object < 0:
                    chosen_object = i
            new_grid[y[0]][self.size-1] = self.objects[chosen_object][0]
        
        return new_grid
        
    def move_objects(self, grid):
        newGrid = grid
        for y in newGrid:
            for x in range(0,len(y)):
                if y[x] != "O" and y[x] != "P":
                    if x == 0:
                        y[x] = "O"
                    else:
                        y[x-1] = y[x]
                        y[x] = "O"
        return newGrid

    def kill_player(self):
        if self.has_hammer == False:
            print("You have died!")
            self.dead = True
            return "X"
        else:
            self.has_hammer = False
            return "P"

    def boost_movement(self):
        self.mvm_amt = 2
        print(self.mvm_amt)
        return "P"
    
    def hammer(self):
        self.has_hammer = True
        return "P"
    
    def bomb(self):
        for y in self.grid:
            for x in range(0,len(y)):
                if y[x] != "O" and y[x] != "P":
                    y[x] = "O"
        return "P"

dodge_game()