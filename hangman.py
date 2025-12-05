import random
import pytest

class Hangman:
    def __init__(self, word_list):
        print("hangman")
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
        if not self.word_list:
            raise ValueError("Word list is empty. Cannot choose a word.")
        
        self.secret_word = random.choice(self.word_list).lower()
        self.display_word = ["_"] * len(self.secret_word)
        self.guessed_letters = []
        self.remaining_attempts = self.max_attempts

    def guess_letter(self):
        print(type(self.secret_word))
        letter = input() #asks the player for a letter, then returns it
        if letter in self.secret_word:
            print("True")
            return True
        if not letter in self.secret_word:
            print("False")
            return False
        

        #Takes a single letter guessed by the player.
        #- Updates guessed_letters
        #- Updates display_word if correct
        #- Decreases remaining_attempts if incorrect
   
        pass

    def is_game_over(self):
    
        #Checks if the game has ended.
        # Returns True if:
        #- The word has been fully guessed, or
        #- The player has no remaining attempts.
        # Otherwise, returns False.
            
        return self.is_word_guessed() or self.remaining_attempts <= 0
    

        pass

    def is_word_guessed(self):
        missing_found = False # determines if any letters are missing
        for letter in self.display_word:
            if letter == "_":
                missing_found = True # sets to true if a missing letter is found
        if missing_found == True:
            return False
        else: # no missing letters found, game won
            return True

    def get_display_word(self):

        #Returns the current display_word to show the player their progress.

        pass

    def get_guessed_letters(self):

        #Returns the list of letters the player has guessed so far.

        pass

    def get_remaining_attempts(self):

        #Returns how many incorrect guesses the player has left.
    
        return self.remaining_attempts

    def reset_game(self):

        #Resets all relevant game variables to start a new game.

        pass

    def draw_hangman(self):

        #Displays the current state of the hangman drawing based on remaining_attempts.
        #Could be implemented with pixel art or graphical output later.

        pass

def test_choose_word_initializes_secret_and_display():
    """Test that choose_word properly initializes the game state."""
    word_list = ["Ethan", "Parker", "IsGreat"]
    game = Hangman(word_list)
    game.choose_word()

    # Ensure a secret word was chosen from the provided list
    assert game.secret_word in word_list

    # Ensure display_word is initialized to underscores with correct length
    assert len(game.display_word) == len(game.secret_word)
    assert all(char == "_" for char in game.display_word)

    # Ensure guessed_letters is empty at start
    assert game.guessed_letters == []

    # Ensure remaining_attempts reset to max_attempts
    assert game.remaining_attempts == game.max_attempts


def test_choose_word_raises_error_on_empty_list():
    """Test that choose_word raises a ValueError when word_list is empty."""
    game = Hangman([])
    with pytest.raises(ValueError):
        game.choose_word()
        
