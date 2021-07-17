class SudSchemaJson:
    def test_groups(self):
        if len(self.__groups_list) == 0:
            raise Exception("SudSchema init groups is zero len")
        if len(self.__groups_list[0]) == 0:
            raise Exception("SudSchema init groups[0] is zero len")
        if len(self.__groups_list[0][0]) == 0:
            raise Exception("SudSchema init groups[0][0] is zero len")

        self.__height: int = len(self.__groups_list[0])
        self.__width: int = len(self.__groups_list[0][0])

        for group in self.__groups_list:
            if len(group) == 0:
                raise Exception("SudSchema init group is zero len")
            if len(group[0]) == 0:
                raise Exception("SudSchema init group[0] is zero len")
            if len(group) != self.__height:
                raise Exception("SudSchema init all groups must have one height")
            for row in group:
                if len(row) != self.__width:
                    raise Exception("SudSchema init all groups must have one width")

    def __init__(self):
        self.__groups_list: list[list[list[int]]] = [
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [2, 2, 2, 2, 2, 2, 2, 2, 2],
                [3, 3, 3, 3, 3, 3, 3, 3, 3],
                [4, 4, 4, 4, 4, 4, 4, 4, 4],
                [5, 5, 5, 5, 5, 5, 5, 5, 5],
                [6, 6, 6, 6, 6, 6, 6, 6, 6],
                [7, 7, 7, 7, 7, 7, 7, 7, 7],
                [8, 8, 8, 8, 8, 8, 8, 8, 8],
                [9, 9, 9, 9, 9, 9, 9, 9, 9]
            ],
            [
                [10, 11, 12, 13, 14, 15, 16, 17, 18],
                [10, 11, 12, 13, 14, 15, 16, 17, 18],
                [10, 11, 12, 13, 14, 15, 16, 17, 18],
                [10, 11, 12, 13, 14, 15, 16, 17, 18],
                [10, 11, 12, 13, 14, 15, 16, 17, 18],
                [10, 11, 12, 13, 14, 15, 16, 17, 18],
                [10, 11, 12, 13, 14, 15, 16, 17, 18],
                [10, 11, 12, 13, 14, 15, 16, 17, 18],
                [10, 11, 12, 13, 14, 15, 16, 17, 18]
            ],
            [
                [19, 19, 19, 20, 20, 20, 21, 21, 21],
                [19, 19, 19, 20, 20, 20, 21, 21, 21],
                [19, 19, 19, 20, 20, 20, 21, 21, 21],
                [22, 22, 22, 23, 23, 23, 24, 24, 24],
                [22, 22, 22, 23, 23, 23, 24, 24, 24],
                [22, 22, 22, 23, 23, 23, 24, 24, 24],
                [25, 25, 25, 26, 26, 26, 27, 27, 27],
                [25, 25, 25, 26, 26, 26, 27, 27, 27],
                [25, 25, 25, 26, 26, 26, 27, 27, 27]
            ]
        ]

        self.__height: int
        self.__width: int

        self.test_groups()

    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width

    @property
    def groups_list(self) -> list[list[list[int]]]:
        return self.__groups_list

    # file_schemas_name: str = "./assets/schemas/standard.json"
    # with open("data_file.json", "w") as write_file:
    #     json.dump(data, write_file)

    # with open("data_file.json", "r") as read_file:
    #     data = json.load(read_file)
