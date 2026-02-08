from app.solver.bfs import bfs
from app.solver.solution import path_is_valid
from app.solver.state import Side, State


def test_bfs_finds_shortest_solution():
    start = State(Side.LEFT, Side.LEFT, Side.LEFT, Side.LEFT)
    goal = State(Side.RIGHT, Side.RIGHT, Side.RIGHT, Side.RIGHT)

    path = bfs(start, goal, max_expansions=10_000)
    assert path is not None
    assert path_is_valid(path, start=start, goal=goal)

    # Classic puzzle shortest solution is 7 moves (8 states)
    assert len(path) - 1 == 7
