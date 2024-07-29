from GUI import (
    Window,
    Line,
    Point
)

def main() -> None:
    win = Window(800, 800)
    
    
    win.draw_line(Line(Point(100, 100), Point(800, 800)), "blue")
    
    
    
    win.wait_for_close()

main()


