from sudocu_solution.data.mDatCell import DatCell
from sudocu_solution.data.mDatMatrix import DatMatrix


class DatCellToStr:
    @staticmethod
    def cell_to_str_digit(cell: DatCell, matrix: DatMatrix) -> str:
        result: str = ""
        if cell.digit == 0:
            for el in cell.can_be:
                result = result + str(el)
        else:
            result = f'({str(cell.digit)})'

        while len(result) < matrix.group_len:
            result = " " + result

        return result

    @staticmethod
    def cell_to_str_groups(cell: DatCell, matrix: DatMatrix) -> str:
        result = f'({str(cell.groups)})'

        while len(result) < matrix.group_len + 1:
            result = " " + result

        return result
