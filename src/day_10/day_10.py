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
        buttons.sort()
        buttons.sort(key=lambda x: len(x), reverse=True)
        debug and print(buttons, target_levels)
        width = len(target_levels)
        buttons_per_target = [0] * width
        for button in buttons:
            for ix in button:
                buttons_per_target[ix] += 1
        result += calculate_pushes(buttons, target_levels, buttons_per_target)

    return result


def calculate_pushes(buttons: list[tuple[int, ...]], target_levels: list[int], buttons_per_target: list[int], already_pressed=0):
    width = len(target_levels)
    height = len(buttons)

    min_target_ix = -1
    min_buttons = inf
    for ix in range(width):
        if buttons_per_target[ix]:
            if buttons_per_target[ix] < min_buttons:
                min_buttons = buttons_per_target[ix]
                min_target_ix = ix
        elif target_levels[ix]:
            # no buttons left to press to reach the target level
            return -1

    if min_buttons == inf:
        # no buttons and no targets: success
        return already_pressed

    button_ix = -1
    for jy in range(height):
        if min_target_ix in buttons[jy]:
            button_ix = jy
            break

    current_button = buttons[button_ix]
    rest_buttons = buttons[:button_ix] + buttons[button_ix + 1:]
    new_buttons_per_target = [buttons_per_target[ix] - (ix in current_button and 1 or 0) for ix in range(width)]
    min_target = inf

    for ix in current_button:
        min_target = min(min_target, target_levels[ix])

    results = []

    values = min_buttons == 1 and [min_target] or [ix for ix in range(min_target + 1)]

    for value in values:
        new_targets = [target_levels[ix] - (ix in current_button and value or 0) for ix in range(width)]
        result = calculate_pushes(rest_buttons, new_targets, new_buttons_per_target, already_pressed + value)
        if result > 0:
            results.append(result)

    return results and min(results) or -1


if __name__ == '__main__':
    print('Day 10')

    with open('../../input/10.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents, True))
