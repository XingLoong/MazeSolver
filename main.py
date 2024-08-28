import _tkinter
from window import *
from line import *
from point import *
from cell import *

def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell.has_top_wall = False
    cell.draw(50, 50, 100, 100)

    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(255, 255, 300, 300)

    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(255, 325, 300, 400)

    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(50, 125, 100, 175)

    win.wait_for_close()

main()