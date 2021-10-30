import toy_package.bin_search as bs
import pytest


@pytest.mark.parametrize("data,target,expected", [
    ([0, 1, 3, 5], 3, 2),
    ([1, 3, 5, 7, 9, 11], 11, 5)
])
def test_parametrized_return_index(data, target, expected) -> None:
    assert bs.binary_search(data, target) is expected


def test_bin_search_returns_index_when_exists() -> None:
    data = [0, 1, 3, 5]
    target = 3

    outcome = bs.binary_search(data, target)

    assert outcome == 2


def test_bin_search_returns_default_when_not_exist() -> None:
    data = [1, 3, 6, 7]
    target = 2

    outcome = bs.binary_search(data, target)

    assert outcome == -1
