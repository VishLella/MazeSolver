from GUI import (
    Window,
    Line,
    Point,
    Cell
)
import random
#from Cell import Cell

def main() -> None:
    win = Window(800, 800)
    
    for x in range(0, 800, 50):
        p1 = Point(x, x)
        p2 = Point(x + 50, x + 50)
        c = Cell(p1.x, p1.y, p2.x, p2.y)
        num = random.randint(2, 10)
        c.has_right_wall = False
        # if num > 8:
        #     c.has_top_wall = False
        # elif num > 6:
        #     c.has_right_wall = False
        # elif num > 4:
        #     c.has_left_wall = False
        # elif num > 2:
        #     c.has_bottom_wall = False
        win.draw_cell(c, "black")
    
    #win.draw_line(Line(Point(100, 100), Point(800, 800)), "blue")
    
    
    
    win.wait_for_close()

main()


