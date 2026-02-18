import random

DIFFICULTIES = {
    "easy":    (8, 8, 10),
    "medium":  (12, 12, 20),
    "hard":    (16, 16, 40)
 #(rows, columns, mines)
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
        
    def _place_mines(self): 
        while len(self.mines) < self.num_mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            self.mines.add((r, c))

    def _count_adjacent_mines(self, r, c):
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
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in self.mines:
                    self.board[r][c] = 'M'
                else:
                    self.board[r][c] = str(self._count_adjacent_mines(r, c))
                    
    def reveal(self, r, c):
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            return True
        if self.flags[r][c]:
            return True
        if self.revealed[r][c]:
            return True
        self.revealed[r][c] = True

        # Stepped on a mine
        if (r, c) in self.mines:
            return False
        if self.board[r][c] == '0':
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        if not self.revealed[nr][nc]:
                            self.reveal(nr, nc)

        return True
        
    def flag(self, r, c):
        if self.revealed[r][c]:
            return  # Can't flag revealed cells
        self.flags[r][c] = not self.flags[r][c]
        
    def display(self, reveal_all=False):
        print("\n   " + " ".join(str(i) for i in range(self.cols)))
        print("  " + "--" * self.cols)

        for r in range(self.rows):
            row_str = f"{r}| "
            for c in range(self.cols):
                if reveal_all:
                    row_str += self.board[r][c] + " "
                else:
                    if self.flags[r][c]:
                        row_str += "F "
                    elif self.revealed[r][c]:
                        row_str += self.board[r][c] + " "
                    else:
                        row_str += ". "
            print(row_str)
        print()

    def check_win(self):
        """Win when all non-mine cells are revealed."""
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) not in self.mines and not self.revealed[r][c]:
                    return False
        return True


    def setUp(self):
        self.game = Minesweeper(5, 5, 0)
        self.game.mines = {(1,1), (3,3)}
        self.game._calculate_numbers()

    def test_mine_placement(self):
        game2 = Minesweeper(6, 6, 8)
        self.assertEqual(len(game2.mines), 8)
        for (r, c) in game2.mines:
            self.assertTrue(0 <= r < 6)
            self.assertTrue(0 <= c < 6)

    def test_adjacent_mine_count(self):
        self.assertEqual(self.game._count_adjacent_mines(0,0), 1)
        self.assertEqual(self.game._count_adjacent_mines(2,2), 2)
        self.assertEqual(self.game._count_adjacent_mines(4,4), 1)

    def test_reveal_safe_cell(self):
        result = self.game.reveal(0, 0)
        self.assertTrue(result)              
        self.assertTrue(self.game.revealed[0][0])

    def test_reveal_mine(self):
        result = self.game.reveal(1, 1)     
        self.assertFalse(result)

    def test_flagging(self):
        self.game.flag(0, 0)
        self.assertTrue(self.game.flags[0][0])
        self.game.flag(0, 0)
        self.assertFalse(self.game.flags[0][0])  # flag removed
        
    def test_flag_does_not_affect_revealed(self):
        self.game.reveal(0, 0)
        self.game.flag(0, 0)
        self.assertFalse(self.game.flags[0][0])  # cannot flag revealed cells

    def test_flood_fill(self):
        self.game.mines = {(4,4)} 
        self.game._calculate_numbers()
        self.game.reveal(0, 0) 
        revealed_count = sum(sum(row) for row in self.game.revealed)
        self.assertGreater(revealed_count, 10)

    def test_win_condition(self):
        # Reveal everything except mines
        for r in range(5):
            for c in range(5):
                if (r, c) not in self.game.mines:
                    self.game.revealed[r][c] = True

        self.assertTrue(self.game.check_win())

          
