from .day_12 import solve_1, solve_2

test_input = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""


def test_solve_1():
    assert solve_1(test_input, True) == 2


def test_solve_2():
    assert solve_2(test_input, True) == 0
