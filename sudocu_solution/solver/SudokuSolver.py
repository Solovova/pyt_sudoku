import copy

from sudocu_solution.data.DatMatrix import DatMatrix
from sudocu_solution.data.matrix.MatrixSolved import MatrixSolved
from sudocu_solution.data.matrix.MatrixToStr import MatrixToStr
from sudocu_solution.solver.turn.TurnFork import TurnFork
from sudocu_solution.solver.turn.TurnHard import TurnHard
from sudocu_solution.solver.turn.TurnSimple import TurnSimple


class SudokuSolver:
    def __init__(self, matrix: DatMatrix):
        self.matrix: DatMatrix = matrix
        self.solutions: list[DatMatrix] = list()
        self.turn_fork: list[TurnFork] = list()

    def next_fork(self) -> (bool, DatMatrix):  # 1 - end of fork
        while True:
            if len(self.turn_fork) == 0:
                return True, None
            test_matrix, result = self.turn_fork[-1].next()
            if result:
                return False, test_matrix
            else:
                self.turn_fork.pop()

    def turns(self) -> bool:
        while True:
            while True:
                is_turn, is_turn_done = TurnSimple.turn(self.matrix)
                # print(f'Simple turn is_turn: {is_turn}, is_turn_done: {is_turn_done}')
                # print(MatrixToStr.matrix_to_str_digit(self.matrix))
                if not is_turn_done:
                    return False
                if not is_turn:
                    break

            is_turn, is_turn_done = TurnHard.turn(self.matrix)
            # print(f'Hard turn is_turn: {is_turn}, is_turn_done: {is_turn_done}')
            # print(MatrixToStr.matrix_to_str_digit(self.matrix))
            if not is_turn_done:
                return False
            if not is_turn:
                break
        return True

    def solve(self) -> bool:
        print("Start solve")
        # print(MatrixToStr.matrix_to_str_digit(self.matrix))

        while True:
            is_truble = self.turns()

            if MatrixSolved.solved(self.matrix):
                matrix_copy = copy.deepcopy(self.matrix)
                self.solutions.append(matrix_copy)

                # next solve
                is_end_of_fork, self.matrix = self.next_fork()
                if is_end_of_fork:
                    return len(self.solutions) == 0

            turn_fork: TurnFork = TurnFork()
            if turn_fork.start(self.matrix):
                self.turn_fork.append(turn_fork)
            else:
                is_end_of_fork, self.matrix = self.next_fork()
                if is_end_of_fork:
                    return len(self.solutions) == 0
