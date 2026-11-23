from collections.abc import Callable

from binds import Applicative


class Box[T](Applicative[T]):

    def __init__(self, value: T) -> None:
        self.value = value

    @classmethod
    def pure[U](cls, value: U) -> 'Box[U]':
        return cls(value)

    def apply[U, V](self: 'Box[Callable[[U], V]]', value: 'Box[U]') -> 'Box[V]':
        return Box(self.value(value.value))

    def map[U](self, fn: Callable[[T], U]) -> 'Box[U]':
        return Box(fn(self.value))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Box):
            return NotImplemented
        return self.value == other.value


def test_applicative_identity():
    v = Box(5)
    left = Box.pure(lambda x: x).apply(v)
    assert left == v


def test_applicative_homomorphism():
    f = lambda x: x + 10
    x = 5

    left = Box.pure(f).apply(Box.pure(x))
    right = Box.pure(f(x))

    assert left == right


def test_applicative_interchange():
    u = Box(lambda x: x + 10)
    y = 5

    left = u.apply(Box.pure(y))
    right = Box.pure(lambda f: f(y)).apply(u)

    assert left == right


def test_applicative_composition():
    u = Box(lambda x: x + 10)
    v = Box(lambda x: x * 2)
    w = Box(10)

    compose = lambda f: lambda g: lambda x: f(g(x))

    left = Box.pure(compose).apply(u).apply(v).apply(w)
    right = u.apply(v.apply(w))

    assert left == right
