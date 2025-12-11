from .day_11 import solve_1, solve_2

test_input = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""


def test_solve_1():
    assert solve_1(test_input, True) == 5


def test_solve_2():
    assert solve_2(test_input, True) == 0
