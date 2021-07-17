from solver.data.loader.loaderMatrix import LoaderMatrix
from solver.data.matrix.matrixSetDigit import MatrixSetDigit
from solver.data.matrix.matrixSetState import MatrixSetState
from solver.data.matrix.matrixToStr import MatrixToStr
from solver.schema.sudSchema import SudSchema
from solver.schema.sudSchemaJson import SudSchemaJson
from develop.testList import TestList


def main():
    # sud_solve: SudSolveOld = SudSolveOld()
    # sud_solve.solve()

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
        matrix = LoaderMatrix.instance_matrix(schema)

        # print(MatrixToStr.matrix_to_str_groups(matrix))
        # print(MatrixToStr.matrix_to_str_digit(matrix))

        MatrixSetState.set_state(matrix, start_state)
        print(MatrixToStr.matrix_to_str_digit(matrix))
    except Exception as e:
        print(MatrixToStr.matrix_to_str_digit(matrix))
        print(f'Exception {e}')


if __name__ == '__main__':
    main()
