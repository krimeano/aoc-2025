def solve_1(text_input: str, debug=False, connections=1000) -> int:
    debug and print()
    boxes = [[int(y) for y in x.split(',')] for x in text_input.splitlines() if x]
    size = len(boxes)
    junctions: list[tuple[int, int, int]] = []

    for ix in range(size - 1):
        debug and print(boxes[ix])

        for jy in range(ix + 1, size):
            distance = sq_distance(boxes[ix], boxes[jy])
            junctions.append((distance, ix, jy))
    junctions.sort()

    boxes_in_circuits: dict[int, set[int]] = {}
    debug and print()

    for kz in range(connections):
        ix = junctions[kz][1]
        jy = junctions[kz][2]
        debug and print(junctions[kz][0], boxes[ix], boxes[jy])

        if ix not in boxes_in_circuits:
            boxes_in_circuits[ix] = set()
            boxes_in_circuits[ix].add(ix)

        if jy in boxes_in_circuits[ix]:
            debug and print('    ', 'already connected')
            continue

        boxes_in_circuits[ix].add(jy)

        if jy not in boxes_in_circuits:
            boxes_in_circuits[jy] = set()

        visited = set()
        to_visit = set()
        to_visit.add(ix)
        to_visit.add(jy)

        while to_visit:
            la = to_visit.pop()
            visited.add(la)
            for mb in boxes_in_circuits[la]:
                if mb not in visited:
                    to_visit.add(mb)

        for la in visited:
            boxes_in_circuits[la] = visited

    circuits: list[set[int]] = []

    debug and print()

    for ix in boxes_in_circuits:
        debug and print(ix, boxes_in_circuits[ix])
        if boxes_in_circuits[ix] not in circuits:
            circuits.append(boxes_in_circuits[ix])

    circuits.sort(key=lambda x: len(x), reverse=True)
    debug and print()
    result = 1

    for x in circuits[:3]:
        debug and print(x)
        result *= len(x)

    return result


def solve_2(text_input: str, debug=False) -> int:
    debug and print()
    return 0


def sq_distance(box_a: list[int], box_b: list[int]) -> int:
    size = len(box_a)
    if size != len(box_b):
        raise ValueError('box1 and box2 must have same length')
    return sum([(box_a[ix] - box_b[ix]) ** 2 for ix in range(size)])


if __name__ == '__main__':
    print('Day 08')

    with open('../../input/08.txt', 'r') as f:
        file_contents = f.read()

    print('1:')
    print(solve_1(file_contents))

    print('2:')
    print(solve_2(file_contents))
