from sudocu_solution.data.cell.CellToStr import CellToStr
from sudocu_solution.data.DatMatrix import DatMatrix


class MatrixToStr:
    @staticmethod
    def matrix_to_str_digit(matrix: DatMatrix) -> str:
        result: str = ""
        for y in range(matrix.height):
            line: str = ""
            for x in range(matrix.width):
                separator: str = " "
                if (x + 1) % 3 == 0:
                    separator = " | "
                cell_str: str = CellToStr.cell_to_str_digit(matrix.cell_matrix[y][x], matrix)
                line = line + cell_str + separator
            result = result + line + "\n"

            if (y + 1) % 3 == 0:
                result = result + "----------------------------------------------------------------------------------------------\n"
        return result

    @staticmethod
    def matrix_to_str_groups(matrix: DatMatrix) -> str:
        result: str = ""
        for y in range(matrix.height):
            line: str = ""
            for x in range(matrix.width):
                separator: str = " "
                if (x + 1) % 3 == 0:
                    separator = " | "
                cell_str: str = CellToStr.cell_to_str_groups(matrix.cell_matrix[y][x], matrix)
                line = line + cell_str + separator
            result = result + line + "\n"

            if (y + 1) % 3 == 0:
                result = result + "----------------------------------------------------------------------------------------------\n"
        return result
