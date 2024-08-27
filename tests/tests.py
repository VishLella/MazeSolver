import unittest

from src.maze import maze
from GUI import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 800)
        num_cols = 12
        num_rows = 10
        m1 = maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1.cells),
            num_rows,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols,
        )

if __name__ == "__main__":
    unittest.main()