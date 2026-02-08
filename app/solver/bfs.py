from __future__ import annotations

from collections import deque
from typing import Optional

from app.solver.rules import is_valid
from app.solver.solution import reconstruct_path
from app.solver.state import State


def _depth(parent: dict[State, State | None], node: State) -> int:
    d = 0
    while parent[node] is not None:
        node = parent[node]  # type: ignore[assignment]
        d += 1
    return d


def bfs(start: State, goal: State, *, max_expansions: int = 10_000, trace: bool = False) -> Optional[list[State]]:
    if not is_valid(start) or not is_valid(goal):
        return None

    q = deque([start])
    parent: dict[State, State | None] = {start: None}
    expansions = 0

    while q:
        cur = q.popleft()

        if trace:
            print(f"[BFS] Exploring depth {_depth(parent, cur)}")
            print(cur)

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