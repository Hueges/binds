# binds

Functional programming abstractions for Python — typed, dependency-free, and law-tested.

> **Status:** early development (0.1.0). The API may change.

## Requirements

Python 3.12+ (uses PEP 695 generic syntax).

## Installation

```bash
pip install binds
```

For development:

```bash
git clone https://github.com/Hueges/binds.git
cd binds
pip install -e ".[dev]"
```

## Abstractions

| Abstraction   | Methods                 | Extends   |
|---------------|-------------------------|-----------|
| `Functor`     | `map(fn)`               | —         |
| `Applicative` | `pure(value)`, `apply(value)` | `Functor` |

Monads are planned.

## Usage

Implement an abstraction by subclassing it:

```python
from collections.abc import Callable
from binds import Applicative


class Box[T](Applicative[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    @classmethod
    def pure[U](cls, value: U) -> "Box[U]":
        return cls(value)

    def map[U](self, fn: Callable[[T], U]) -> "Box[U]":
        return Box(fn(self.value))

    def apply[U, V](self: "Box[Callable[[U], V]]", value: "Box[U]") -> "Box[V]":
        return Box(self.value(value.value))


Box(5).map(lambda x: x + 1).value                       # 6
Box.pure(lambda x: x * 2).apply(Box(21)).value          # 42
```

Note that `apply` is called on the container holding the **function**, with the container holding the **argument**.

Everything public is importable from the top-level package (`from binds import Functor, Applicative`).
Internal module paths such as `binds.abstractions.functor` may change between versions.

## Laws

Implementations are expected to satisfy the standard laws, which the test suite checks:

- **Functor:** identity, composition
- **Applicative:** identity, homomorphism, interchange, composition

## Development

```bash
pytest       # run tests
mypy src     # type-check
```

## License

MIT
