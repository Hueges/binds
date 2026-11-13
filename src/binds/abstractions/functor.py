from abc import ABC, abstractmethod
from collections.abc import Callable

class Functor[T](ABC):
    @abstractmethod
    def map[U](self, fn: Callable[[T], U]) -> 'Functor[U]':
        ...

