from .day_06 import solve_1, solve_2

test_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


def test_solve_1():
    assert solve_1(test_input, True) == 4277556


def test_solve_2():
    assert solve_2(test_input, True) == 0
