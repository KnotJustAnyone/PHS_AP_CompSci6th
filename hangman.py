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

    def get_remaining_attempts(self):
        return self.remaining_attempts

    def reset_game(self):
        self.secret_word = None
        self.display_word = None
        self.guessed_letters = []
        self.remaining_attempts = self.max_attempts

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


