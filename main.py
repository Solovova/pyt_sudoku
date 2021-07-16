from solve.sudCell import SudCell
from solve.sudMatrix import SudMatrix


def main():
    # test_sell = SudCell(0, 0)
    # test_sell.add_not_can_be(1)
    # print(test_sell)

    test_matrix = SudMatrix()
    test_matrix.set_digit(1, 1, 5)
    test_matrix.print_compact()
    # print(test_matrix)


if __name__ == '__main__':
    main()
