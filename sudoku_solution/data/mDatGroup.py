from dataclasses import dataclass
from sudoku_solution.data.mDatCell import DatCell


@dataclass
class DatGroup:
    group: list[DatCell]
