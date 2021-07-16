from solve.sudCell import SudCell
from solve.sudMatrix import SudMatrix


def main():
    # start_state: list[str] = [
    #     "   4  7  ",
    #     "8 7  6   ",
    #     " 62    18",
    #     "   3 189 ",
    #     "3  6   47",
    #     " 2   8   ",
    #     "9 8 63154",
    #     "243 7568 ",
    #     " 1  94   "
    # ]

    # start_state: list[str] = [
    #     "",
    #     "",
    #     "",
    #     "",
    #     "",
    #     "",
    #     "",
    #     "",
    #     ""
    # ]

    # start_state: list[str] = [
    #     "  9   4 2",
    #     "   3 4 69",
    #     " 54 96   ",
    #     "       7 ",
    #     "17     2 ",
    #     "   127695",
    #     " 2 5 9  7",
    #     "  178 94 ",
    #     "  7  3   "
    # ]

    start_state: list[str] = [
        "98 6   31",
        "  7      ",
        "6  54    ",
        "     8374",
        "    6    ",
        "      9 2",
        " 32  74  ",
        " 4 3   1 ",
        "         "
    ]

    test_matrix = SudMatrix()
    test_matrix.set_start_state(start_state)

    # while not test_matrix.solved():
    #     while test_matrix.next_simple_turn():
    #         print("turn simple")
    #     if not test_matrix.next_hard_turn():
    #         break

    while test_matrix.next_hard_turn():
        test_matrix.print_compact()

    test_matrix.set_digit(1, 2, 1)
    test_matrix.print_compact()

    while test_matrix.next_hard_turn():
        test_matrix.print_compact()


# print(test_matrix)


if __name__ == '__main__':
    main()
