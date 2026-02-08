from __future__ import annotations

from collections import deque
from typing import Optional

from app.solver.rules import is_valid
from app.solver.solution import reconstruct_path
from app.solver.state import State


def bfs(start: State, goal: State, *, max_expansions: int = 10_000) -> Optional[list[State]]:
    """Breadth-first search (guarantees shortest solution in number of moves)."""
    if not is_valid(start) or not is_valid(goal):
        return None

    q = deque([start])
    parent: dict[State, State | None] = {start: None}
    expansions = 0

    while q:
        cur = q.popleft()
        if cur == goal:
            return reconstruct_path(parent, cur)

        expansions += 1
        if expansions > max_expansions:
            return None

        for nxt in cur.successors():
            if nxt in parent:
                continue
            if not is_valid(nxt):
                continue
            parent[nxt] = cur
            q.append(nxt)

    return None
