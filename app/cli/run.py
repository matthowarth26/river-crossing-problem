import argparse
from typing import Iterable

from app.solver.state import State, Side
from app.solver.bfs import bfs
from app.solver.dfs import dfs
from app.solver.solution import format_path, path_is_valid


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="farmer-lion-goat-grass",
        description="Solve the classic river crossing puzzle using BFS or DFS.",
    )
    p.add_argument(
        "--method",
        choices=["bfs", "dfs"],
        default="bfs",
        help="Search method to use (default: bfs).",
    )
    p.add_argument(
        "--max-steps",
        type=int,
        default=10_000,
        help="Safety cap on explored nodes (default: 10000).",
    )
    p.add_argument(
        "--show-states",
        action="store_true",
        help="Print each state in the solution path.",
    )
    return p


def main(argv: Iterable[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    start = State(
        farmer=Side.LEFT,
        lion=Side.LEFT,
        goat=Side.LEFT,
        grass=Side.LEFT,
    )
    goal = State(
        farmer=Side.RIGHT,
        lion=Side.RIGHT,
        goat=Side.RIGHT,
        grass=Side.RIGHT,
    )

    if args.method == "bfs":
        path = bfs(start, goal, max_expansions=args.max_steps)
    else:
        path = dfs(start, goal, max_expansions=args.max_steps)

    if path is None:
        print(f"No solution found with {args.method.upper()} within {args.max_steps} expansions.")
        return 2

    # Defensive check (also shows off correctness in a portfolio repo)
    if not path_is_valid(path, start=start, goal=goal):
        print("Internal error: produced an invalid solution path.")
        return 3

    print(f"Method: {args.method.upper()}")
    print(f"Moves: {len(path) - 1}")
    if args.show_states:
        print(format_path(path))
    else:
        print("Run with --show-states to display the full state-by-state solution.")

    return 0
