from sudoku_solution.data.mDatMatrix import DatMatrix


class DatMatrixSolved:
    @staticmethod
    def solved(matrix: DatMatrix) -> bool:
        for cell in matrix.cell_list:
            if cell.digit == 0:
                return False
        return True
