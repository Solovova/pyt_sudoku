from solve.sudMatrix import SudMatrix
from solve.sudTurnFork import SudTurnFork


class SudSolve:

    def __init__(self):
        self.turnFork: list[SudTurnFork] = list()

    def solve(self) -> bool:
        solved_bool: bool = False
        start_state: list[str] = [
            "9 6 7    ",
            "  1 4    ",
            "   2  81 ",
            " 85     7",
            " 34     6",
            "     4   ",
            "   91 6  ",
            "  76 3  5",
            "       3 "
        ]

        test_matrix = SudMatrix()
        test_matrix.set_start_state(start_state)

        solved: int = 0

        while True:
            while test_matrix.turn():
                pass

            if test_matrix.solved():
                solved = solved + 1
                solved_bool = True
                print(f'Solved: {solved}')
                test_matrix.print_compact()
                # next
                while True:
                    # print(f'fork len:{str(len(self.turnFork))}')
                    if len(self.turnFork) == 0:
                        return solved_bool

                    test_matrix, result = self.turnFork[len(self.turnFork) - 1].next()
                    if result:
                        break
                    if not result:
                        self.turnFork.pop()
                        # print(f'fork back len:{str(len(self.turnFork))}')

            fork: SudTurnFork = SudTurnFork()
            if fork.start(test_matrix):
                self.turnFork.append(fork)
                # print(f'fork up len:{str(len(self.turnFork))}')
            else:
                while True:
                    # print(f'fork len:{str(len(self.turnFork))}')
                    if len(self.turnFork) == 0:
                        return solved_bool

                    test_matrix, result = self.turnFork[len(self.turnFork) - 1].next()
                    if result:
                        break
                    if not result:
                        self.turnFork.pop()
                        # print(f'fork back len:{str(len(self.turnFork))}')
