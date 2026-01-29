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
        
        print("After your last guess, the display word is now " + self.display_word + ". You currently have " + self.remaining_attempts + " left!")


        #Returns the current display_word to show the player their progress.

        pass

    def self.get_guessed_letters(self):

        print("Letters guessed so far are" + guessed_letters)
        
        
        #Returns the list of letters the player has guessed so far.

        

    def get_remaining_attempts(self):

        #Returns how many incorrect guesses the player has left.
    
        return self.remaining_attempts

    def reset_game(self):

        #the secret word shouldn't be the same as last round
        #maybe take it out of the array of possible words in the word list?
        self.secret_word = None  

        #letters guessed is reset to an empty array
        self.guessed_letters = []

        #attempts are reset also 
        self.remaining_attempts = 6
        self.max_attempts = 6

        #should check if the previous word has been guessed or if the player is out of attempts
        #could also be if the player is stuck and wants to start ovr
        if self.is_game_over():   
            self.choose_word()
        #will reset hangman and choose a new word to play
        
        

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
    assert self.secret_word in word_list

    # Ensure display_word is initialized to underscores with correct length
    assert len(game.display_word) == len(self.secret_word)
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

def get_guessed_letters_test():
    # Test that get_guessed_letters properly returns a list of guessed letters
    game = Hangman(["apple"])
    game.choose_word()

    # Ensure that the list of guessed letters is initially empty
    assert game.get_guessed_letters() == []

    # Pretend player guessed some letters
    game.guessed_letters = ['a', 'e', 's']

    # Test that the function properly returns an updated list of all guessed letters
    assert game.get_guessed_letters() == ['a','e','s']

    




        
def test_get_display_word_returns_string():
    """get_display_word should return the display_word as a spaced string."""
    game = Hangman(["apple"])
    game.secret_word = "apple"
    game.display_word = ["a", "_", "p", "_", "_"]

    result = game.get_display_word()
    assert isinstance(result, str)
    assert result == "a _ p _ _"

def test_get_display_word_with_all_underscores():
    """Should correctly display all underscores when no letters guessed."""
    game = Hangman(["test"])
    game.secret_word = "test"
    game.display_word = ["_", "_", "_", "_"]

    assert game.get_display_word() == "_ _ _ _"

def test_get_display_word_after_full_guess():
    """Should display full word when all letters guessed."""
    game = Hangman(["dog"])
    game.secret_word = "dog"
    game.display_word = ["d", "o", "g"]

    assert game.get_display_word() == "d o g"
    
def get_display_word(self):
    return " ".join(self.display_word)
