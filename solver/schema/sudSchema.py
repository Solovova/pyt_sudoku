from solver.schema.sudSchemaJson import SudSchemaJson


class SudSchema:
    def print_compact(self):
        for y in range(len(self.__group)):
            line: str = ""

            for x in range(len(self.__group[y])):
                separator: str = " "
                if (x + 1) % 3 == 0:
                    separator = " | "
                line = line + str(self.__group[y][x]) + separator
            print(line)

            if (y + 1) % 3 == 0:
                print('----------------------------------------------------------------------------------------------')

        print(f'Groups:{self.__groups_quantity}')

    def __init__(self, schema: SudSchemaJson):
        self.__height: int = schema.height
        self.__width: int = schema.width
        self.__groups_quantity: int = 0
        self.__group: list[list[list[int]]] = [[list() for x in range(self.__width)] for y in range(self.__height)]
        for groups in schema.groups_list:
            for y in range(schema.height):
                for x in range(schema.width):
                    self.__group[x][y].append(groups[x][y])
                    if groups[x][y] > self.__groups_quantity:
                        self.__groups_quantity = groups[x][y]

    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width

    @property
    def groups_quantity(self) -> int:
        return self.__groups_quantity

    @property
    def group(self) -> list[list[list[int]]]:
        return self.__group
