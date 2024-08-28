from line import *
from point import *

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall)
        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall)
        if self.has_bottom_wall:
            bot_wall = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bot_wall)
        if self.has_left_wall:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_wall)
        
    def draw_move(self, to_cell, undo= False):
        x_centre1 = (self._x1 + self._x2) / 2
        y_centre1 = (self._y1 + self._y2) / 2
        x_centre2 = (to_cell._x1 + to_cell._x2) / 2
        y_centre2 = (to_cell._y1 + to_cell._y2) / 2

        if undo:
            self._win.draw_line(
                Line(Point(x_centre1, y_centre1), Point(x_centre2, y_centre2)), "gray")
        else:
            self._win.draw_line(
            Line(Point(x_centre1, y_centre1), Point(x_centre2, y_centre2)), "red"
        )