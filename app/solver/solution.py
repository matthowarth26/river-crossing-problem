from __future__ import annotations

from typing import Iterable, List, Optional, Sequence

from app.solver.state import State
from app.solver.rules import is_valid


def reconstruct_path(parent: dict[State, State | None], goal: State) -> list[State]:
    path: list[State] = []
    cur: State | None = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path


def format_path(path: Sequence[State]) -> str:
    lines = []
    for i, s in enumerate(path):
        prefix = "start" if i == 0 else f"move {i:02d}"
        lines.append(f"{prefix}: {s}")
    return "\n".join(lines)


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
