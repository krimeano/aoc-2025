def solve_1(text_input: str, debug=False) -> int:
    debug and print()

    result = 0
    ranges: list[tuple[int, int]] = []
    mode = 'ranges'

    for line in text_input.splitlines():
        debug and print(mode, line)

        if not line:
            if mode == 'ranges':
                ranges = merge_ranges(ranges)
                mode = 'ids'

            continue

        if mode == 'ranges':
            az = [int(x.strip()) for x in line.split('-') if x]
            ranges.append((az[0], az[1]))
            continue

        x = int(line.strip())

        for (a, z) in ranges:
            if a <= x <= z:
                result += 1
                break

    return result


def solve_2(text_input: str, debug=False) -> int:
    debug and print()
    lines = text_input.splitlines()

    ranges: list[tuple[int, int]] = []

    for line in lines:
        if not line:
            ranges = merge_ranges(ranges)
            break

        az = [int(x.strip()) for x in line.split('-') if x]
        ranges.append((az[0], az[1]))
        continue

    if debug:
        print()
        for az in ranges:
            print(az)

    return sum(z - a + 1 for (a, z) in ranges)


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    output: list[tuple[int, int]] = []

    ranges = sorted(ranges)

    a, b = ranges.pop(0)

    while ranges:
        c, d = ranges.pop(0)
        if c <= b:
            b = max(b, d)
        else:
            output.append((a, b))
            a, b = c, d
    else:
        output.append((a, b))

    return output


if __name__ == '__main__':
    print('Day 05')

    with open('../../input/05.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents))
