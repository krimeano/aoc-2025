start = 50


def solve(text_input, debug=False):
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


if __name__ == '__main__':
    with open('../../input/day_01.txt', 'r') as f:
        print(solve(f.read()))
