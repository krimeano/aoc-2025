start = 50


def solve_1(text_input, debug=False):
    debug and print()
    cur = start
    result = 0
    for x in text_input.split('\n'):
        x = x.strip()
        if not x: continue
        factor = x[0] == 'R' and 1 or -1
        cur = (cur + factor * int(x[1:])) % 100
        debug and print(x, cur)
        if not cur:
            result += 1
    return result


def solve_2(text_input, debug=False):
    debug and print()
    cur = start
    last = cur
    result = 0

    for x in text_input.split('\n'):
        x = x.strip()
        if not x: continue
        factor = x[0] == 'R' and 1 or -1
        cur = cur + factor * int(x[1:])
        debug and print(x, cur)

        if cur < 0:
            while cur < 0:
                cur += 100
                result += 1

            if not last:
                result -= 1

        if not cur:
            result += 1

        while cur >= 100:
            cur -= 100
            result += 1

        last = cur

    return result


if __name__ == '__main__':
    print('Day 01')

    with open('../../input/01.txt', 'r') as f:
        file_contents = f.read()

    print(solve_1(file_contents))
    print(solve_2(file_contents))
