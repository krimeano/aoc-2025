def solve_1(text_input: str, debug=False, part_2=False) -> int:
    debug and print()

    lines = text_input.splitlines()
    height = len(lines)

    if not height:
        return 0

    width = height and len(lines[0])

    result = 0
    ignited: dict[tuple[int, int], int] = {}
    wave: list[tuple[int, int, str]] = []

    def radiate(kx, ly, density=1) -> int:
        if not (kx < height and 0 <= ly < width):
            return 0
        cell = lines[kx][ly]

        if cell == '^':
            radiate(kx, ly - 1, density)
            radiate(kx, ly + 1, density)
            return 1

        if (kx, ly) in ignited:
            ignited[(kx, ly)] += density

        else:
            ignited[(kx, ly)] = density
            wave.append((kx, ly, cell))

        return 0

    for jy in range(width):
        if lines[0][jy] == 'S':
            radiate(0, jy, 1)

    while wave:
        ix, jy, quant = wave.pop(0)
        result += radiate(ix + 1, jy, ignited[(ix, jy)])

    if debug:
        for ix in range(height):
            for jy in range(width):
                if lines[ix][jy] == '.':
                    print((ix, jy) in ignited and '|' or '.', end='')
                else:
                    print(lines[ix][jy], end='')
            print()

    debug and print(ignited)

    if part_2:
        result = 0
        ix = height - 1
        for jy in range(width):
            if (ix, jy) in ignited:
                result += ignited[(ix, jy)]

    return result


def solve_2(text_input: str, debug=False) -> int:
    return solve_1(text_input, debug, True)


if __name__ == '__main__':
    print('Day 07')

    with open('../../input/07.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents))
