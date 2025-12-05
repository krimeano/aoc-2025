def solve_1(text_input: str, debug=False) -> int:
    debug and print()
    lines = text_input.splitlines()
    mode = 'ranges'
    ranges: list[tuple[int, int]] = []
    result = 0
    for line in lines:
        if not line:
            mode = 'ids'
            continue

        debug and print(mode, line)

        if mode == 'ranges':
            az = [int(x.strip()) for x in line.split('-') if x]
            ranges.append((az[0], az[1]))
            continue

        x = int(line.strip())

        fresh = False

        for (a, z) in ranges:
            if a <= x <= z:
                fresh = True
                break

        result += fresh

    return result


def solve_2(text_input: str, debug=False) -> int:
    debug and print()
    return 0


if __name__ == '__main__':
    print('Day 05')

    with open('../../input/05.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents))
