from sudocu_solution.data.DatCell import DatCell
from sudocu_solution.data.DatGroup import DatGroup
from sudocu_solution.data.DatMatrix import DatMatrix
from sudocu_solution.data.DatTurn import DatTurn
from sudocu_solution.schema.SudSchema import SudSchema


class MatrixLoader:
    @staticmethod
    def instance_matrix(schema: SudSchema) -> DatMatrix:
        cell_matrix: list[list[DatCell]] = [
            [DatCell(x, y, set(), set(), list(), 0) for x in range(schema.width)]
            for y in range(schema.height)]

        cell_list: list[DatCell] = [item for sublist in cell_matrix for item in sublist]

        cell_groups: list[DatGroup] = [DatGroup(list()) for _ in range(schema.groups_quantity)]
        for x in range(schema.width):
            for y in range(schema.height):
                for group in schema.group[y][x]:
                    cell_groups[group - 1].group.append(cell_matrix[y][x])

        group_len: int = len(cell_groups[0].group)

        for datGroup in cell_groups:
            if len(datGroup.group) != group_len:
                raise Exception(f'All group must be one length 1 group -> {group_len} that group {len(datGroup.group)}')

        for cell in cell_list:
            cell.can_be = set(x for x in range(1, group_len + 1))

            cell_in_group: list[int] = list()
            for ind in range(len(cell_groups)):
                if cell in cell_groups[ind].group:
                    cell_in_group.append(ind)

            cell.groups = cell_in_group

        turns: list[DatTurn] = list()

        return DatMatrix(cell_matrix, cell_list, cell_groups, group_len, schema.width, schema.height, turns)
