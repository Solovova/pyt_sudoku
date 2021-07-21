import logging
import time
from typing import Union

from sudoku_ocr.mSudokuOcr import SudokuOcr
from sudoku_solution.data.dat_matrix.mDatMatrixLoader import DatMatrixLoader
from sudoku_solution.data.dat_matrix.mDatMatrixSetState import DatMatrixSetState
from sudoku_solution.data.mDatMatrix import DatMatrix
from sudoku_solution.schema.mSudSchema import SudSchema
from sudoku_solution.schema.mSudSchemaJson import SudSchemaJson
from sudoku_solution.solver.mSudokuSolver import SudokuSolver
from sudoku_turns.mSudokuTurns import SudokuTurns
from sudoku_turns.mSudokuTurnsTread import SudokuTurnsTread


class SudokuMain:
    def __init__(self, area: Union[list[int], None] = None, filename: Union[str, None] = None,
                 area_button: Union[list[int], None] = None):
        self.schema_json: SudSchemaJson = SudSchemaJson()
        self.schema: SudSchema = SudSchema(self.schema_json)
        self.matrix: DatMatrix = DatMatrixLoader.instance_matrix(self.schema)
        self.sudoku_ocr: SudokuOcr = SudokuOcr(width=self.matrix.width, height=self.matrix.height)

        self.area: Union[list[int], None] = area
        self.area_button: Union[list[int], None] = area_button
        self.filename: Union[str, None] = filename

    def turns(self, matr: DatMatrix):
        if self.area is None or self.area_button is None:
            return
        sudoku_turns: SudokuTurns = SudokuTurns(matr, area=self.area, area_button=self.area_button)
        sudoku_turns.turns()
        # sudoku_turns_tread: SudokuTurnsTread = SudokuTurnsTread(sudoku_turns)
        # sudoku_turns_tread.start()

    def ocr(self) -> list[str]:
        self.sudoku_ocr.set_img(filename=self.filename, area=self.area)
        if logging.DEBUG <= logging.root.level:
            self.sudoku_ocr.dat_sudoku_image.show_img()
        self.sudoku_ocr.dat_sudoku_image.clean_parts()
        return self.sudoku_ocr.get_list()

    def solve(self, state_list: list[str]) -> (bool, Union[DatMatrix, None]):
        try:
            DatMatrixSetState.set_state(self.matrix, state_list)
            solver: SudokuSolver = SudokuSolver(self.matrix)
            if solver.solve():
                return True, solver.solutions[0]
            else:
                return False, None
        except Exception as e:
            logging.error(f'Exception {e}', exc_info=True)
