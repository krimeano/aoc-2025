from math import gcd, lcm

class Matrix:
    @staticmethod
    def transpose(xxx: list[list[int]]):
        if not len(xxx):
            return []
        return [[xx[ix] for xx in xxx] for ix in range(len(xxx[0]))]

    @staticmethod
    def to_str(xxx: list[list[int]]) -> str:
        if not len(xxx):
            return '<empty>'
        ww = [max([len(str(x)) for x in xx]) for xx in Matrix.transpose(xxx)]
        return '\n' + '\n'.join(Matrix.line_to_str(xx, ww) for xx in xxx)

    @staticmethod
    def line_to_str(xx: list[int], ww: list[int]) -> str:
        pieces = ['{{0:{0}}}'.format(ww[ix]).format(xx[ix]) for ix in range(len(xx))]
        pieces.insert(-1, '|')
        return ' '.join(pieces)

    @staticmethod
    def solve(xxx: list[list[int]]) -> list[list[int]]:
        curr_ix = 0

        while curr_ix < len(xxx) and curr_ix < len(xxx[0]) - 1:
            xxx = Matrix.sort_columns(xxx, curr_ix)

            xxx = Matrix.sort_rows(xxx, curr_ix)

            xxx = Matrix.subtract_row(xxx, curr_ix)

            xxx = Matrix.remove_empty_rows(xxx)

            xxx = Matrix.simplify_rows(xxx)

            curr_ix += 1

        xxx = Matrix.sort_columns(xxx)

        xxx = Matrix.sort_rows(xxx)

        xxx = Matrix.remove_zeros(xxx)
        return xxx

    @staticmethod
    def sort_columns(xxx: list[list[int]], start_ix=0) -> list[list[int]]:
        xxx = Matrix.transpose(xxx)
        aaa = xxx[:start_ix]
        zzz = xxx[len(xxx) - 1:]
        xxx = xxx[start_ix:len(xxx) - 1]
        xxx.sort(key=lambda xx: sum([x != 0 for x in xx]))
        return Matrix.transpose(aaa + xxx + zzz)

    @staticmethod
    def sort_rows(xxx: list[list[int]], start_ix=0) -> list[list[int]]:
        aaa = xxx[:start_ix]
        xxx = xxx[start_ix:]
        xxx.sort(key=lambda xx: sum([x != 0 for x in xx]))
        m = max([max([abs(x) for x in xx]) for xx in xxx]) + 1
        xxx.sort(key=lambda xx: [x == 0 and m or abs(x) for x in xx])
        return aaa + xxx

    @staticmethod
    def subtract_row(xxx: list[list[int]], fixed_ix=0) -> list[list[int]]:
        fixed_row = xxx[fixed_ix]
        fixed_item = fixed_row[fixed_ix]  # 6

        if not fixed_item:
            return xxx

        width = len(fixed_row)

        for ix in range(len(xxx)):
            if ix == fixed_ix:
                continue
            row = xxx[ix]
            item = row[fixed_ix]  # 10
            c = lcm(fixed_item, item)  # 30
            if not c:
                continue
            f = c // item  # 3
            g = c // fixed_item  # 5
            xxx[ix] = [row[jy] * f - fixed_row[jy] * g for jy in range(width)]
        return xxx

    @staticmethod
    def remove_empty_rows(xxx: list[list[int]]) -> list[list[int]]:
        return [xx for xx in xxx if any(xx)]

    @staticmethod
    def simplify_rows(xxx: list[list[int]]) -> list[list[int]]:
        return [Matrix.simplify_row(xx) for xx in xxx]

    @staticmethod
    def simplify_row(xx: list[int]) -> list[int]:
        sign = 1
        for x in xx:
            if x != 0:
                sign = x < 0 and -1 or 1
                break

        f = sign * gcd(*xx)
        return [x // f for x in xx] if f else xx

    @staticmethod
    def remove_zeros(xxx: list[list[int]]) -> list[list[int]]:
        curr_ix = 0
        while curr_ix < len(xxx):
            if not any(xxx[curr_ix][:curr_ix] + xxx[curr_ix][curr_ix + 1:]):
                xxx = Matrix.get_minor(xxx, curr_ix, curr_ix)
            else:
                curr_ix += 1
        return xxx

    @staticmethod
    def get_minor(xxx: list[list[int]], ix: int, jy: int) -> list[list[int]]:
        return [row[:ix] + row[ix + 1:] for row in xxx[:ix] + xxx[ix + 1:]]
