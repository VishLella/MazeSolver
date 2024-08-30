from GUI import (
    Cell,
    Point,
    Line,
    Window
)

import time
import random

class maze:
    def __init__(self, 
                x1, 
                y1, 
                num_rows, 
                num_cols, 
                cell_size_x, 
                cell_size_y, 
                win,
                seed=None):
        
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.cells = self.create_cells()
        self.break_entrance_and_exit()

        if seed != None:
            random.seed(seed)

        self.break_walls_r(0, 0)

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

        #print("Done!")
        return cells        
        # for i in range(len(cells)):
        #     for j in range(len(cells[i])):
        #         self.__draw_cell(cells[i][j], i, j)

    def break_entrance_and_exit(self):
        #print(len(self.cells))
        #print(len(self.cells[0]))
        entrance_cell = self.cells[0][0]
        exit_cell = self.cells[self.num_rows - 1][self.num_cols - 1]

        entrance_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False

        self.draw_cell(0, 0)
        self.draw_cell(self.num_rows - 1, self.num_cols - 1)

    def break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        cell = self.cells[i][j]

        while True:
            toVisit = []
            #upper cell
            if i - 1 >= 0:
                if self.cells[i - 1][j].visited != True:
                    toVisit.append((i - 1, j, "top"))
            #lower cell
            if i + 1 <= len(self.cells) - 1:
                if self.cells[i - 1][j].visited != True:
                    toVisit.append((i - 1, j, "bot"))
            #left cell
            if j - 1 >= 0:
                if self.cells[i][j - 1].visited != True:
                    toVisit.append((i, j - 1, "left"))
            #right cell
            if j + 1 <= len(self.cells[0]):
                if self.cells[i][j + 1].visited != True:
                    toVisit.append((i, j + 1, "right"))

            if len(toVisit) == 0:
                self.draw_cell(i, j)
                return
            
            num = random.randint(0, len(toVisit) - 1)
            if toVisit[num][2] == "top":
                self.cells[i][j].has_top_wall = False
                self.cells[i - 1][j].has_bottom_wall = False
                self.draw_cell(i, j)
                self.draw_cell(i - 1, j)
                toVisit.pop(num)
                self.break_walls_r(i - 1, j)
            elif toVisit[num][2] == "bot":
                self.cells[i][j].has_bottom_wall = False
                self.cells[i + 1][j].has_top_wall = False
                self.draw_cell(i, j)
                self.draw_cell(i + 1, j)
                toVisit.pop(num)
                self.break_walls_r(i + 1, j)
            elif toVisit[num][2] == "left":
                self.cells[i][j].has_left_wall = False
                self.cells[i][j - 1].has_right_wall = False
                self.draw_cell(i, j)
                self.draw_cell(i, j - 1)
                toVisit.pop(num)
                self.break_walls_r(i, j - 1)
            elif toVisit[num][2] == "right":
                self.cells[i][j].has_right_wall = False
                self.cells[i][j + 1].has_leftm_wall = False
                self.draw_cell(i, j)
                self.draw_cell(i, j + 1)
                toVisit.pop(num)
                self.break_walls_r(i, j + 1)
         

    def draw_cell(self, i, j): 
        #print(self.cells)
        self.win.draw_cell(self.cells[i][j], "black")
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.02)
    


