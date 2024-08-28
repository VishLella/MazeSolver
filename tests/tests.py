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
        

    def test_maze_entrance_exit(self):
        win = Window(800, 800)
        num_cols = 16
        num_rows = 16
        m1 = maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            m1.cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1.cells[num_rows - 1][num_cols - 1].has_bottom_wall,
            False,
        )
if __name__ == "__main__":
    unittest.main()