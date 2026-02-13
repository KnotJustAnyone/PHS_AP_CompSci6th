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

        #Takes a single letter guessed by the player.
        #- Updates guessed_letters
        #- Updates display_word if correct
        #- Decreases remaining_attempts if incorrect
   
        pass
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
        if not guess. isaplha():
            return False, "Your guess should contain letters only."

        if guess == self.secret_word: 
            self.display_word = list(self.secret_word) 
            return True, f"Corret! The word was'{self.secret_word}'."
        else:
                # Wrong guess costs one attempt
                self.remaining_attempts -= 1
                return False, f"'{guess}' is not the word. Attempts left: {self.remaining_attempts}"
 
    def is_game_over(self):
        """
        Checks if the game has ended.
        Returns True if:
        - The word has been fully guessed, or
        - The player has no remaining attempts.
        Otherwise, returns False.
        """
        return self.is_word_guessed() or self.remaining_attempts <= 0

            

    def is_word_guessed(self):
        """
        Checks if the entire word has been successfully guessed.
        Returns True if the display_word matches the secret_word.
        """
        return "".join(self.display_word) == self.secret_word

    def is_word_guessed(self):
        return "_" not in self.display_word

    
    def get_display_word(self):
        return " ".join(self.display_word)

    def get_guessed_letters(self):
        return self.guessed_letters
        

    def get_guessed_letters(self):
        #Returns the list of letters the player has guessed so far.
        print("Letters guessed so far are" + self.guessed_letters)

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
    assert len(game.display_word) == len(game.secret_word)
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

#Test -----
def test_is_game_over_when_word_guessed():
    """Game should be over when the word is fully guessed."""
    game = Hangman(["test"])
    game.secret_word = "test"
    game.display_word = list("test")  # fully guessed
    game.remaining_attempts = 3       # still have tries left

    assert game.is_game_over() is True


def test_is_game_over_when_no_attempts_left():
    """Game should be over when remaining_attempts reaches 0."""
    game = Hangman(["test"])
    game.secret_word = "test"
    game.display_word = ["_", "_", "_", "_"]  # not guessed
    game.remaining_attempts = 0

    assert game.is_game_over() is True


def test_is_game_over_when_not_finished():
    """Game should continue when the word is not guessed and attempts remain."""
    game = Hangman(["test"])
    game.secret_word = "test"
    game.display_word = ["t", "_", "_", "t"]
    game.remaining_attempts = 4

    assert game.is_game_over() is False

def test_get_remaining_attempts_initial():
    """Ensure get_remaining_attempts returns the correct initial value."""
    word_list = ["test"]
    game = Hangman(word_list)
    game.choose_word()

    assert game.get_remaining_attempts() == game.max_attempts


def test_get_remaining_attempts_after_wrong_guess(monkeypatch):
    """Ensure remaining attempts decrease after a wrong guess."""
    word_list = ["apple"]
    game = Hangman(word_list)
    game.choose_word()

    # Force user input to be a wrong guess
    monkeypatch.setattr("builtins.input", lambda: "z")

    # Call guess_letter() which should reduce attempts
    game.guess_letter()

    assert game.get_remaining_attempts() == game.max_attempts - 1


def test_get_remaining_attempts_after_correct_guess(monkeypatch):
    """Ensure remaining attempts do not decrease after a correct guess."""
    word_list = ["banana"]
    game = Hangman(word_list)
    game.choose_word()

    correct_letter = game.secret_word[0]  # choose a known correct letter
    monkeypatch.setattr("builtins.input", lambda: correct_letter)

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
