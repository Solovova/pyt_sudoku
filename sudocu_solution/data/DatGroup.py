from dataclasses import dataclass
from sudocu_solution.data.DatCell import DatCell


@dataclass
class DatGroup:
    group: list[DatCell]
