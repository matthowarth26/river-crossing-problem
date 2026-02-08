from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Tuple


class Side(str, Enum):
    LEFT = "L"
    RIGHT = "R"

    def other(self) -> "Side":
        return Side.RIGHT if self == Side.LEFT else Side.LEFT


@dataclass(frozen=True, slots=True)
class State:
    """Puzzle state.

    Each entity is on LEFT or RIGHT. A move consists of the farmer crossing
    (possibly carrying one passenger: lion, goat, or grass).
    """

    farmer: Side
    lion: Side
    goat: Side
    grass: Side

    def is_goal(self) -> bool:
        return (
            self.farmer == Side.RIGHT
            and self.lion == Side.RIGHT
            and self.goat == Side.RIGHT
            and self.grass == Side.RIGHT
        )

    def successors(self) -> Iterable["State"]:
        """Generate all *candidate* next states (validity checked elsewhere)."""
        # Farmer always moves.
        new_farmer = self.farmer.other()

        # Farmer crosses alone
        yield State(new_farmer, self.lion, self.goat, self.grass)

        # Farmer crosses with exactly one passenger that starts on same side
        if self.lion == self.farmer:
            yield State(new_farmer, self.lion.other(), self.goat, self.grass)
        if self.goat == self.farmer:
            yield State(new_farmer, self.lion, self.goat.other(), self.grass)
        if self.grass == self.farmer:
            yield State(new_farmer, self.lion, self.goat, self.grass.other())

    def as_tuple(self) -> Tuple[str, str, str, str]:
        return (self.farmer.value, self.lion.value, self.goat.value, self.grass.value)

    def __str__(self) -> str:
        # Nice display for CLI output / README
        def fmt(name: str, side: Side) -> str:
            return f"{name}:{side.value}"
        return " ".join(
            [fmt("F", self.farmer), fmt("L", self.lion), fmt("G", self.goat), fmt("Gr", self.grass)]
        )
