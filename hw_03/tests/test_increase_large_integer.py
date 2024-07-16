from hw_03.src.main_3 import increase_large_integer
import pytest


@pytest.mark.parametrize("digits, expected_result",
                         [
                             ([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]),
                             ([1, 2, 3, 4, 9], [1, 2, 3, 5, 0]),
                             ([1, 2, 9, 9, 9], [1, 3, 0, 0, 0]),
                             ([9, 9, 9, 9], [1, 0, 0, 0, 0]),
                         ])
def test_increase_int_positive(digits, expected_result):
    assert increase_large_integer(digits) == expected_result


@pytest.mark.parametrize("digits, expected_result",
                         [
                             ("str", pytest.raises(TypeError)),
                             ([0, -1, 0, 1], pytest.raises(ValueError)),
                             ([42, 1, 0, 1], pytest.raises(ValueError)),
                             ([2.4, 1.1, 0, 1], pytest.raises(TypeError)),
                             ([], pytest.raises(ValueError)),
                         ])
def test_increase_int_negative(digits, expected_result):
    with expected_result:
        assert increase_large_integer(digits) == expected_result
