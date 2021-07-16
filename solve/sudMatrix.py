from solve.sudCell import SudCell


class SudMatrix:
    def __init__(self):
        self.cellsMatrix: list[list[SudCell]] = [[SudCell(x, y) for y in range(9)] for x in range(9)]
        self.cellsArray: list[SudCell] = [item for sublist in self.cellsMatrix for item in sublist]

    def __str__(self):
        result: str = ""
        for cell in self.cellsArray:
            result = result + str(cell) + '\n'
        return result

    def set_digit(self, x: int, y: int, digit: int):
        if self.cellsMatrix[x][y].digit != 0:
            raise Exception(f'Already set digit {self.cellsMatrix[x][y].digit} in cell ({x},{y})')
        self.cellsMatrix[x][y].digit = digit

        for tx in range(9):
            if tx != x:
                self.cellsMatrix[tx][y].add_not_can_be(digit)

        for ty in range(9):
            if ty != y:
                self.cellsMatrix[x][ty].add_not_can_be(digit)

        dx: int = (x // 3) * 3
        dy: int = (y // 3) * 3
        for tx in range(dx, dx + 3):
            for ty in range(dy, dy + 3):
                if tx != x or ty != y:
                    self.cellsMatrix[tx][ty].add_not_can_be(digit)

    def print_compact(self):
        for y in range(9):
            line: str = ""

            for x in range(9):
                separator: str = " "
                if (x + 1) % 3 == 0:
                    separator = " | "
                line = line + self.cellsMatrix[x][y].str_compact() + separator
            print(line)

            if (y + 1) % 3 == 0:
                print('----------------------------------------------------------------------------------------------')

    def set_start_state(self, matrix: list[str]):
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                cell_str = matrix[y][x]
                cell_digit = 0
                if cell_str != " ":
                    cell_digit = int(cell_str)
                self.set_digit(x, y, cell_digit)

    def solved(self) -> bool:
        for x in range(9):
            for y in range(9):
                if self.cellsMatrix[x][y].digit == 0:
                    return False
        return True

    def next_simple_turn(self) -> bool:
        self.cellsArray.sort(key=lambda x: x.get_can_be_len())
        if self.cellsArray[0].get_can_be_len() == 1:
            # print(f'simple ({self.cellsArray[0].x},{self.cellsArray[0].y}) {self.cellsArray[0].get_can_be_first()}')
            self.set_digit(self.cellsArray[0].x, self.cellsArray[0].y, self.cellsArray[0].get_can_be_first())
            return True
        else:
            return False

    def next_hard_turn(self) -> bool:
        # by cube
        for dx in range(3):
            for dy in range(3):
                for digit in range(1, 10):
                    digit_can_be_in_cell: int = 0
                    tx: int = -1
                    ty: int = -1
                    for x in range(dx * 3, dx * 3 + 3):
                        for y in range(dy * 3, dy * 3 + 3):
                            if self.cellsMatrix[x][y].can_be(digit):
                                digit_can_be_in_cell = digit_can_be_in_cell + 1
                                tx = x
                                ty = y
                    if digit_can_be_in_cell == 1:
                        # print(f'hard_d({tx},{ty}) {digit}')
                        self.set_digit(tx, ty, digit)
                        return True

        # by line
        for y in range(9):
            for digit in range(1, 10):
                digit_can_be_in_cell: int = 0
                tx: int = -1
                ty: int = -1
                for x in range(9):
                    if self.cellsMatrix[x][y].can_be(digit):
                        digit_can_be_in_cell = digit_can_be_in_cell + 1
                        tx = x
                        ty = y
                if digit_can_be_in_cell == 1:
                    # print(f'hard_x({tx},{ty}) {digit}')
                    self.set_digit(tx, ty, digit)
                    return True

        # by col
        for x in range(9):
            for digit in range(1, 10):
                digit_can_be_in_cell: int = 0
                tx: int = -1
                ty: int = -1
                for y in range(9):
                    if self.cellsMatrix[x][y].can_be(digit):
                        digit_can_be_in_cell = digit_can_be_in_cell + 1
                        tx = x
                        ty = y
                if digit_can_be_in_cell == 1:
                    # print(f'hard_y({tx},{ty}) {digit}')
                    self.set_digit(tx, ty, digit)
                    return True

        return False

    def turn(self) -> bool:
        if self.next_simple_turn():
            return True
        return self.next_hard_turn()



