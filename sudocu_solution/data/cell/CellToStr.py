from sudocu_solution.data.DatCell import DatCell
from sudocu_solution.data.DatMatrix import DatMatrix


class CellToStr:
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

        while len(result) < 10:
            result = " " + result

        return result
