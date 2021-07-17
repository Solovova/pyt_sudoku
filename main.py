from sudocu_solution.data.matrix.MatrixLoader import MatrixLoader
from sudocu_solution.data.matrix.MatrixSetState import MatrixSetState
from sudocu_solution.data.matrix.MatrixToStr import MatrixToStr
from sudocu_solution.schema.SudSchema import SudSchema
from sudocu_solution.schema.SudSchemaJson import SudSchemaJson
from sudocu_solution.solver.SudokuSolver import SudokuSolver


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

    try:
        schema_json: SudSchemaJson = SudSchemaJson()
        schema: SudSchema = SudSchema(schema_json)
        matrix = MatrixLoader.instance_matrix(schema)
        MatrixSetState.set_state(matrix, start_state)
        solver: SudokuSolver = SudokuSolver(matrix)
        solver.solve()
        print(f'Solutions: {len(solver.solutions)}')
        for ind in range(len(solver.solutions)):
            print(f'Solution: {ind + 1}')
            print(MatrixToStr.matrix_to_str_digit(solver.solutions[ind]))
    except Exception as e:
        print(f'Exception {e}')


if __name__ == '__main__':
    main()
