import copy

from sudocu_solution.data.DatMatrix import DatMatrix
from sudocu_solution.data.cell.CellCanBeLen import CellCanBeLen
from sudocu_solution.data.matrix.MatrixSetDigit import MatrixSetDigit


class TurnFork:
    matrix_before_turn: DatMatrix
    can_be: list[int]
    x: int
    y: int
    ind: int

    def start(self, matrix: DatMatrix) -> bool:
        self.matrix_before_turn = copy.deepcopy(matrix)
        matrix.cell_list.sort(key=lambda x: CellCanBeLen.cell_len(x, matrix))
        if CellCanBeLen.cell_len(matrix.cell_list[0], matrix) <= 1:
            return False

        self.can_be: list[int] = copy.copy(list(matrix.cell_list[0].can_be))
        self.x: int = matrix.cell_list[0].x
        self.y: int = matrix.cell_list[0].y
        self.ind: int = 0
        MatrixSetDigit.set_digit(matrix, self.x, self.y, self.can_be[self.ind], True)
        return True

    def next(self) -> (DatMatrix, bool):
        if self.ind + 1 >= len(self.can_be):
            return None, False

        matrix = copy.deepcopy(self.matrix_before_turn)
        self.ind = self.ind + 1
        MatrixSetDigit.set_digit(matrix, self.x, self.y, self.can_be[self.ind], True)
        return matrix, True

    def print_info(self):
        print(f'Fork ({self.x},{self.y}) choice {self.can_be} now: {self.can_be[self.ind]} index:{self.ind} ')
