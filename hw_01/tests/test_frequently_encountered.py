from hw_01.src.main_1 import most_frequently_encountered_element
import pytest


@pytest.mark.parametrize("numbers, expected_result",
                         [
                             ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 4),
                             ([1, 2, 3, 4, 1, 2, 3, 1, 2, 1], 1),
                             ([52, 65, 31, 76, 13, 13, 52, 98], 13),
                             ([4, 4, 2], 4),
                             ([1, 2, 3, 4, 5], 1),
                         ])
def test_frequently_encountered_positive(numbers, expected_result):
    assert most_frequently_encountered_element(numbers) == expected_result


@pytest.mark.parametrize("numbers, expected_result",
                         [
                             ("str", pytest.raises(TypeError)),
                             (["str", True, 12], pytest.raises(TypeError)),
                             ([12.4, 75.3, 231.2], pytest.raises(TypeError)),
                             (3, pytest.raises(TypeError)),
                             ([-12, 24, 24, -12, 55, 23, 54, -21], pytest.raises(ValueError)),
                             ([13, 0, 4, 1, 64, 0], pytest.raises(ValueError)),
                             ([13, 3 * 10**4], pytest.raises(ValueError)),
                             ([2] * (2 * 10**5), pytest.raises(ValueError)),
                             ([], pytest.raises(ValueError)),
                         ])
def test_frequently_encountered_negative(numbers, expected_result):
    with expected_result:
        assert most_frequently_encountered_element(numbers) == expected_result


@pytest.mark.parametrize("numbers, expected_result",
                         [
                             ([2], 2),
                             ([2 * 10**4, 2, 2 * 10**4], 2 * 10**4),
                         ])
def test_frequently_encountered_boundary(numbers, expected_result):
    assert most_frequently_encountered_element(numbers) == expected_result

