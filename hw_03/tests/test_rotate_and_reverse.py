from hw_03.src.main_3 import rotate_and_reverse
import pytest


@pytest.mark.hw_03
@pytest.mark.parametrize("array, k, expected_result",
                         [
                             ([0, 1, 2, 3, 4, 5], 0, [5, 4, 3, 2, 1, 0]),
                             ([0, 1, 2, 3, 4, 5], 1, [4, 3, 2, 1, 0, 5]),
                             ([0, 1, 2, 3, 4, 5], 4, [1, 0, 5, 4, 3, 2]),
                             ([], 2, []),
                             ([1], 2, [1])
                         ])
def test_rotate_and_reverse_positive(array, k, expected_result):
    assert rotate_and_reverse(array, k) == expected_result


@pytest.mark.hw_03
@pytest.mark.parametrize("array, k, expected_result",
                         [
                             ("", 0, pytest.raises(TypeError)),
                         ])
def test_rotate_and_reverse_negative(array, k, expected_result):
    with expected_result:
        assert rotate_and_reverse(array, k) == expected_result

