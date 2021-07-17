from sudocu_solution.data.DatMatrix import DatMatrix


class MatrixSolved:
    @staticmethod
    def solved(matrix: DatMatrix) -> bool:
        for cell in matrix.cell_list:
            if cell.digit == 0:
                return False
        return True
