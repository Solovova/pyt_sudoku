from dataclasses import dataclass
from sudocu_solution.data.mDatCell import DatCell


@dataclass
class DatGroup:
    group: list[DatCell]
