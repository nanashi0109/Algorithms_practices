from hw_04.src.main_4 import recursive_sum
import pytest


@pytest.mark.hw_04
@pytest.mark.parametrize("array, expected_result",
                         [
                             ([1, 4, 6, 2, 4], 17),
                             ([1.2, 5.2, 8.7, 1.9], 17.0),
                             ([5.1, 10, 5.6, 21], 41.7),
                         ])
def test_recursive_sum_positive(array, expected_result):
    assert recursive_sum(array) == expected_result


@pytest.mark.hw_04
@pytest.mark.parametrize("array, expected_result",
                         [
                             ([], 0),
                             ([0], 0)
                         ])
def test_recursive_sum_boundary(array, expected_result):
    assert recursive_sum(array) == expected_result
