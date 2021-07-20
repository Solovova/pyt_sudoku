from dataclasses import dataclass


@dataclass
class DatCell:
    x: int
    y: int
    can_be: set[int]
    not_can_be: set[int]
    groups: list[int]
    digit: int

