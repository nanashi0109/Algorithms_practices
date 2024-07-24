from hw_04.src.main_4 import sum_of_digits
import pytest


@pytest.mark.hw_04
@pytest.mark.parametrize("value, expected_result",
                         [
                             (111, 3),
                             (123, 6),
                             (987, 24),
                             (87, 15),
                             (1552, 13)
                         ])
def test_sum_of_digits_positive(value, expected_result):
    assert sum_of_digits(value) == expected_result


@pytest.mark.hw_04
@pytest.mark.parametrize("value, expected_result",
                         [
                             (0, 0),
                             (9, 9)
                         ])
def test_sum_of_digits_boundary(value, expected_result):
    assert sum_of_digits(value) == expected_result
