import math


class Qn:
    p = 0
    q = 1

    def __init__(self, numerator: Qn | int, denominator: int = 1):
        if isinstance(numerator, Qn):
            pn, qn = numerator.p, numerator.q
        else:
            pn, qn = numerator, 1

        p = pn
        q = qn * denominator

        if q == 0 or q == math.inf or q == -math.inf or p == math.inf or p == -math.inf:
            raise ValueError("Invalid fraction: division by zero or infinity")

        if p == 0:
            q = 1

        gcd = math.gcd(p, q)
        p //= gcd
        q //= gcd

        if q < 0:
            p = -p
            q = -q

        self.p = p
        self.q = q

    def __add__(self, other: Qn | int) -> Qn:
        if isinstance(other, int):
            other = Qn(other)
        return Qn(self.p * other.q + other.p * self.q, self.q * other.q)

    def __sub__(self, other: Qn | int) -> Qn:
        if isinstance(other, int):
            other = Qn(other)
        return Qn(self.p * other.q - other.p * self.q, self.q * other.q)

    def __mul__(self, other: Qn | int) -> Qn:
        if isinstance(other, int):
            other = Qn(other)
        return Qn(self.p * other.p, self.q * other.q)

    def __truediv__(self, other: Qn | int) -> Qn:
        if isinstance(other, int):
            other = Qn(other)
        return Qn(self.p * other.q, self.q * other.p)

    def __floordiv__(self, other) -> int:
        if isinstance(other, int):
            other = Qn(other)
        result = self / other
        return result.p // result.q

    def __mod__(self, other) -> Qn:
        if isinstance(other, int):
            other = Qn(other)
        result = self / other
        result.p = result.p % result.q
        return result

    def __divmod__(self, other):
        if isinstance(other, int):
            other = Qn(other)
        result = self / other
        return Qn(result.p // result.q), Qn(result.p % result.q, result.q)

    def __radd__(self, other):
        return Qn(other).__add__(self)

    def __rsub__(self, other):
        return Qn(other).__sub__(self)

    def __rmul__(self, other):
        return Qn(other).__mul__(self)

    def __rtruediv__(self, other):
        return Qn(other).__truediv__(self)

    def __rfloordiv__(self, other):
        return Qn(other).__floordiv__(self)

    def __rmod__(self, other):
        return Qn(other).__mod__(self)

    def __rdivmod__(self, other):
        return Qn(other).__divmod__(self)

    def __neg__(self):
        return Qn(-self.p, self.q)

    def __pos__(self):
        return Qn(-self.p, self.q)

    def __eq__(self, other):
        if isinstance(other, int):
            other = Qn(other)
        return self.p * other.q == other.p * self.q

    def __ne__(self, other):
        if isinstance(other, int):
            other = Qn(other)
        return self.p * other.q != other.p * self.q

    def __lt__(self, other):
        if isinstance(other, int):
            other = Qn(other)
        return self.p * other.q < other.p * self.q

    def __le__(self, other):
        if isinstance(other, int):
            other = Qn(other)
        return self.p * other.q <= other.p * self.q

    def __gt__(self, other):
        if isinstance(other, int):
            other = Qn(other)
        return self.p * other.q > other.p * self.q

    def __ge__(self, other):
        if isinstance(other, int):
            other = Qn(other)
        return self.p * other.q >= other.p * self.q

    def __float__(self):
        return self.p / self.q

    def __int__(self):
        return int(float(self))

    def __abs__(self):
        return Qn(abs(self.p), abs(self.q))

    def __repr__(self):
        return f'Qn({self.p!r}, {self.q!r})'

    def __str__(self):
        if self.q == 1:
            return f'{self.p}'
        return f'{self.p}/{self.q}'

    def __format__(self, format_spec):
        return f'{str(self):{format_spec}}'

    def __bool__(self):
        return bool(self.p)


class Vr:
    def __init__(self, xx: list[int]):
        self.xx = xx
        self.size = len(xx)
        self._index = 0

    def __len__(self):
        return self.size

    def __getitem__(self, ix: int) -> int:
        return self.xx[ix]

    def __setitem__(self, ix: int, value: int):
        self.xx[ix] = value

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= self.size:
            raise StopIteration
        item = self.xx[self._index]
        self._index += 1
        return item

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Vectors must have the same length')
        return Vr([x + y for x, y in zip(self, other)])

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Vectors must have the same length')
        return Vr([x - y for x, y in zip(self, other)])

    def __mul__(self, other: int) -> Vr:
        return Vr([x * other for x in self])

    def __rmul__(self, other: int) -> Vr:
        return Vr([x * other for x in self])

    def __matmul__(self, other: Vr | list) -> int:
        if len(self) != len(other):
            raise ValueError('Vectors must have the same length')
        return sum(x * y for x, y in zip(self, other))

    def __floordiv__(self, other):
        return Vr([x // other for x in self])

    def __neg__(self):
        return -1 * self

    def __eq__(self, other):
        if isinstance(other, int):
            return all(x == other for x in self.xx)
        if len(self) != len(other):
            raise ValueError('Vectors must have the same length')
        return all(x == y for x, y in zip(self, other))

    def __ne__(self, other):
        if isinstance(other, int):
            return all(x != other for x in self.xx)
        if len(self) != len(other):
            raise ValueError('Vectors must have the same length')
        return all(x != y for x, y in zip(self, other))

    def __lt__(self, other):
        if isinstance(other, int):
            return all(x < other for x in self.xx)
        if len(self) != len(other):
            raise ValueError('Vectors must have the same length')
        return all(x < y for x, y in zip(self, other))

    def __le__(self, other):
        if isinstance(other, int):
            return all(x <= other for x in self.xx)
        if len(self) != len(other):
            raise ValueError('Vectors must have the same length')
        return all(x <= y for x, y in zip(self, other))

    def __gt__(self, other):
        if isinstance(other, int):
            return all(x > other for x in self.xx)
        if len(self) != len(other):
            raise ValueError('Vectors must have the same length')
        return all(x > y for x, y in zip(self, other))

    def __ge__(self, other):
        if isinstance(other, int):
            return all(x >= other for x in self.xx)
        if len(self) != len(other):
            raise ValueError('Vectors must have the same length')
        return all(x >= y for x, y in zip(self, other))

    def __abs__(self):
        return sum([x * x for x in self]) ** .5

    def __repr__(self):
        return f'Vr({self.xx!r})'

    def __str__(self):
        max_w = max([len(str(x)) for x in self.xx])
        return ', '.join('{{0:{0}}}'.format(max_w).format(x) for x in self.xx)

    def get_factor(self) -> int:
        return math.gcd(*self)


class Mx:
    def __init__(self, xxx: list[list[int]]):
        if not self.is_matrix(xxx):
            raise ValueError('Expected a valid matrix')
        self.xxx: list[list[int]] = xxx
        self.h = len(xxx)
        self.w = len(xxx[0]) if xxx else 0

    def __add__(self, other: Mx) -> Mx:
        if not isinstance(other, Mx):
            raise TypeError('Can only add Mx objects')
        if self.h != other.h or self.w != other.w:
            raise ValueError('Matrices must have the same dimensions')
        result_matrix = [[self.xxx[ix][jy] + other.xxx[ix][jy] for jy in range(self.w)] for ix in range(self.h)]
        return Mx(result_matrix)

    def __sub__(self, other: Mx) -> Mx:
        if not isinstance(other, Mx):
            raise TypeError('Can only add Mx objects')
        if self.h != other.h or self.w != other.w:
            raise ValueError('Matrices must have the same dimensions')
        result_matrix = [[self.xxx[ix][jy] - other.xxx[ix][jy] for jy in range(self.w)] for ix in range(self.h)]
        return Mx(result_matrix)

    def __matmul__(self, other: Mx) -> Mx:
        if isinstance(other, list):
            other = Mx(other)
        if not isinstance(other, Mx):
            raise TypeError('Can only multiply Mx objects')
        if self.w != other.h:
            raise ValueError('Matrices must have compatible dimensions for multiplication')
        result_matrix = [[Vr(self.get_row(ix)) @ Vr(other.get_col(jy)) for jy in range(other.w)] for ix in range(self.h)]
        return Mx(result_matrix)

    def __repr__(self):
        return f'Mx({self.xxx!r})'

    def __str__(self):
        max_w = max([max([len(str(element)) for element in row]) for row in self.xxx])
        return '\n' + '\n'.join(' '.join('{{0:{0}}}'.format(max_w).format(element) for element in row) for row in self.xxx)

    @staticmethod
    def is_matrix(xxx: list[list[int]]) -> bool:
        height = len(xxx)

        if not height:
            return True

        width = -1

        for xx in xxx:
            if width == -1:
                width = len(xx)

            if width != len(xx):
                return False

        return True

    def get_row(self, ix: int):
        return self.xxx[ix]

    def get_col(self, ix: int):
        return [row[ix] for row in self.xxx]


class MxE(Mx):
    def __init__(self, size: int):
        super().__init__([[(ix == jy and 1 or 0) for jy in range(size)] for ix in range(size)])


class MxZ(Mx):
    def __init__(self, size: int, width=0):
        super().__init__([[0 for __ in range(width or size)] for _ in range(size)])


class MxPij(Mx):
    def __init__(self, size: int, i: int, j: int):
        def get_value(ix: int, jy: int) -> int:
            if ix == i:
                return jy == j and 1 or 0
            if ix == j:
                return jy == i and 1 or 0

            return ix == jy and 1 or 0

        super().__init__([[get_value(ix, jy) for jy in range(size)] for ix in range(size)])


class MxEplusEij(Mx):
    def __init__(self, size: int, i: int, j: int, c: int):
        def get_value(ix: int, jy: int) -> int:
            if ix == i and jy == j:
                return c
            return ix == jy and 1 or 0

        super().__init__([[get_value(ix, jy) for jy in range(size)] for ix in range(size)])


# System of linear equations
class Sole(Mx):
    def __init__(self, xxx: list[list[int]], a: list[int] | None = None):
        if a:
            if len(xxx) != len(a):
                raise ValueError('Length of xxx and a must be equal')
            xxx = [[x for x in xxx[ix]] + [a[ix]] for ix in range(len(xxx))]
        super().__init__(xxx)

    def __repr__(self):
        return f'Repr({self.xxx!r})'

    def __str__(self):
        max_w = max([max([len(str(x)) for x in xx]) for xx in self.xxx])
        return '\n' + '\n'.join(' '.join('{{0:{0}}}'.format(max_w).format(x) for x in xx[:-1]) + ' | ' + '{{0:{0}}}'.format(max_w).format(xx[-1]) for xx in self.xxx)


if __name__ == '__main__':
    m = Sole([[1, 1, 0, 0, 0, 0, 3],
              [1, 0, 1, 0, 0, 0, 5],
              [0, 1, 0, 1, 1, 0, 4],
              [0, 0, 1, 1, 0, 1, 7]])
    print(m)
