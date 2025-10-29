import pytest

from main import custom_sum


def test_plus():
    assert 1 + 2 == 3


def test_minus():
    assert 1 - 2 == -1


def test_sum1():
    assert 19.2 == custom_sum([1, 9.2, 9])


def test_sum2():
    assert 1.2 == custom_sum([1, 9.2, -9])


def test_sum3():
    assert 10.2 == custom_sum([1, 9.2, 0])


def test_sum4():
    assert 1 == custom_sum([1, "c", 0])


def test_sum5():
    assert 0 == custom_sum([])


def test_sum6():
    assert 1 == custom_sum([1])


def test_sum7():
    assert 1 == custom_sum()


def test_sum_tuple():
    assert custom_sum((1, 2, 2)) == 6


def test_sum_raises():
    with pytest.raises(TypeError):
        assert custom_sum(1) == 6


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ([1, 9.2, 9], 19.2),
        ([1, 9.2, -9], 1.2),
        ([1, 9.2, 0], 10.2),
        ([1, "c", 0], 1),
        ([], 0),
        ([1], 1),
        ((), 0),  # если custom_sum корректно обрабатывает пустой tuple
        ((1, 2, 2), 5),  # или 6, если custom_sum должен суммировать tuple
    ],
)
def test_custom_sum(input_data, expected):
    assert custom_sum(input_data) == expected


@pytest.mark.sum
@pytest.mark.parametrize("input_data, expected", [("c", 0), (1, 0), (None, 0), (True, 0), (False, 0), (1.9, 0)])
def test_sum_raises(input_data, expected):  # noqa F811
    data = input_data
    with pytest.raises(TypeError):
        assert custom_sum(data) == expected
