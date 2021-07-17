import copy
import logging

from sudocu_solution.data.mDatMatrix import DatMatrix
from sudocu_solution.data.dat_matrix.mDatMatrixSolved import DatMatrixSolved
from sudocu_solution.data.dat_matrix.mDatMatrixToStr import DatMatrixToStr
from sudocu_solution.solver.turn.mTurnFork import TurnFork
from sudocu_solution.solver.turn.mTurnHard import TurnHard
from sudocu_solution.solver.turn.mTurnSimple import TurnSimple


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
                logging.debug(f'\nSimple turn is_turn: {is_turn}, is_turn_done: {is_turn_done}')
                logging.debug(f'\n{DatMatrixToStr.matrix_to_str_digit(self.matrix)}')
                if not is_turn_done:
                    return False
                if not is_turn:
                    break

            is_turn, is_turn_done = TurnHard.turn(self.matrix)
            logging.debug(f'\nHard turn is_turn: {is_turn}, is_turn_done: {is_turn_done}')
            logging.debug(f'\n{DatMatrixToStr.matrix_to_str_digit(self.matrix)}')
            if not is_turn_done:
                return False
            if not is_turn:
                break
        return True

    def solve(self) -> bool:
        # print(MatrixToStr.matrix_to_str_digit(self.dat_matrix))

        while True:
            is_truble = self.turns()

            if DatMatrixSolved.solved(self.matrix):
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
