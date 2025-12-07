def solve_1(text_input: str, debug=False) -> int:
    debug and print()

    lines = text_input.splitlines()
    height = len(lines)

    if not height:
        return 0

    width = height and len(lines[0])

    ignited: set[tuple[int, int]] = set()
    wave: list[tuple[int, int, str]] = []
    result = 0

    def radiate(kx, ly) -> int:
        if kx < height and 0 <= ly < width and (kx, ly) not in ignited:
            cell = lines[kx][ly]
            ignited.add((kx, ly))
            wave.append((kx, ly, cell))
            return cell == '^'
        return 0

    for jy in range(width):
        if lines[0][jy] == 'S':
            radiate(0, jy)

    while wave:
        ix, jy, quant = wave.pop(0)

        if quant == 'S' or quant == '.':
            result += radiate(ix + 1, jy)
        elif quant == '^':
            result += radiate(ix, jy + 1)
            result += radiate(ix, jy - 1)

    if debug:
        for ix in range(height):
            for jy in range(width):
                if lines[ix][jy] == '.':
                    print((ix, jy) in ignited and '|' or '.', end='')
                else:
                    print(lines[ix][jy], end='')
            print()
    return result


def solve_2(text_input: str, debug=False) -> int:
    debug and print()
    return 0


if __name__ == '__main__':
    print('Day 07')

    with open('../../input/07.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents))
