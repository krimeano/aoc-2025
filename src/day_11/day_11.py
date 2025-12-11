def solve_1(text_input: str, debug=False) -> int:
    debug and print()
    items = {}
    for line in text_input.splitlines():
        if not line.strip():
            continue
        item, children = line.split(': ')
        if item not in items:
            items[item] = {'parents': set(), 'children': set(), 'ways': 0}
        for child in children.split(' '):
            if child not in items:
                items[child] = {'parents': set(), 'children': set(), 'ways': 0}
            items[item]['children'].add(child)
            items[child]['parents'].add(item)

    items['you']['ways'] = 1

    children = {'you'}
    while children:
        cur = children.pop()
        for child in items[cur]['children']:
            items[child]['ways'] = 0
            for parent in items[child]['parents']:
                items[child]['ways'] += items[parent]['ways']
            children.add(child)
    return items['out']['ways']


def solve_2(text_input: str, debug=False) -> int:
    debug and print()
    items = {}

    for line in text_input.splitlines():
        if not line.strip():
            continue

        item, children = line.split(': ')
        if item not in items:
            items[item] = {'parents': set(), 'children': set(), 'ways': [0, 0, 0, 0]}
        for child in children.split(' '):
            if child not in items:
                items[child] = {'parents': set(), 'children': set(), 'ways': [0, 0, 0, 0]}
            items[item]['children'].add(child)
            items[child]['parents'].add(item)

    items['svr']['ways'] = [1, 0, 0, 0]

    if debug:
        print()
        for item in items:
            print(item, items[item])
        print()

    children = {'svr'}
    while children:
        cur = children.pop()
        for child in items[cur]['children']:
            items[child]['ways'] = [0, 0, 0, 0]
            for parent in items[child]['parents']:
                if child == 'fft':
                    items[child]['ways'][1] += items[parent]['ways'][0]
                    items[child]['ways'][3] += items[parent]['ways'][2]
                elif child == 'dac':
                    items[child]['ways'][2] += items[parent]['ways'][0]
                    items[child]['ways'][3] += items[parent]['ways'][1]
                else:
                    for ix in range(4):
                        items[child]['ways'][ix] += items[parent]['ways'][ix]
            children.add(child)

    return items['out']['ways'][3]


if __name__ == '__main__':
    print('Day 11')

    with open('../../input/11.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents))
