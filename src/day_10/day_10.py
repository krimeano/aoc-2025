def solve_1(text_input: str, debug=False) -> int:
    debug and print()
    result = 0

    for line in text_input.splitlines():
        if not line:
            continue
        lights, buttons, tail = parse_line(line)
        result += push_buttons(lights, buttons, debug=debug)

    return result


def solve_2(text_input: str, debug=False) -> int:
    debug and print()
    return 0


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


if __name__ == '__main__':
    print('Day 10')

    with open('../../input/10.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents))
