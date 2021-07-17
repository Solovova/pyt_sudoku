class SudCellOld:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.__canBe: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.__notCanBe: set[int] = set()
        self.digit: int = 0

    def add_not_can_be(self, i: int):
        if i in self.__canBe and self.digit == 0:
            self.__canBe.remove(i)
            self.__notCanBe.add(i)

    def __str__(self) -> str:
        return f'x:{self.x} y:{self.y} canBe:{str(self.__canBe)}'

    def get_can_be_len(self) -> int:
        if self.digit != 0:
            return 10
        else:
            return len(self.__canBe)

    def get_can_be_first(self) -> int:
        return list(self.__canBe)[0]

    def can_be(self, digit: int) -> bool:
        if self.digit == 0:
            return digit in self.__canBe
        else:
            return False

    def get_can_be(self) -> set[int]:
        return self.__canBe

    def str_compact(self) -> str:
        len_need: int = 9
        result: str = ""
        if self.digit == 0:
            for canBeEl in self.__canBe:
                result = result + str(canBeEl)
        else:
            result = f'({str(self.digit)})'

        while len(result) < len_need:
            result = " " + result

        return result