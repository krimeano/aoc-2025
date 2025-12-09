def solve_1(text_input: str, debug=False) -> int:
    debug and print()
    tiles = [tuple([int(y) for y in x.split(',')]) for x in text_input.splitlines() if x]
    size = len(tiles)
    result = 0
    for ix in range(size - 1):
        for iy in range(ix + 1, size):
            x = tiles[ix]
            y = tiles[iy]
            current = (abs(x[0] - y[0]) + 1) * (abs(x[1] - y[1]) + 1)
            if current > result:
                result = current
    return result


def solve_2(text_input: str, debug=False) -> int:
    debug and print()
    return 0


if __name__ == '__main__':
    print('Day 09')

    with open('../../input/09.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents))
