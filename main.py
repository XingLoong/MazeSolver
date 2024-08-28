import _tkinter
from window import *
from line import *
from point import *
from cell import *

def main():
    win = Window(800, 600)

    cell1 = Cell(win)
    cell1.has_top_wall = False
    cell1.draw(50, 50, 100, 100)

    cell2 = Cell(win)
    cell2.has_right_wall = False
    cell2.draw(255, 255, 300, 300)

    cell1.draw_move(cell2)

    cell3 = Cell(win)
    cell3.has_bottom_wall = False
    cell3.draw(255, 325, 300, 400)

    cell2.draw_move(cell3)

    cell4 = Cell(win)
    cell4.has_left_wall = False
    cell4.draw(50, 125, 100, 175)

    cell3.draw_move(cell4, True)

    win.wait_for_close()

main()