from .day_04 import solve_1, solve_2

test_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def test_solve_1():
    assert solve_1(test_input, True) == 13


def test_solve_2():
    assert solve_2(test_input, True) == 43
