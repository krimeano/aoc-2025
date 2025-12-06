def solve_1(text_input: str, debug=False) -> int:
    debug and print()

    result = 0
    matrix = [[y.strip() for y in x.split()] for x in text_input.splitlines()]
    operations = matrix.pop()

    for ix in range(len(operations)):
        op = operations[ix]
        value = op == '*' and 1 or 0

        for row in matrix:
            current = int(row[ix])
            if op == '*':
                value *= current
            else:
                value += current

        result += value

    return result


def solve_2(text_input: str, debug=False) -> int:
    debug and print()
    result = 0
    lines = text_input.splitlines()
    operations = lines.pop()

    op = ''
    value = 0
    for ix in range(len(operations)):
        if operations[ix] != ' ':
            op = operations[ix]
            value = op == '*' and 1 or 0

        current = 0

        for line in lines:
            if line[ix] != ' ':
                current = current * 10 + int(line[ix])

        if current:
            if op == '*':
                value *= current
            else:
                value += current
        else:
            result += value

    else:
        result += value

    return result


if __name__ == '__main__':
    print('Day 06')

    with open('../../input/06.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents))
