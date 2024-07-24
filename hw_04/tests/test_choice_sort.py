from hw_04.src.main_4 import choice_sort
import pytest


@pytest.mark.hw_04
@pytest.mark.parametrize("array, expected_result",
                         [
                             ([4, 2, 1, 3], [[1, 2, 3, 4], 6, 3]),
                             ([4, 2, 1, 3, 0], [[0, 1, 2, 3, 4], 10, 4]),
                             ([8.3, 3.2, 6, 1.2], [[1.2, 3.2, 6, 8.3], 6, 3]),
                             ([-2, 5, -21, 5, 0], [[-21, -2, 0, 5, 5], 10, 4]),
                         ])
def test_choice_sort_positive(array, expected_result):
    assert choice_sort(array) == expected_result


@pytest.mark.hw_04
@pytest.mark.parametrize("array, expected_result",
                         [
                             ([], [[], 0, 0]),
                             ([1], [[1], 0, 0])
                         ])
def test_choice_sort_boundary(array, expected_result):
    assert choice_sort(array) == expected_result
