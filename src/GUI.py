from tkinter import Tk, BOTH, Canvas
#from Cell import Cell
# from GUI import (
#     Line,
#     Point
# )
class Cell:

    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        #self.__win = win

    def draw(self, canvas: Canvas, color: str) -> None:
        top_left = Point(self.__x1, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        top_right = Point(self.__x2, self.__y1)
        bottom_right = Point(self.__x2, self.__y2)
        if self.has_left_wall:
            l = Line(top_left, bottom_left)
            l.draw(canvas, color)
        if self.has_right_wall:
            l = Line(top_right, bottom_right)
            l.draw(canvas, color)
        if self.has_top_wall:
            l = Line(top_right, top_left)
            l.draw(canvas, color)
        if self.has_bottom_wall:
            l = Line(bottom_right, bottom_left)
            l.draw(canvas, color)

class Point:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line:

    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas: Canvas, color: str) -> None:
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=color, width=2)


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__root = Tk()

        self.__root.title = "Window"
        self.__canvas = Canvas(self.__root, height=self.__height, width=self.__width, bg="white")
        self.__canvas.pack()

        self.__isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__isRunning = True
        while self.__isRunning:
            self.redraw()

    def close(self) -> None:
        self.__isRunning = False

    def draw_line(self, line: Line, color: str) -> None:
        line.draw(self.__canvas, color)

    def draw_cell(self, cell: Cell, color: str) -> None:
        cell.draw(self.__canvas, color)


