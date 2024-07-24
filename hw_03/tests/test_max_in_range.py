from hw_03.src.main_3 import max_in_range
import pytest


@pytest.mark.hw_03
@pytest.mark.parametrize("array, start, end, expected_result",
                         [
                             ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 9, [9, 9, 9]),
                             ([0, 1.4, 2, 3, 4.4, 5, 6.1, 7, 8, 9], 0, 9, [9, 9, 9]),
                             ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7, [7, 4, 7]),
                             ([5, 12, 64, 1, 85, 24, 1, 2], 5, 6, [24, 0, 5]),
                             ([-5, -12, -64, -1, -85, -24, -1, -2], 5, 6, [-1, 1, 6])
                         ])
def test_max_in_range_positive(array, start, end, expected_result):
    assert max_in_range(array, start, end) == expected_result


@pytest.mark.hw_03
@pytest.mark.parametrize("array, start, end, expected_result",
                         [
                             ("", 0, 0, pytest.raises(TypeError)),
                             ([1, "", True], 0, 2, pytest.raises(TypeError)),
                             ([0, 1, 2, 3, 4], 0, 10, pytest.raises(ValueError)),
                             ([0, 1, 2, 3, 4], -5, 3, pytest.raises(ValueError)),
                             ([0, 1, 2, 3, 4], 10, 3, pytest.raises(ValueError)),
                         ])
def test_max_in_range_negative(array, start, end, expected_result):
    with expected_result:
        assert max_in_range(array, start, end) == expected_result

