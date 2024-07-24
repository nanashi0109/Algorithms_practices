from hw_04.src.main_4 import recursive_even_sum
import pytest


@pytest.mark.hw_04
@pytest.mark.parametrize("array, expected_result",
                         [
                             ([1, 5, 2, 7, 2, 9, 2, 3], 6),
                             ([2, 6, 8, 10, 2, 4, 23, 1], 32),
                             ([-2, -5, -1, -6, -8], -16),
                             ([-2, -5, -1, -6, 8], 0)
                         ])
def test_recursive_even_sum_positive(array, expected_result):
    assert recursive_even_sum(array) == expected_result


@pytest.mark.hw_04
@pytest.mark.parametrize("array, expected_result",
                         [
                             ([1, 3, 5, 7, 9, 1, 13], 0),
                             ([], 0),
                             ([6], 6),
                         ])
def test_recursive_even_sum_boundary(array, expected_result):
    assert recursive_even_sum(array) == expected_result
