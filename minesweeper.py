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
