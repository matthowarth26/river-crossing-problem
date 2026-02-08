from __future__ import annotations

from typing import Optional

from app.solver.rules import is_valid
from app.solver.solution import reconstruct_path
from app.solver.state import State


def dfs(start: State, goal: State, *, max_expansions: int = 10_000) -> Optional[list[State]]:
    """Depth-first search using an explicit stack.

    DFS is not guaranteed to find the shortest solution, but it can be simpler and memory-light.
    """
    if not is_valid(start) or not is_valid(goal):
        return None

    stack: list[State] = [start]
    parent: dict[State, State | None] = {start: None}
    expansions = 0

    while stack:
        cur = stack.pop()
        if cur == goal:
            return reconstruct_path(parent, cur)

        expansions += 1
        if expansions > max_expansions:
            return None

        # Push successors to stack (order affects which solution DFS finds)
        for nxt in cur.successors():
            if nxt in parent:
                continue
            if not is_valid(nxt):
                continue
            parent[nxt] = cur
            stack.append(nxt)

    return None
