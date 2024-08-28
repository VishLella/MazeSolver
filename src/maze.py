from GUI import (
    Cell,
    Point,
    Line,
    Window
)

import time

class maze:
    def __init__(self, 
                x1, 
                y1, 
                num_rows, 
                num_cols, 
                cell_size_x, 
                cell_size_y, 
                win):
        
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.cells = self.create_cells()
        self.break_entrance_and_exit()

    def create_cells(self):
        cells = []
        for y in range(self.y1, self.cell_size_y * self.num_rows, self.cell_size_y):
            cell_row = []
            for x in range(self.x1, self.cell_size_x * self.num_cols, self.cell_size_x):
                p1 = Point(x, y)
                p2 = Point(x + self.cell_size_x, y + self.cell_size_y)
                c = Cell(p1.x, p1.y, p2.x, p2.y)
                cell_row.append(c)
                self.win.draw_cell(c, "black")
                self.animate()
            cells.append(cell_row)

        print("Done!")
        return cells        
        # for i in range(len(cells)):
        #     for j in range(len(cells[i])):
        #         self.__draw_cell(cells[i][j], i, j)

    def break_entrance_and_exit(self):
        print(len(self.cells))
        print(len(self.cells[0]))
        entrance_cell = self.cells[0][0]
        exit_cell = self.cells[self.num_rows - 1][self.num_cols - 1]

        entrance_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False

        self.draw_cell(0, 0)
        self.draw_cell(self.num_rows - 1, self.num_cols - 1)

    def draw_cell(self, i, j): 
        #print(self.cells)
        self.win.draw_cell(self.cells[i][j], "black")
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.02)
    


