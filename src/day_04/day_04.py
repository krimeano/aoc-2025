shifts = (-1, 0, 1)
too_many = 4


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
            for mx, ny in get_neighbours_indexes(ix, jy, size):
                neighbours += lines[mx][ny] != '.'
            if neighbours < too_many:
                x = 'x'
                result += 1
            debug and print(x, end='')
        debug and print()
    return result


def solve_2(text_input: str, debug=False) -> int:
    debug and print()
    lines = [x.strip() for x in text_input.split('\n') if x]
    size = len(lines)

    neighbour_cells = [[get_neighbours_indexes(ix, jy, size) for jy in range(size)] for ix in range(size)]
    to_remove = set()
    removed = set()
    current = (-1, -1)

    def calculate_neighbours(ix: int, jy: int) -> int:
        return sum([lines[mx][ny] != '.' and (mx, ny) not in removed for mx, ny in neighbour_cells[ix][jy]])

    def print_result():
        for ix in range(size):
            for jy in range(size):
                if (ix, jy) == current:
                    x = 'o'
                elif (ix, jy) in removed:
                    x = 'x'
                elif (ix, jy) in to_remove:
                    x = '?'
                else:
                    x = lines[ix][jy]
                debug and print(x, end='')
            debug and print()

    for ix in range(size):
        for jy in range(size):
            x = lines[ix][jy]
            if x == '.':
                continue
            if calculate_neighbours(ix, jy) < 4:
                to_remove.add((ix, jy))

    while to_remove:
        current = next(iter(to_remove))
        debug and print()
        debug and print('  removed =', sorted(removed))
        debug and print('to_remove =', sorted(to_remove))
        debug and print('  current =', current)
        removed.add(current)
        to_remove.remove(current)

        for ix, jy in neighbour_cells[current[0]][current[1]]:
            if lines[ix][jy] == '.' or (ix, jy) in removed:
                continue
            if calculate_neighbours(ix, jy) < too_many:
                to_remove.add((ix, jy))

    debug and print_result()
    return len(removed)


def get_neighbours_indexes(ix: int, jy: int, size: int) -> list[tuple[int, int]]:
    out = []
    for kx in shifts:
        for ly in shifts:
            if not kx and not ly:
                continue
            mx = ix + kx
            ny = jy + ly
            if 0 <= mx < size and 0 <= ny < size:
                out.append((mx, ny))
    return out


if __name__ == '__main__':
    print('Day 04')

    with open('../../input/04.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents))
