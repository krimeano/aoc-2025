from .day_05 import solve_1, solve_2

test_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


def test_solve_1():
    assert solve_1(test_input, True) == 3


def test_solve_2():
    assert solve_2(test_input, True) == 0
