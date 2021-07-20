from typing import Union

import pyautogui

from sudoku_solution.data.mDatMatrix import DatMatrix
from sudoku_solution.data.mDatTurn import DatTurn


class SudokuTurns:
    def __init__(self, matrix: DatMatrix, area: Union[list[int], None] = None,
                 area_button: Union[list[int], None] = None):
        self.area: Union[list[int], None] = area
        self.area_button: Union[list[int], None] = area_button
        self.matrix = matrix

    def get_subarea_buttons(self, area: list[int], dig: int, dimension: int) -> list[int]:
        wx: int = (area[2] - area[0]) // dimension
        sx: int = area[0] + wx * (dig - 1)
        return list([sx, area[1], sx + wx, area[3]])

    def click_area(self, area: list[int]):
        x = int((area[0] + area[2]) // 2)
        y = int((area[1] + area[3]) // 2)

        pyautogui.moveTo(x, y)
        pyautogui.click()
        pyautogui.sleep(0.1)

    def get_subarea(self, area: list[int], x: int, y: int, dx: int, dy: int) -> list[int]:
        wx: int = (area[2] - area[0]) // dx
        wy: int = (area[3] - area[1]) // dy
        sx: int = area[0] + wx * x
        sy: int = area[1] + wy * y
        return list([sx, sy, sx + wx, sy + wy])

    def do_turn(self, turn: DatTurn, matrix: DatMatrix):
        subarea = self.get_subarea(self.area, turn.x, turn.y, matrix.width, matrix.height)
        self.click_area(subarea)
        subarea_buttons = self.get_subarea_buttons(self.area_button, turn.digit, matrix.group_len)
        self.click_area(subarea_buttons)

    def turns(self):
        for ind in range(len(self.matrix.turns)):
            print(self.matrix.turns[ind])
            self.do_turn(self.matrix.turns[ind], self.matrix)
