from solve.sudCell import SudCell


class SudMatrix:
    def __init__(self):
        self.cellsMatrix: list[list[SudCell]] = [[SudCell(x, y) for x in range(9)] for y in range(9)]
        self.cellsArray: list[SudCell] = [item for sublist in self.cellsMatrix for item in sublist]

    def __str__(self):
        result: str = ""
        for cell in self.cellsArray:
            result = result + str(cell) + '\n'
        return result

    def set_digit(self, x: int, y: int, digit: int):
        self.cellsMatrix[x][y].digit = digit

        for tx in range(9):
            if tx != x:
                self.cellsMatrix[tx][y].add_not_can_be(digit)

        for ty in range(9):
            if ty != y:
                self.cellsMatrix[x][ty].add_not_can_be(digit)

    def print_compact(self):
        for x in range(9):
            line: str = ""

            for y in range(9):
                separator: str = " "
                if (y+1) % 3 == 0:
                    separator = " | "
                line = line + self.cellsMatrix[x][y].str_compact() + separator
            print(line)

            if (x+1) % 3 == 0:
                print('----------------------------------------------------------------------------------------------')
