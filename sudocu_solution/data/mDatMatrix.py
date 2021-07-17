from dataclasses import dataclass

from sudocu_solution.data.mDatCell import DatCell
from sudocu_solution.data.mDatGroup import DatGroup
from sudocu_solution.data.mDatTurn import DatTurn


@dataclass
class DatMatrix:
    cell_matrix: list[list[DatCell]]
    cell_list: list[DatCell]
    cell_groups: list[DatGroup]
    group_len: int
    width: int
    height: int
    turns: list[DatTurn]
