from app.solver.state import Side, State


def test_state_hashable_and_equatable():
    a = State(Side.LEFT, Side.RIGHT, Side.LEFT, Side.RIGHT)
    b = State(Side.LEFT, Side.RIGHT, Side.LEFT, Side.RIGHT)
    assert a == b
    assert hash(a) == hash(b)
    assert len({a, b}) == 1


def test_successors_farmer_always_moves():
    s = State(Side.LEFT, Side.LEFT, Side.LEFT, Side.LEFT)
    nxt = list(s.successors())
    assert all(t.farmer == Side.RIGHT for t in nxt)
