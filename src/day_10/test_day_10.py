from .day_10 import solve_1, solve_2, parse_button, parse_lights

test_input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""


def test_parse_lights():
    assert parse_lights('[#]') == 1
    assert parse_lights('[.]') == 0
    assert parse_lights('[.#]') == 2
    assert parse_lights('[#.]') == 1
    assert parse_lights('###') == 7
    assert parse_lights('.##') == 6
    assert parse_lights('#.#.#.#') == 85


def test_parse_button():
    assert parse_button('(0)') == 1
    assert parse_button('(1)') == 2
    assert parse_button('2') == 4
    assert parse_button('0,1') == 3
    assert parse_button('(0,2)') == 5
    assert parse_button('(0,1,2)') == 7
    assert parse_button('(1,5,6,7,8)') == 482


def test_solve_1():
    assert solve_1("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}", False) == 2
    assert solve_1("[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}", False) == 3
    assert solve_1("[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}", False) == 2
    assert solve_1(test_input, False) == 7


def test_solve_2():
    assert solve_2("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}", True) == 10
    assert solve_2("[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}", True) == 12
    assert solve_2("[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}", True) == 11
    assert solve_2(test_input, True) == 33
