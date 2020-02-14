from typing import FrozenSet
from typing import Iterable
from typing import NoReturn
from typing import Set
from typing import TypeVar


_T = TypeVar("_T")


class CSet(Set[_T]):
    """A set with chainable methods."""

    def __repr__(self) -> str:
        return f"{type(self)}({super().__repr__()})"

    def __str__(self) -> str:
        return f"{type(self)}({super().__str__()})"

    # set & frozenset methods

    def union(self, *others: Iterable[_T]) -> "CSet[_T]":
        return type(self)(super().union(*others))

    def intersection(self, *others: Iterable[_T]) -> "CSet[_T]":
        return type(self)(super().intersection(*others))

    def difference(self, *others: Iterable[_T]) -> "CSet[_T]":
        return type(self)(super().difference(*others))

    def symmetric_difference(self, other: Iterable[_T]) -> "CSet[_T]":
        return type(self)(super().symmetric_difference(other))

    def copy(self) -> "CSet[_T]":
        return type(self)(super().copy())

    # set methods

    def update(self) -> NoReturn:
        raise RuntimeError("Use the 'union' method instead of 'update'")

    def intersection_update(self) -> NoReturn:
        raise RuntimeError(
            "Use the 'intersection' method instead of 'intersection_update'",
        )

    def difference_update(self) -> NoReturn:
        raise RuntimeError(
            "Use the 'difference' method instead of 'difference_update'",
        )

    def symmetric_difference_update(self) -> NoReturn:
        raise RuntimeError(
            "Use the 'symmetric_difference' method instead of "
            "'symmetric_difference_update'",
        )

    def add(self, element: _T) -> "CSet[_T]":
        super().add(element)
        return self

    def remove(self, element: _T) -> "CSet[_T]":
        super().remove(element)
        return self

    def discard(self, element: _T) -> "CSet[_T]":
        super().discard(element)
        return self

    def pop(self) -> "CSet[_T]":
        super().pop()
        return self

    def clear(self) -> "CSet[_T]":
        super().clear()
        return self


class CFrozenSet(FrozenSet[_T]):
    """A frozenset with chainable methods."""

    def __repr__(self) -> str:
        return f"{type(self)}({super().__repr__()})"

    def __str__(self) -> str:
        return f"{type(self)}({super().__str__()})"

    # set & frozenset methods

    def union(self, *others: Iterable[_T]) -> "CFrozenSet[_T]":
        return type(self)(super().union(*others))

    def intersection(self, *others: Iterable[_T]) -> "CFrozenSet[_T]":
        return type(self)(super().intersection(*others))

    def difference(self, *others: Iterable[_T]) -> "CFrozenSet[_T]":
        return type(self)(super().difference(*others))

    def symmetric_difference(self, other: Iterable[_T]) -> "CFrozenSet[_T]":
        return type(self)(super().symmetric_difference(other))

    def copy(self) -> "CFrozenSet[_T]":
        return type(self)(super().copy())
