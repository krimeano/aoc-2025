shifts = (-1, 0, 1)


def solve_1(text_input: str, debug=False) -> int:
    debug and print()
    lines = [x.strip() for x in text_input.split('\n') if x]
    size = len(lines)
    result = 0
    for ix in range(size):
        for jy in range(size):
            x = lines[ix][jy]
            if x == '.':
                debug and print(x, end='')
                continue
            neighbours = 0
            for kx in shifts:
                for ly in shifts:
                    mx = ix + kx
                    ny = jy + ly
                    if mx == ix and ny == jy:
                        continue
                    if not (0 <= mx < size and 0 <= ny < size):
                        continue
                    neighbours += lines[mx][ny] != '.'
            if neighbours < 4:
                x = 'x'
                result += 1
            debug and print(x, end='')
        debug and print()
    return result


def solve_2(text_input: str, debug=False) -> int:
    return 0


if __name__ == '__main__':
    print('Day 04')

    with open('../../input/04.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents, True))

    print('2:')
    print(solve_2(file_contents))
