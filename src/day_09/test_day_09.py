from .day_09 import solve_1, solve_2, unzipped_coord_indexes

test_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


def test_unzipped_coord_indexes():
    assert unzipped_coord_indexes([10, 5, 20, 11, 15, 19]) == ([1, 3, 4, 6, 8, 9], [5, 10, 11, 15, 19, 20])


def test_solve_1():
    assert solve_1(test_input, True) == 50


def test_solve_2():
    assert solve_2(test_input, True) == 24
