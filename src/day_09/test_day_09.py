from .day_09 import solve_1, solve_2

test_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


def test_solve_1():
    assert solve_1(test_input, True) == 50


def test_solve_2():
    assert solve_2(test_input, True) == 0
