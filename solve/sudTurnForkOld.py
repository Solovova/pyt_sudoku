import copy

from solve.sudMatrixOld import SudMatrixOld


class SudTurnFork:
    sudMatrixBeforeTurn: SudMatrixOld
    canBe: list[int]
    x: int
    y: int
    ind: int

    def start(self, matrix: SudMatrixOld) -> bool:
        self.sudMatrixBeforeTurn = copy.deepcopy(matrix)
        matrix.cellsArray.sort(key=lambda x: x.get_can_be_len())
        if matrix.cellsArray[0].get_can_be_len() <= 1:
            return False

        self.canBe: list[int] = copy.copy(list(matrix.cellsArray[0].get_can_be()))
        self.x: int = matrix.cellsArray[0].x
        self.y: int = matrix.cellsArray[0].y
        self.ind: int = 0
        matrix.set_digit(self.x, self.y, self.canBe[self.ind])
        return True

    def next(self) -> (SudMatrixOld, bool):
        if self.ind + 1 >= len(self.canBe):
            return None, False

        matrix = copy.deepcopy(self.sudMatrixBeforeTurn)
        self.ind = self.ind + 1
        matrix.set_digit(self.x, self.y, self.canBe[self.ind])
        return matrix, True

    def print_info(self):
        print(f'Fork ({self.x},{self.y}) choice {self.canBe} now: {self.canBe[self.ind]} index:{self.ind} ')
