class wordle_board:

    def __init__(self):
        self.word_list = {
            # list of 5 letter english words, at least 25 words but maybe more
        }
        self.winning_word = "" # choose a word at random from array above
        self.word_board = [] # words are added to this array as they are guessed
        self.num_board = [] # arrays of numbers are added to this array as words are guessed, indicating the correctness of each letter
    
    def guess_word(word): # returns whether a word is eligible, and then checks the letters of the word, adding to the word and number boards.
        # checks the number of letters in the word
        # if not 5, returns false
        # otherwise, continue
        # adds the guessed word to the end of the word board
        # loops through the letters of the guessed word and the letters of the correct word
        # determines if each letter is in the guessed word
        # uses a number variable to look at the position of each letter
        # creates an array, adds 1 for letters that match, 2 for letters with the same position, and 0 for letters that fulfill neither
        # appends this array to the number board
        # prints out the two boards
        return
    
    def game_over():
        # loops through the number board
        # uses a variable to determine the length
        # checks if anything in the number board is [1,1,1,1,1]
        # if so, return True and print out that the player won
        # if not, continue
        # checks if the variable is greater than or equal to 6
        # if so, return True and print out that the player has lost
        return

def game():
    # use a while loop and game_over() to check the game is still going
    # ask the player for a word
    # check it using guess_word()
    return