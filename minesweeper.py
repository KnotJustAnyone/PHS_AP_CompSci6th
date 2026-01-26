#Minesweeper: Function and test for placing mines
import random

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

    #replacing and then removing flags, but can't flag the cells thatare revealed
    def flag(self, r, c):
        if self.revealed[r][c]:
            return 
        self.flags[r][c] = not self.flags[r][c]
                
     def _calculate_numbers(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in self.mines:
                    self.board[r][c] = 'M'
                else:
                    self.board[r][c] = str(self._count_adjacent_mines(r, c))
                    
    def check_win(self):
            #Win when all non-mine cells are revealed
            for r in range(self.rows):
                for c in range(self.cols):
                    if (r, c) not in self.mines and not self.revealed[r][c]:
                        return False
            return True
        
     #This is the code for the testing part of the project. 
     def setUp(self):
        # A small 5x5 board used for predictable testing
        self.game = Minesweeper(5, 5, 0)
        self.game.mines = {(1,1), (3,3)}
        self.game._calculate_numbers()


    def _count_adjacent_mines(self, r, c):
        """Count mines around (r, c)."""
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if (nr, nc) in self.mines:
                        count += 1
        return count
        
    def _calculate_numbers(self):
        """Fill the board with numbers based on mine positions."""
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in self.mines:
                    self.board[r][c] = 'M'
                else:
                    self.board[r][c] = str(self._count_adjacent_mines(r, c))

          
