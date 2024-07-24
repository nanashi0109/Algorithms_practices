from hw_04.src.main_4 import recursive_max
import pytest


@pytest.mark.hw_04
@pytest.mark.parametrize("array, expected_result",
                         [
                             ([2, 5, 6, 1, 2, 21, 3, 0], 21),
                             ([2.5, 25.1, 25.2, 6.3, 25.3], 25.3),
                             ([2, 6.1, 6], 6.1)
                         ])
def test_recursive_max_positive(array, expected_result):
    assert recursive_max(array) == expected_result


@pytest.mark.hw_04
@pytest.mark.parametrize("array, expected_result",
                         [
                             ([1], 1),
                             ([], 0),
                             ([1, 1, 1, 1, 1, 1], 1)
                         ])
def test_recursive_max_boundary(array, expected_result):
    assert recursive_max(array) == expected_result
