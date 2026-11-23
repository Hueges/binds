from collections.abc import Callable

from binds import Functor


class Box[T](Functor[T]):

    def __init__(self, value: T) -> None:
        self.value = value

    def map[U](self, fn: Callable[[T], U]):
        return Box(fn(self.value))




def test_functor_identity():
    box = Box(5)

    result = box.map(lambda x: x)

    assert result.value == box.value
    assert isinstance(result, Box)


def test_functor_composition():
    box = Box(5)

    f = lambda x: x+2
    g = lambda x: x*3

    left = box.map(lambda x: g(f(x)))
    right = box.map(f).map(g)

    assert left.value == right.value