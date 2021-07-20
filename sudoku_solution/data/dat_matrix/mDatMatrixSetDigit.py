from sudoku_solution.data.mDatCell import DatCell
from sudoku_solution.data.mDatMatrix import DatMatrix
from sudoku_solution.data.mDatTurn import DatTurn


class DatMatrixSetDigit:
    @staticmethod
    def set_digit(matrix: DatMatrix, x: int, y: int, digit: int, save_turn: bool = True) -> bool:
        # print(f'test set_digit {x},{y} {digit}')
        if matrix.cell_matrix[y][x].digit != 0 or digit in matrix.cell_matrix[y][x].not_can_be:
            # print(f'test MatrixSetDigit {dat_matrix.cell_matrix[y][x]} {digit}')
            return False

        matrix.cell_matrix[y][x].digit = digit
        matrix.cell_matrix[y][x].can_be = set()
        matrix.cell_matrix[y][x].not_can_be = set()

        cells_for_change: list[DatCell] = list()
        for group in matrix.cell_matrix[y][x].groups:
            for cell in matrix.cell_groups[group].group:
                if cell != matrix.cell_matrix[y][x] and cell not in cells_for_change:
                    cells_for_change.append(cell)

        for cell_for_change in cells_for_change:
            if cell_for_change.digit == 0:
                if digit in cell_for_change.can_be:
                    cell_for_change.can_be.remove(digit)
                    cell_for_change.not_can_be.add(digit)

        if save_turn:
            dat_turn: DatTurn = DatTurn(x, y, digit)
            matrix.turns.append(dat_turn)

        return True
