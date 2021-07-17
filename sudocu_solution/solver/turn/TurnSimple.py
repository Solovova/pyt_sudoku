from sudocu_solution.data.DatMatrix import DatMatrix
from sudocu_solution.data.matrix.MatrixSetDigit import MatrixSetDigit


class TurnSimple:
    @staticmethod
    def turn(matrix: DatMatrix) -> (bool, bool):  # 1 - is turn, 2 - problem set
        for cell in matrix.cell_list:
            if len(cell.can_be) == 1:
                return True, MatrixSetDigit.set_digit(matrix, cell.x, cell.y, list(cell.can_be)[0], True)

        return False, True