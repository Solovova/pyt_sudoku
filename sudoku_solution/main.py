from sudoku_solution.data.dat_matrix.mDatMatrixLoader import DatMatrixLoader
from sudoku_solution.data.dat_matrix.mDatMatrixSetState import DatMatrixSetState
from sudoku_solution.data.dat_matrix.mDatMatrixToStr import DatMatrixToStr
from sudoku_solution.schema.mSudSchema import SudSchema
from sudoku_solution.schema.mSudSchemaJson import SudSchemaJson
from sudoku_solution.solver.mSudokuSolver import SudokuSolver
import logging


def main():
    start_state: list[str] = [
        "8        ",
        "  36     ",
        " 7  9 2  ",
        " 5   7   ",
        "    457  ",
        "   1   3 ",
        "  1    68",
        "  85   1 ",
        " 9    4  "
    ]

    logging.basicConfig(level=logging.INFO)

    try:
        schema_json: SudSchemaJson = SudSchemaJson()
        schema: SudSchema = SudSchema(schema_json)
        matrix = DatMatrixLoader.instance_matrix(schema)
        DatMatrixSetState.set_state(matrix, start_state)
        solver: SudokuSolver = SudokuSolver(matrix)
        solver.solve()

        logging.info(f'\nSolutions: {len(solver.solutions)}')
        for ind in range(len(solver.solutions)):
            logging.info(f'\nSolution: {ind + 1}')
            logging.info(f'\n{DatMatrixToStr.matrix_to_str_digit(solver.solutions[ind])}')
    except Exception as e:
        logging.error(f'Exception {e}', exc_info=True)


if __name__ == '__main__':
    main()
