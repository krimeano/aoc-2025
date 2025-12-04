def solve_1(text_input: str, debug=False) -> int:
    debug and print()
    return 0


def solve_2(text_input: str, debug=False) -> int:
    debug and print()
    return 0


if __name__ == '__main__':
    print('Day 11')

    with open('../../input/11.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents))
