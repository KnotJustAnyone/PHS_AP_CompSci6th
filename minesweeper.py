#Minesweeper: Function and test for placing mines
import random
def Minesweeper(a,b,c):
        return 

DIFFICULTIES = {
    "easy":    (8, 8, 10),
    "medium":  (12, 12, 20),
    "hard":    (16, 16, 40)
#where each entry is given as (rows, columns, mines)
}

class Minesweeper:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines

        # Game state
        self.board = [['0' for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.flags = [[False for _ in range(cols)] for _ in range(rows)]
        self.mines = set()

        self._place_mines()
        self._calculate_numbers()
        
def test_place_mines(self):
        game2 = Minesweeper(6, 6, 8)
        self.assertEqual(len(game2.mines), 8)
        # Ensure all mines within bounds
        for (r, c) in game2.mines:
            self.assertTrue(0 <= r < 6)
            self.assertTrue(0 <= c < 6)

def _place_mines(self):
        #Randomly place mines in unique positions.
        while len(self.mines) < self.num_mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            self.mines.add((r, c))
                
def check_win(self):
        #Win when all non-mine cells are revealed
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) not in self.mines and not self.revealed[r][c]:
                    return False
        return True


          
