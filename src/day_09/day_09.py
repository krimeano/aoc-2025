neighbours_shifts = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


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
    corners: list[tuple[int, int]] = []

    for line in text_input.splitlines():
        if not line:
            continue
        x, y = [int(z) for z in line.split(',')]
        corners.append((x, y))
        print(x, y)

    uu, xx = unzipped_coord_indexes([xy[0] for xy in corners])
    vv, yy = unzipped_coord_indexes([xy[1] for xy in corners])
    x_to_u = dict(zip(xx, uu))
    u_to_x = dict(zip(vv, xx))
    y_to_v = dict(zip(yy, vv))
    v_to_y = dict(zip(vv, yy))

    print(u_to_x)
    print(v_to_y)
    squeezed_corners = [(x_to_u[x], y_to_v[y]) for x, y in corners]
    print(corners)
    print(squeezed_corners)
    tiles = [['.' for __ in range(max(uu) + 2)] for _ in range(max(vv) + 2)]

    s, t = squeezed_corners[0]
    tiles[t][s] = '#'
    min_y_corners = []

    for u, v in squeezed_corners[1:] + squeezed_corners[:1]:
        if v == 1:
            min_y_corners.append((u, v))
        tiles[v][u] = '#'
        dx = get_step(s, u)
        dy = get_step(t, v)
        x = s + dx
        y = t + dy

        print((s, t), (x, y), (dx, dy), (u, v))

        while x != u or y != v:
            tiles[y][x] = 'X'
            x = x + dx
            y = y + dy

        s, t = u, v
    print(min_y_corners)
    x, y = (min_y_corners[0][0] + min_y_corners[1][0]) // 2, 2
    tiles[y][x] = 'Y'
    wave = [(x, y)]
    while wave:
        print(wave)
        x0, y0 = wave.pop(0)
        for dx, dy in neighbours_shifts:
            x, y = x0 + dx, y0 + dy
            if tiles[y][x] != '.':
                continue
            tiles[y][x] = 'Y'
            wave.append((x, y))
    print_tiles(tiles)
    return 0


def unzipped_coord_indexes(values: list[int]) -> tuple[list[int], list[int]]:
    ix = -1
    prev_v = -1

    vv = sorted(set(values))
    kk = []
    for v in vv:
        ix += 1
        if v - prev_v > 1:
            ix += 1
        kk.append(ix)
        prev_v = v
    return kk, vv


def get_step(x_from: int, x_to: int) -> int:
    if x_to < x_from:
        return -1
    if x_to > x_from:
        return 1
    return 0


def print_tiles(tiles: list[list[str]]):
    for row in tiles:
        print(''.join(row))

    print('GOING TO WRITE TO FILE')
    with open('./out_09.txt', 'w') as g:
        print('WRITING TO FILE')
        g.writelines([''.join(row) + '\n' for row in tiles])


if __name__ == '__main__':
    print('Day 09')

    with open('../../input/09.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents))
