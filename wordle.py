import random

class wordle_board:
    
    word_board = [] # words are added to this array as they are guessed
    num_board = [] # arrays of numbers are added to this array as words are guessed, indicating the correctness of each letter
    
    def __init__(self):
        self.word_list = { # list of 5 letter english words
            "river",
            "child",
            "basic",
            "lease",
            "salon",
            "snarl",
            "great",
            "skate",
            "obese",
            "treat",
            "motif",
            "write",
            "block",
            "graze",
            "troop",
            "awful",
            "bread",
            "youth",
            "clerk",
            "hover",
            "lover",
            "glide",
            "sharp",
            "crowd",
            "toast"
        }
        self.winning_word = self.word_list[random.randint(0,len(self.word_list)-1)] # choose a word at random from array above
    
    def guess_word(self, word): # returns whether a word is eligible, and then checks the letters of the word, adding to the word and number boards.
        if len(word) != 5: # checks if the word doesn't have 5 letters
            return False
        else: # otherwise, continue
            self.word_board.append(word) # adds the word to the end of the word board
            x_position = 0 # uses a number variable to look at the position of each letter
            numbers_array = [] # creates an array, adds 1 for letters that match, 2 for letters with the same position, and 0 for letters that fulfill neither
            letters_array = [] # creates an array to keep track of which letters have been considered so repeats do not happen
            for x in word: # loops through the letters of the word
                number_given = 0 # accounts for what has been added
                y_position = 0 # uses a number variable to look at the position of each letter
                used_letter = 5
                for y in self.winning_word: # loops through the letters of the winning word
                    letter_used = False
                    for letter in letters_array:
                        if y_position == letter:
                            letter_used = True
                    if x == y and number_given < 2 and letter_used == False: # determines if each letter is in the guessed word and makes sure it isn't already given a 2
                        if x_position == y_position: # checks if they have the same position
                            numbers_array.append(2) # add a 2 for the letter
                            number_given = 2 # account for the change
                            used_letter = y_position
                        elif number_given < 1: # otherwise, if there isnt a number given yet
                            numbers_array.append(1) # add a 1 for the letter
                            number_given = 1 # account for the change
                            used_letter = y_position
                    y_position += 1 # set position equal to correct position
                if number_given == 0: # if there has been no number added
                    numbers_array.append(0) # add a 0
                letters_array.append(used_letter)
                x_position += 1 # set position equal to correct position
            self.num_board.append(numbers_array) # add the numbers to the array
            for x in range(0,len(self.word_board)): # loops through the word board and number board to print each value
                print(self.word_board[x]) # prints the xth value of the word board
                print(self.num_board[x]) # prints the xth value of the number board
            return True
    
    def game_over():
        # loops through the number board
        # uses a variable to determine the length
        # checks if anything in the number board is [1,1,1,1,1]
        # if so, return True and print out that the player won
        # if not, continue
        # checks if the variable is greater than or equal to 6
        # if so, return True and print out that the player has lost
        return

    def _test_game_over():
                # Set a known winning word to control the test
        game.winning_word = "apple"
        
        #  Test 1: Win after correct 
        print("Test 1: Player guesses the correct word")
        game.guess_word("apple")  # Correct guess
        print("game_over():", game.game_over())  # Should print True and "You won!"
        print("Expected: True\n")
        
        #Test 2: Lose after 6 wrong guesses
        print("Test 2: Player makes 6 incorrect guesses")
        game = wordle_board()
        game.winning_word = "apple"
        
        # Make 6 incorrect guesses
        for i in range(6):
            game.guess_word("stone")  # Wrong word
        
        print("game_over():", game.game_over())  # Should print True and "You lost!"
        print("Expected: True\n")
        
        # --- Test 3: Game still in progress ---
        print("Test 3: Game still in progress after 3 incorrect guesses")
        game = wordle_board()
        game.winning_word = "apple"
        
        # Make 3 incorrect guesses
        for i in range(3):
            game.guess_word("grape")
        
        print("game_over():", game.game_over())  # Should print False
        print("Expected: False\n")

    def test_guess_word(self): #returns false if the code returns the wrong thing, true if it returns the right thing
        board = self
        if board.guess_word(board,"owen") == True or board.guess_word(board,"obingus") == True: # if the function returns true for an ineligible word
            return False
        else:
            board.winning_word = "abbcd" # sets the winning word to abbcd
            if board.guess_word(board,"abcbc") == False: # if it says abcbc is not allowed
                return False
            else:
                if board.word_board[-1] == "abcbc" and board.num_board[-1] == [2,2,1,1,0]: # if it gives the correct array for the word jhihy
                    return True
                else:
                    return False


def game():
    # use a while loop and game_over() to check the game is still going
    # ask the player for a word
    # check it using guess_word()
    return

print(wordle_board.test_guess_word(wordle_board))
