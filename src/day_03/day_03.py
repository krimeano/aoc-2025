def solve_1(text_data: str, debug=False) -> int:
    debug and print()
    result = 0
    for line in text_data.split():
        result += find_largest_joltage_simple([int(x.strip()) for x in line if x], debug)
    return result


def solve_2(text_data: str, debug=False) -> int:
    debug and print()
    return 0


def find_largest_joltage_simple(batteries: list[int], debug=True) -> int:
    debug and print('batteries', batteries, end=' -> ')
    a = 0
    b = 0
    for x in batteries:
        if b > a:
            a = b
            b = x
        if b < x:
            b = x
    debug and print(a, b)
    return a * 10 + b


if __name__ == '__main__':
    print('Day 03')

    with open('../../input/day_03.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents, False))

    print('2:')
    print(solve_2(file_contents, False))
