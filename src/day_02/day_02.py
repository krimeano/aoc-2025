def solve_1(text_input: str, debug=False) -> int:
    debug and print()
    result = 0
    for item in get_items(text_input):
        debug and print()
        debug and print(item)
        limit_from = int(item[0])
        limit_to = int(item[1])

        size_from = len(item[0]) // 2
        prefix_from = int(item[0][:size_from] or '0')

        if len(item[0]) == len(item[1]):
            if len(item[0]) % 2:
                debug and print('    odd size, skipping')
                continue
            prefix_to = int(item[1][:size_from])
        else:
            prefix_to = int(item[1][:len(item[1]) // 2 + len(item[1]) % 2])

        debug and print(limit_from, limit_to, ' -> ', prefix_from, prefix_to)

        for x in range(prefix_from, prefix_to + 1):
            invalid_id = int(str(x) + str(x))
            debug and print('    ?', limit_from, '<=', invalid_id, '<=', limit_to)
            if limit_from <= invalid_id <= limit_to:
                debug and print('    result +=', invalid_id)
                result += invalid_id

    return result


def solve_2(text_input: str, debug=False) -> int:
    debug and print()
    return 0


def get_items(text_input: str) -> list[list[str]]:
    return [[y.strip() for y in x.split('-')] for x in ' '.join(text_input.split('\n')).split(',') if x]


if __name__ == '__main__':
    print('Day 02')

    print('1:', end=' ')

    with open('../../input/day_02.txt', 'r') as f:
        print(solve_1(f.read(), True))

    print('2:', end=' ')
    with open('../../input/day_02.txt', 'r') as f:
        print(solve_2(f.read()))
