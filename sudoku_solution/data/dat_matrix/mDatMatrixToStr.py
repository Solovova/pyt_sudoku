from sudoku_solution.data.dat_cell.mDatCellToStr import DatCellToStr
from sudoku_solution.data.mDatMatrix import DatMatrix


class DatMatrixToStr:
    @staticmethod
    def matrix_to_str_digit(matrix: DatMatrix) -> str:
        result: str = ""
        for y in range(matrix.height):
            line: str = ""
            for x in range(matrix.width):
                separator: str = " "
                if (x + 1) % 3 == 0:
                    separator = " | "
                cell_str: str = DatCellToStr.cell_to_str_digit(matrix.cell_matrix[y][x], matrix)
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
                cell_str: str = DatCellToStr.cell_to_str_groups(matrix.cell_matrix[y][x], matrix)
                line = line + cell_str + separator
            result = result + line + "\n"

            if (y + 1) % 3 == 0:
                result = result + "----------------------------------------------------------------------------------------------\n"
        return result
