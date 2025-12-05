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
    lines = text_input.splitlines()

    ranges: list[tuple[int, int]] = []
    result: list[tuple[int, int]] = []

    for line in lines:
        if not line:
            break

        az = [int(x.strip()) for x in line.split('-') if x]
        ranges.append((az[0], az[1]))
        continue

    ranges = sorted(ranges)

    if debug:
        print()
        for az in ranges:
            print(az)

    a, b = ranges.pop(0)

    while ranges:
        c, d = ranges.pop(0)
        if c <= b:
            b = max(b, d)
        else:
            result.append((a, b))
            a, b = c, d
    else:
        result.append((a, b))

    if debug:
        print()
        for az in result:
            print(az)

    return sum(z - a + 1 for (a, z) in result)


if __name__ == '__main__':
    print('Day 05')

    with open('../../input/05.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents))
