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
        buttons.sort()
        buttons.sort(key=lambda x: len(x))
        width = len(buttons)
        height = len(target_levels)
        debug and print(height, buttons, target_levels)
        matrix = [[ix in buttons[jy] and 1 or 0 for jy in range(width)] + [target_levels[ix]] for ix in range(height)]
        triangle, fixed = make_matrix_triangle(matrix)
        # print_matrix(triangle)
        reduced = reduce_matrix(triangle, fixed)
        print(fixed)
        print_matrix(reduced)
    return result


def make_matrix_triangle(matrix0: list[list[int]], fixed: tuple[int, ...] = ()) -> tuple[list[list[int]], tuple[int, ...]]:
    # print('make_matrix_triangle')
    # print_matrix(matrix0)
    height = len(matrix0)
    fix_col = len(fixed)
    skipped_cols = len([ix for ix in fixed if ix == -1])

    if not height - fix_col + skipped_cols:
        # we still want to sort horizontal vector
        return matrix0, fixed

    width = len(matrix0[0])

    if width - fix_col < 2:
        # 0 - empty matrix
        # 1 - vertical vector
        return matrix0, fixed

    # look for not empty smallest item in vertical
    columns_rotated = 0
    row_indexes = find_not_empty_rows_for_fix_col(matrix0, fixed)

    if not row_indexes:
        return make_matrix_triangle(matrix0, tuple([x for x in fixed] + [-1]))

    matrix = [[y for y in x] for x in matrix0]

    while len(row_indexes) > 1:
        ix0 = row_indexes.pop(0)
        smallest_row = matrix[ix0]
        a = smallest_row[fix_col]

        for ix in row_indexes:
            row = matrix[ix]
            b = row[fix_col]
            n = b // a

            for jy in range(fix_col, width):
                row[jy] -= n * smallest_row[jy]
        row_indexes = find_not_empty_rows_for_fix_col(matrix, fixed)

    fix_row = row_indexes.pop(0)

    matrix, fixed = make_matrix_triangle(matrix, tuple([x for x in fixed] + [fix_row]))

    return matrix, fixed


def reduce_matrix(matrix: list[list[int]], fixed: tuple[int, ...]) -> list[list[int]]:
    width = len(matrix) and len(matrix[0])
    for jy0 in range(len(fixed) - 1, -1, -1):
        ix0 = fixed[jy0]

        if ix0 == -1:
            continue

        current_row = matrix[ix0]
        a = current_row[jy0]

        for jy1 in range(jy0):
            ix = fixed[jy1]

            if ix == -1:
                continue

            row = matrix[ix]
            b = row[jy0]

            if not b:
                continue
            n = b // a

            for kz in range(jy0, width):
                row[kz] -= n * current_row[kz]

    return matrix


def find_not_empty_rows_for_fix_col(matrix: list[list[int]], fixed: tuple[int, ...]) -> list[int]:
    height = len(matrix)
    fix_col = len(fixed)
    out = [ix for ix in range(height) if ix not in fixed and matrix[ix][fix_col] != 0]
    out.sort(key=lambda ix: abs(matrix[ix][-1]))
    out.sort(key=lambda ix: abs(matrix[ix][fix_col]))
    # print('find_not_empty_rows_for_fix_col: ', fixed, '->', out)
    return out


def print_matrix(matrix: list[list[int]]) -> None:
    width = len(matrix[0])
    print('-' * width * 3)
    for ix in range(len(matrix)):
        print(matrix[ix])
    print('-' * width * 3)


if __name__ == '__main__':
    print('Day 10')

    with open('../../input/10.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents, True))
