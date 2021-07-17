from sudocu_solution.data.mDatMatrix import DatMatrix
from sudocu_solution.data.dat_matrix.mDatMatrixSetDigit import DatMatrixSetDigit


class TurnHard:
    @staticmethod
    def turn(matrix: DatMatrix) -> (bool, bool):  # 1 - is turn, 2 - problem set
        for group in matrix.cell_groups:
            for digit in range(1, matrix.group_len+1):
                digit_can_be_in_cell_count: int = 0
                digit_can_be_in_cell = None
                for cell in group.group:
                    if cell.digit == 0 and digit in cell.can_be:
                        digit_can_be_in_cell_count = digit_can_be_in_cell_count + 1
                        digit_can_be_in_cell = cell
                if digit_can_be_in_cell_count == 1 and digit_can_be_in_cell is not None:
                    return True, DatMatrixSetDigit.set_digit(matrix, digit_can_be_in_cell.x, digit_can_be_in_cell.y, digit, True)

        return False, True
