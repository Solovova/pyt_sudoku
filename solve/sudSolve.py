from solve.sudMatrix import SudMatrix
from solve.sudTurnFork import SudTurnFork


class SudSolve:

    def __init__(self):
        self.turnFork: list[SudTurnFork] = list()

    def next_fork(self) -> (bool, SudMatrix):  # 1 - end of fork
        while True:
            if len(self.turnFork) == 0:
                return True, None
            test_matrix, result = self.turnFork[-1].next()
            if result:
                return False, test_matrix
            else:
                self.turnFork.pop()

    def solve(self) -> bool:
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

        test_matrix = SudMatrix()
        test_matrix.set_start_state(start_state)

        solved_bool: bool = False
        solved_count: int = 0

        while True:
            while test_matrix.turn():
                pass

            if test_matrix.solved():
                solved_count = solved_count + 1
                solved_bool = True
                print(f'Solved: {solved_count}')
                test_matrix.print_compact()
                # next solve
                end_of_fork, test_matrix = self.next_fork()
                if end_of_fork:
                    return solved_bool

            fork: SudTurnFork = SudTurnFork()
            if fork.start(test_matrix):
                self.turnFork.append(fork)
            else:
                end_of_fork, test_matrix = self.next_fork()
                if end_of_fork:
                    return solved_bool
