from .solution import solve

test_input = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def test_solve():
    assert solve(test_input, True) == 3
