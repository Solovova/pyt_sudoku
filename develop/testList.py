class TestList:
    def __init__(self):
        self.width: int = 6
        self.height: int = 4
        self.test_list: list[list[str]] = [
            [f'({x}_{y})' for x in range(self.width)]
            for y in range(self.height)]

    def __str__(self):
        result = ""
        for y in range(self.height):
            line: str = ""
            for x in range(self.width):
                line = line + self.test_list[y][x] + " | "
            result = result + line + "\n"
        return result
