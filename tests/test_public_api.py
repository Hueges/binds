import binds
from binds import abstractions
from binds.abstractions.applicative import Applicative
from binds.abstractions.functor import Functor


def test_top_level_exports_match_all():
    for name in binds.__all__:
        assert hasattr(binds, name), f"binds.__all__ lists missing name {name!r}"


def test_top_level_reexports_are_the_same_objects():
    assert binds.Functor is Functor
    assert binds.Applicative is Applicative


def test_abstractions_package_reexports():
    assert abstractions.Functor is Functor
    assert abstractions.Applicative is Applicative
