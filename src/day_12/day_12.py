def solve_1(text_input: str, debug=False) -> int:
    debug and print()
    presents, containers = parse_input(text_input.splitlines())
    print(presents)
    print(containers)
    return 0


def solve_2(text_input: str, debug=False) -> int:
    debug and print()
    return 0


def parse_input(lines: list[str]) -> tuple[list, list]:
    mode = 'present'
    presents = []
    containers = []
    rows = []
    for line in lines:
        line = line.strip()
        if not line:
            if mode == 'present':
                mode = ''
                if rows:
                    present = tuple([tuple([x == '#' and 1 or 0 for x in row]) for row in rows])
                    presents.append(present)
                rows = []
            continue
        if line.endswith(":"):
            mode = 'present'
            continue
        if mode == 'present':
            rows.append(line)
            continue
        parts = line.split(': ')
        if len(parts) < 2:
            continue
        wh = [int(x) for x in parts.pop(0).split('x')]
        quantities = [int(x) for x in parts.pop().split(' ')]
        containers.append(((wh[0], wh[1]), quantities))
    return presents, containers


if __name__ == '__main__':
    print('Day 12')

    with open('../../input/12.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents))
