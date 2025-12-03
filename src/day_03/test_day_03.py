from .day_03 import solve_1, solve_2, find_largest_joltage_simple

test_input = """987654321111111
811111111111119
234234234234278
818181911112111
"""


def test_find_largest_joltage():
    assert find_largest_joltage_simple([1, 1]) == 11
    assert find_largest_joltage_simple([1, 2]) == 12
    assert find_largest_joltage_simple([2, 1]) == 21

    assert find_largest_joltage_simple([5, 4, 3]) == 54
    assert find_largest_joltage_simple([4, 5, 3]) == 53
    assert find_largest_joltage_simple([3, 4, 5]) == 45

    assert find_largest_joltage_simple([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1]) == 98
    assert find_largest_joltage_simple([8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]) == 89
    assert find_largest_joltage_simple([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8]) == 78
    assert find_largest_joltage_simple([8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1]) == 92


def test_solve_1():
    assert solve_1(test_input, True) == 357


def test_solve_2():
    assert solve_2(test_input, True) == 0
