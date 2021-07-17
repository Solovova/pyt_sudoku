from sudocu_solution.data.DatMatrix import DatMatrix
from sudocu_solution.data.matrix.MatrixToStr import MatrixToStr
from sudocu_solution.solver.turn.TurnHard import TurnHard
from sudocu_solution.solver.turn.TurnSimple import TurnSimple


class SudokuSolver:
    def __init__(self, matrix: DatMatrix):
        self.matrix: DatMatrix = matrix
        self.solutions: list[DatMatrix] = list()

    def turns(self) -> bool:
        while True:
            while True:
                is_turn, is_turn_done = TurnSimple.turn(self.matrix)
                print(f'Simple turn is_turn: {is_turn}, is_turn_done: {is_turn_done}')
                print(MatrixToStr.matrix_to_str_digit(self.matrix))
                if not is_turn_done:
                    return False
                if not is_turn:
                    break

            is_turn, is_turn_done = TurnHard.turn(self.matrix)
            print(f'Hard turn is_turn: {is_turn}, is_turn_done: {is_turn_done}')
            print(MatrixToStr.matrix_to_str_digit(self.matrix))
            if not is_turn_done:
                return False
            if not is_turn:
                break
        return True

    def solve(self):
        print("Start solve")
        print(MatrixToStr.matrix_to_str_digit(self.matrix))
        self.turns()
