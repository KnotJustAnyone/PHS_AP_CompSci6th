
class Hangman:
    def __init__(self, word_list):

        #Initialize the Hangman game.
        #- word_list: list of words to randomly choose from for the game
        #- This function sets up the starting state of the game.
  
        self.word_list = word_list              # List of potential words to use
        self.secret_word = None                 # The word to be guessed
        self.display_word = None                # The current state of the guessed word (e.g. "_ _ a _ _")
        self.guessed_letters = []               # List of letters guessed so far
        self.remaining_attempts = 6             # Number of incorrect guesses allowed
        self.max_attempts = 6                   # Maximum allowed attempts

    def choose_word(self):

        #Randomly selects a word from the word list and sets it as the secret word.
        #Also initializes the display_word with underscores.
        pass

    def guess_letter(self, letter):

        #Takes a single letter guessed by the player.
        #- Updates guessed_letters
        #- Updates display_word if correct
        #- Decreases remaining_attempts if incorrect
   
        pass

    def is_game_over(self):

        #Checks if the game has ended due to either:
        #- All letters guessed
        #- Player has run out of attempts
        #Returns True if the game is over, otherwise False.

        pass

    def is_word_guessed(self):
    
        #Checks if the entire word has been successfully guessed.
        #Returns True if the display_word matches the secret_word.
       
        pass

    def get_display_word(self):

        #Returns the current display_word to show the player their progress.

        pass

    def get_guessed_letters(self):

        #Returns the list of letters the player has guessed so far.

        pass

    def get_remaining_attempts(self):

        #Returns how many incorrect guesses the player has left.

        pass

    def reset_game(self):

        #Resets all relevant game variables to start a new game.

        pass

    def draw_hangman(self):

        #Displays the current state of the hangman drawing based on remaining_attempts.
        #Could be implemented with pixel art or graphical output later.

        pass
