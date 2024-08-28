import _tkinter
from window import *
from line import *
from point import *

def main():
    win = Window(800, 600)
    point1 = Point(1, 1)
    point2 = Point(200, 200)
    line = Line(point1, point2)
    win.draw_line(line, "red")
    win.wait_for_close()

main()