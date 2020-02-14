from itertools import chain
from typing import List
from typing import Set
from typing import Type
from typing import Union

from hypothesis import given
from hypothesis import infer
from hypothesis.strategies import sampled_from
from pytest import raises

from chained_iterable.chained_set import CFrozenSet
from chained_iterable.chained_set import CSet


classes = sampled_from([CSet, CFrozenSet])
CSetOrCFrozenset = Union[Type[CSet], Type[CFrozenSet]]


@given(cls=classes, x=infer, xs=infer)
def test_union(cls: CSetOrCFrozenset, x: Set[int], xs: List[Set[int]]) -> None:
    cset = cls(x).union(*xs)
    assert isinstance(cset, cls)
    assert cset == x.union(*xs)


@given(cls=classes, x=infer, xs=infer)
def test_intersection(
    cls: CSetOrCFrozenset, x: Set[int], xs: List[Set[int]],
) -> None:
    cset = cls(x).intersection(*xs)
    assert isinstance(cset, cls)
    assert cset == x.intersection(*xs)


@given(cls=classes, x=infer, xs=infer)
def test_difference(
    cls: CSetOrCFrozenset, x: Set[int], xs: List[Set[int]],
) -> None:
    cset = cls(x).difference(*xs)
    assert isinstance(cset, cls)
    assert cset == x.difference(*xs)


@given(cls=classes, x=infer, y=infer)
def test_symmetric_difference(
    cls: CSetOrCFrozenset, x: Set[int], y: Set[int],
) -> None:
    cset = cls(x).symmetric_difference(y)
    assert isinstance(cset, cls)
    assert cset == x.symmetric_difference(y)


@given(x=infer, y=infer)
def test_add(x: Set[int], y: int) -> None:
    cset = CSet(x).add(y)
    assert isinstance(cset, CSet)
    assert cset == set(chain(x, [y]))


@given(x=infer, y=infer)
def test_remove(x: Set[int], y: int) -> None:
    cset = CSet(x)
    if y in x:
        new = cset.remove(y)
        assert isinstance(new, CSet)
        assert new == {i for i in x if i != y}
    else:
        with raises(KeyError, match=str(y)):
            cset.remove(y)


@given(x=infer, y=infer)
def test_discard(x: Set[int], y: int) -> None:
    cset = CSet(x).discard(y)
    assert isinstance(cset, CSet)
    assert cset == {i for i in x if i != y}


@given(x=infer)
def test_pop(x: Set[int]) -> None:
    cset = CSet(x)
    if cset:
        new = cset.pop()
        assert isinstance(new, CSet)
        assert len(new) == (len(x) - 1)
    else:
        with raises(KeyError, match="pop from an empty set"):
            cset.pop()
