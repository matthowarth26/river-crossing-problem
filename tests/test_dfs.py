from app.solver.dfs import dfs
from app.solver.solution import path_is_valid
from app.solver.state import Side, State


def test_dfs_finds_a_valid_solution():
    start = State(Side.LEFT, Side.LEFT, Side.LEFT, Side.LEFT)
    goal = State(Side.RIGHT, Side.RIGHT, Side.RIGHT, Side.RIGHT)

    path = dfs(start, goal, max_expansions=10_000)
    assert path is not None
    assert path_is_valid(path, start=start, goal=goal)
