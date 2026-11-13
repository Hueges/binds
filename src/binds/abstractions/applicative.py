from collections.abc import Callable
from abc import ABC, abstractmethod

from binds.abstractions.functor import Functor

class Applicative[T](Functor[T], ABC):

    @classmethod
    @abstractmethod
    def pure[U](cls, value: U) -> 'Applicative[U]':
        ...

    @abstractmethod
    def apply[U, V](
        self: "Applicative[Callable[[U], V]]",
        value: "Applicative[U]"
    ) -> 'Applicative[V]':
        ...


        