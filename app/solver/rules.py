from __future__ import annotations

from app.solver.state import State


def is_valid(state: State) -> bool:
    """Check puzzle constraints.

    - Lion can't be left alone with the goat (without the farmer).
    - Goat can't be left alone with the grass (without the farmer).
    """
    # Lion eats goat if together without farmer
    if state.lion == state.goat and state.farmer != state.lion:
        return False

    # Goat eats grass if together without farmer
    if state.goat == state.grass and state.farmer != state.goat:
        return False

    return True
