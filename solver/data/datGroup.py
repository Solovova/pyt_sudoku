from dataclasses import dataclass
from solver.data.datCell import DatCell


@dataclass
class DatGroup:
    group: list[DatCell]
