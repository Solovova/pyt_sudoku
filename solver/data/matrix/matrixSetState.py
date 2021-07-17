from solver.data.datMatrix import DatMatrix
from solver.data.matrix.matrixSetDigit import MatrixSetDigit


class MatrixSetState:
    @staticmethod
    def check_list(matrix: DatMatrix, state: list[str]):
        if matrix.height != len(state):
            raise Exception(f'Set state error mast be height {matrix.height} but have {len(state)}')
        for line in state:
            if matrix.width != len(line):
                raise Exception(f'Set state error mast be width {matrix.width} but have {len(line)}')

    @staticmethod
    def set_state(matrix: DatMatrix, state: list[str]):
        MatrixSetState.check_list(matrix, state)

        for y in range(len(state)):
            for x in range(len(state[y])):
                cell_str = state[y][x]
                if cell_str != " ":
                    digit = int(cell_str)
                    if not MatrixSetDigit.set_digit(matrix, x, y, digit):
                        raise Exception(f'Set state error ({x},{y}) digit:{digit}')
