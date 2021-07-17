from dataclasses import dataclass

from solver.data.datCell import DatCell
from solver.data.datGroup import DatGroup
from solver.data.datTurn import DatTurn


@dataclass
class DatMatrix:
    cell_matrix: list[list[DatCell]]
    cell_list: list[DatCell]
    cell_groups: list[DatGroup]
    group_len: int
    width: int
    height: int
    turns: list[DatTurn]
