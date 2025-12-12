from math import inf


def solve_1(text_input: str, debug=False) -> int:
    debug and print()
    result = 0

    for line in text_input.splitlines():
        if not line:
            continue
        lights, buttons, tail = parse_line(line)
        result += push_buttons(lights, buttons, debug=debug)

    return result


def parse_line(line: str, debug=False) -> tuple[int, list[int], list[int]]:
    parts = line.split()
    debug and print(parts)
    lights = parse_lights(parts.pop(0))
    tail = parse_tail(parts.pop())
    buttons = [parse_button(x) for x in parts]
    debug and print(lights, buttons, tail)
    return lights, buttons, tail


def parse_lights(lights: str) -> int:
    if lights.startswith('['):
        lights = lights[1:-1]
    out = 0
    for char in lights[::-1]:
        out = (out << 1) + (char == '#')
    return out


def parse_button(button: str) -> int:
    if button.startswith('('):
        button = button[1:-1]
    out = 0
    for x in button.split(','):
        out += 2 ** int(x)
    return out


def parse_tail(tail: str) -> list[int]:
    if tail.startswith('{'):
        tail = tail[1:-1]
    return [int(x) for x in tail.split(',')]


def push_buttons(lights: int, buttons: list[int], debug=False) -> int:
    debug and print(lights, buttons)

    visited_states = {lights}
    new_states = [lights]
    pushes = 0

    while new_states:
        states = new_states
        new_states = []

        pushes += 1

        while states:
            state = states.pop()

            for button in buttons:
                new_state = state ^ button

                if not new_state:
                    return pushes

                if new_state not in visited_states:
                    visited_states.add(new_state)
                    new_states.append(new_state)

    return -1


def solve_2(text_input: str, debug=False) -> int:
    debug and print()
    result = 0

    for line in text_input.splitlines():
        if not line:
            continue
        parts = line.split(' ')
        parts.pop(0)
        target_levels = parse_tail(parts.pop())
        buttons = [tuple([int(y) for y in x[1:-1].split(',')]) for x in parts]
        width = len(buttons)
        height = len(target_levels)
        debug and print(height, buttons, target_levels)
        matrix = [[ix in buttons[jy] and 1 or 0 for jy in range(width)] + [target_levels[ix]] for ix in range(height)]
        make_matrix_triangle(matrix)
    return result


def make_matrix_triangle(matrix0: list[list[int]]) -> list[list[int]]:
    print('make_matrix_triangle')
    height = len(matrix0)
    if not height:
        return []
    width = len(matrix0[0])
    if not width:
        return []

    matrix = [[y for y in x] for x in matrix0]

    if height == 1 or width == 1:
        print('vector', matrix[0])
        return matrix

    print_matrix(matrix)
    matrix = move_smallest_column(matrix)
    print_matrix(matrix)

    processed = height

    while processed:
        processed = 0

        matrix.sort(key=lambda xx: abs(xx[0]))
        matrix.sort(key=lambda xx: xx[0] == 0)
        print_matrix(matrix)

        first_row = matrix[0]
        a = first_row[0]

        if not a:
            raise 'DIVISION TO ZERO'

        for ix in range(1, height):
            b = matrix[ix][0]
            if not b:
                break
            processed += 1
            n = b // a
            for jy in range(width):
                matrix[ix][jy] = matrix[ix][jy] - n * first_row[jy]
    print_matrix(matrix)
    sub_matrix = make_matrix_triangle([[y for y in x[1:]] for x in matrix[1:]])
    return []


def print_matrix(matrix: list[list[int]]) -> None:
    width = len(matrix[0])
    print('-' * width * 3)
    for ix in range(len(matrix)):
        print(matrix[ix])
    print('-' * width * 3)


def move_smallest_column(matrix: list[list[int]]) -> list[list[int]]:
    width = len(matrix[0])
    height = len(matrix)

    min_ix = -1
    min_value = height
    min_total = inf

    for ix in range(width - 1):
        value = sum([matrix[jy][ix] != 0 for jy in range(height)])
        total = sum([abs(matrix[jy][ix]) for jy in range(height)])
        if 0 < value < min_value or (value == min_value and total < min_total):
            min_value = value
            min_ix = ix

    if min_ix < 1:
        return matrix

    return [[row[min_ix]] + row[:min_ix] + row[min_ix + 1:] for row in matrix]


if __name__ == '__main__':
    print('Day 10')

    with open('../../input/10.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents, True))
