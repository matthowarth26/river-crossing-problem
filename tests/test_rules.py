from app.solver.rules import is_valid
from app.solver.state import Side, State


def test_valid_start_state():
    s = State(Side.LEFT, Side.LEFT, Side.LEFT, Side.LEFT)
    assert is_valid(s)


def test_invalid_lion_with_goat_without_farmer():
    # Farmer on Right, lion+goat on Left
    s = State(Side.RIGHT, Side.LEFT, Side.LEFT, Side.RIGHT)
    assert not is_valid(s)


def test_invalid_goat_with_grass_without_farmer():
    # Farmer on Right, goat+grass on Left
    s = State(Side.RIGHT, Side.RIGHT, Side.LEFT, Side.LEFT)
    assert not is_valid(s)
