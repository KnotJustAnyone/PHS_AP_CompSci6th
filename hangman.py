import random
#import pytest

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

    #this is the function for the list. This function checks through the word 
    #(list of strings) to see if the guessed letter is in it.
    def guess_letter(self):
        """Asks for input, processes a guess, and updates the game."""
        if self.secret_word is None:
            raise ValueError("No secret word chosen yet. Call choose_word() before guessing.")

        letter = input("Guess a letter: ").lower().strip()

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            return False

        if letter in self.guessed_letters:
            print(f"You already guessed '{letter}'. Try a different letter.")
            return False

        self.guessed_letters.append(letter)

        if letter in self.secret_word:
            for i in range(len(self.secret_word)):
                if self.secret_word[i] == letter:
                    self.display_word[i] = letter
            print("Correct")
            return True
        else:
            self.remaining_attempts -= 1
            print("Incorrect")
            return False

        # Takes a single letter guessed by the player.
        # - Updates guessed_letters
        # - Updates display_word if correct
        # - Decreases remaining_attempts if incorrect

    def guess_word(self, guess):
        """
        Let the player guess the entire word at once>
        Returns: (bool, str) - (is_correct, message) 
        """
        if self. secret_word is None: 
            return False, "No word chosen yet. Call choose_ word() first."
        if self.is_game_over(): 
            return False, "The game is already over." 

        guess = guess.strip().lower ()
        if not guess.isalpha():
            return False, "Your guess should contain letters only."

        if guess == self.secret_word: 
            self.display_word = list(self.secret_word) 
            return True, f"Correct! The word was'{self.secret_word}'."
        else:
                # Wrong guess costs one attempt
                self.remaining_attempts -= 1
                return False, f"'{guess}' is not the word. Attempts left: {self.remaining_attempts}"

    def is_game_over(self):
    
        #Checks if the game has ended.
        # Returns True if:
        #- The word has been fully guessed, or
        #- The player has no remaining attempts.
        # Otherwise, returns False.
            
        return self.is_word_guessed() or self.remaining_attempts <= 0

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
        return " ".join(self.display_word)

    def get_guessed_letters(self):
        return self.guessed_letters
        
    def get_remaining_attempts(self):

        #Returns how many incorrect guesses the player has left.
    
        return self.remaining_attempts

    def draw_hangman(self):
        """Displays a simple hangman stage based on remaining attempts."""
        stages = [
            "\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========\n",
            "\n  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========\n",
            "\n  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========\n",
            "\n  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========\n",
            "\n  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========\n",
            "\n  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========\n",
            "\n  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n",
        ]

        index = self.max_attempts - self.remaining_attempts
        if index < 0:
            index = 0
        elif index >= len(stages):
            index = len(stages) - 1

        print(stages[index])

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
        
'''

Maddie Korman developed function

Take in a 5 letter word board, an array of inputs (_ _ _ _ _)

   inputs align with letters in the word or not

   if letter is in word, fills blank

Returns if the player is right or wrong, tells them to guess again

   if word is guessed or no more guesses left, game is over

'''


def play_hangman():
    words = ["python", "hangman", "classroom", "testing", "openai"]
    game = Hangman(words)


    game.choose_word()

    print("hangman!")

    while not game.is_game_over():
        print("\nWord:", game.get_display_word())
        print("Guessed letters:", game.get_guessed_letters())
        print("Remaining attempts:", game.get_remaining_attempts())
    
        game.guess_letter()

    # Game ended
    if game.is_word_guessed():
        print("\n🎉 You won! The word was:", game.secret_word)
    else:
        print("\n💀 You lost! The word was:", game.secret_word)
        ##game.draw_hangman()

def test_choose_word_initializes_secret_and_display(self):
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

def test_guess_letter_incorrect():
    game = Hangman(["apple"])
    game.secret_word = "apple"

    mock = MockInput("z")
    original_input = __builtins__.input
    __builtins__.input = mock

    result = game.guess_letter()

    __builtins__.input = original_input

    assert result is False


def test_guess_letter_prints_type():
    game = Hangman(["apple"])
    game.secret_word = "apple"

    mock = MockInput("a")
    original_input = __builtins__.input
    __builtins__.input = mock

    # capture printed text
    import io, sys
    captured = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = captured

    game.guess_letter()

    sys.stdout = original_stdout
    __builtins__.input = original_input

    output = captured.getvalue()
    assert "class 'str'" in output

    game.guess_letter()

    # Should remain unchanged
    assert game.get_remaining_attempts() == game.max_attempts


def test_get_remaining_attempts_matches_internal_state():
    """Ensure the getter returns the internal value even after manual change."""
    game = Hangman(["hello"])
    game.remaining_attempts = 3  # simulate game progress manually
    assert game.get_remaining_attempts() == 3
   
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

game = Hangman(["word"])
        
# --- helper to mock input() ---
class MockInput:
    def __init__(self, value):
        self.value = value
    def __call__(self, *args, **kwargs):
        return self.value


def run_test(name, func):
    try:
        func()
        print(f"[PASS] {name}")
    except AssertionError as e:
        print(f"[FAIL] {name}")
        print("       ", e)


# --- TESTS ---

def test_guess_letter_correct():
    game = Hangman(["apple"])
    game.secret_word = "apple"

    mock = MockInput("a")
    original_input = __builtins__.input
    __builtins__.input = mock

    result = game.guess_letter()

    __builtins__.input = original_input  # restore input

    assert result is True


if __name__ == "__main__":
    play_hangman()

