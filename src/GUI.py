from tkinter import Tk, BOTH, Canvas
# from GUI import (
#     Line,
#     Point
# )

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


