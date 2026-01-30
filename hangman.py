import random
import pytest

class Hangman:
    def __init__(self, word_list):
        print("hangman")
        self.word_list = word_list
        self.secret_word = None
        self.display_word = None
        self.guessed_letters = []
        self.remaining_attempts = 6
        self.max_attempts = 6

    def choose_word(self):
        if not self.word_list:
            raise ValueError("Word list is empty. Cannot choose a word.")

        self.secret_word = random.choice(self.word_list).lower()
        self.display_word = ["_"] * len(self.secret_word)
        self.guessed_letters = []
        self.remaining_attempts = self.max_attempts

    def guess_letter(self):
        """Asks for input, processes a guess, and updates the game."""
        letter = input("Guess a letter: ").lower()

        # Reject invalid input
        if not (len(letter) == 1 and letter.isalpha()):
            print("Invalid input. Enter one letter.")
            return False

        # Already guessed
        if letter in self.guessed_letters:
            print("You already guessed that letter.")
            return False

        self.guessed_letters.append(letter)

        # Correct guess
        if letter in self.secret_word:
            print("Correct!")
            for i, ch in enumerate(self.secret_word):
                if ch == letter:
                    self.display_word[i] = letter
            return True
        
        # Incorrect guess
        print("Incorrect!")
        self.remaining_attempts -= 1
        return False

    def is_game_over(self):
        return self.is_word_guessed() or self.remaining_attempts <= 0

    def is_word_guessed(self):
        return "_" not in self.display_word

    def get_display_word(self):
        return " ".join(self.display_word)

    def get_guessed_letters(self):
        return self.guessed_letters
        
        print("After your last guess, the display word is now " + self.display_word + ". You currently have " + self.remaining_attempts + " left!")


        #Returns the current display_word to show the player their progress.

        pass

    def get_guessed_letters(self):

        print("Letters guessed so far are" + self.guessed_letters)
        
        
        #Returns the list of letters the player has guessed so far.

        

    def get_remaining_attempts(self):
        return self.remaining_attempts

    def reset_game(self):
        self.secret_word = None
        self.display_word = None
        self.guessed_letters = []
        self.remaining_attempts = self.max_attempts

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
        """Simple ASCII hangman based on remaining attempts."""
        stages = [
            """
             -----
             |   |
             |   O
             |  /|\\
             |  / \\
             |
            -----
            """,
            """
             -----
             |   |
             |   O
             |  /|\\
             |  / 
             |
            -----
            """,
            """
             -----
             |   |
             |   O
             |  /|\\
             |  
             |
            -----
            """,
            """
             -----
             |   |
             |   O
             |  /|
             |  
             |
            -----
            """,
            """
             -----
             |   |
             |   O
             |   |
             |  
             |
            -----
            """,
            """
             -----
             |   |
             |   O
             |
             |
             |
            -----
            """,
            """
             -----
             |   |
             |
             |
             |
             |
            -----
            """
        ]
        print(stages[self.max_attempts - self.remaining_attempts])


# --------------------------
#    PLAYABLE GAME LOOP
# --------------------------

def play_hangman():
    words = ["python", "hangman", "classroom", "testing", "openai"]
    game = Hangman(words)
    game.choose_word()

    print("Welcome to Hangman!")

    # Ensure a secret word was chosen from the provided list
    assert game.secret_word in words

    # Ensure display_word is initialized to underscores with correct length
    assert len(game.display_word) == len(self.secret_word)
    assert all(char == "_" for char in game.display_word)

    while not game.is_game_over():
        print("\nWord:", game.get_display_word())
        print("Guessed letters:", game.get_guessed_letters())
        print("Remaining attempts:", game.get_remaining_attempts())
        game.draw_hangman()
        game.guess_letter()

    # Game ended
    if game.is_word_guessed():
        print("\n🎉 You won! The word was:", game.secret_word)
    else:
        print("\n💀 You lost! The word was:", game.secret_word)
        game.draw_hangman()


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
