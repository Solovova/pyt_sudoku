import copy

from sudoku_solution.data.mDatMatrix import DatMatrix
from sudoku_solution.data.dat_cell.mDatCellCanBeLen import DatCellCanBeLen
from sudoku_solution.data.dat_matrix.mDatMatrixSetDigit import DatMatrixSetDigit


class TurnFork:
    matrix_before_turn: DatMatrix
    can_be: list[int]
    x: int
    y: int
    ind: int

    def start(self, matrix: DatMatrix) -> (bool, bool):
        self.matrix_before_turn = copy.deepcopy(matrix)
        matrix.cell_list.sort(key=lambda x: DatCellCanBeLen.cell_len(x, matrix))
        if DatCellCanBeLen.cell_len(matrix.cell_list[0], matrix) <= 1:
            return False, False

        self.can_be: list[int] = copy.copy(list(matrix.cell_list[0].can_be))
        self.x: int = matrix.cell_list[0].x
        self.y: int = matrix.cell_list[0].y
        self.ind: int = 0

        return True, DatMatrixSetDigit.set_digit(matrix, self.x, self.y, self.can_be[self.ind], True)

    def next(self) -> (DatMatrix, bool, bool):
        if self.ind + 1 >= len(self.can_be):
            return None, False, False

        matrix = copy.deepcopy(self.matrix_before_turn)
        self.ind = self.ind + 1

        return matrix, True, DatMatrixSetDigit.set_digit(matrix, self.x, self.y, self.can_be[self.ind], True)

    def print_info(self):
        print(f'Fork ({self.x},{self.y}) choice {self.can_be} now: {self.can_be[self.ind]} index:{self.ind} ')
