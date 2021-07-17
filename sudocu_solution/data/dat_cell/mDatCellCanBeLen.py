from sudocu_solution.data.mDatCell import DatCell
from sudocu_solution.data.mDatMatrix import DatMatrix


class DatCellCanBeLen:
    @staticmethod
    def cell_len(cell: DatCell, matrix: DatMatrix) -> int:
        if cell.digit != 0:
            return matrix.group_len + 1
        else:
            return len(cell.can_be)
