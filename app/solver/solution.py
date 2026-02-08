from __future__ import annotations

from typing import Sequence

from app.solver.state import Side, State
from app.solver.rules import is_valid


def reconstruct_path(parent: dict[State, State | None], goal: State) -> list[State]:
    path: list[State] = []
    cur: State | None = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path


_ENTITY_ORDER: list[tuple[str, str]] = [
    ("Farmer", "farmer"),
    ("Lion", "lion"),
    ("Goat", "goat"),
    ("Grass", "grass"),
]


def _format_side(state: State, side: Side) -> str:
    names = [label for (label, attr) in _ENTITY_ORDER if getattr(state, attr) == side]
    return ", ".join(names) if names else "None"


def format_path(path: Sequence[State]) -> str:
    """Format a solution path in the classic 'Starting side / Target side' style.

    This mirrors the output many instructors expect for the river crossing puzzle.
    """
    lines: list[str] = []
    for i, state in enumerate(path, start=1):
        lines.append(f"Step {i}:")
        lines.append(f"Starting side: {_format_side(state, Side.LEFT)}")
        lines.append(f"Target side: {_format_side(state, Side.RIGHT)}")
        lines.append("")  # blank line between steps
    return "\n".join(lines).rstrip()


def path_is_valid(path: Sequence[State], *, start: State, goal: State) -> bool:
    if not path:
        return False
    if path[0] != start:
        return False
    if path[-1] != goal:
        return False
    for s in path:
        if not is_valid(s):
            return False
    # Ensure each step is a legal successor
    for a, b in zip(path, path[1:]):
        if b not in set(a.successors()):
            return False
    return True
