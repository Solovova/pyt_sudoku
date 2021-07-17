from sudocu_solution.data.DatCell import DatCell
from sudocu_solution.data.DatMatrix import DatMatrix


class CellCanBeLen:
    @staticmethod
    def cell_len(cell: DatCell, matrix: DatMatrix) -> int:
        if cell.digit != 0:
            return matrix.group_len + 1
        else:
            return len(cell.can_be)
