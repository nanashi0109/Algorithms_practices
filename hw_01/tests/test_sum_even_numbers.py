from hw_01.src.main_1 import sum_even_numbers
import pytest


@pytest.mark.parametrize("numbers, expected_result",
                         [
                             ([4, 5, 6, 1, 75, 3, 82, 2, 0, 4], 98),
                             ([-4, -2, -5, -2, -512, -5, 2, -5124, -5232], 1),
                             ([8, 3, 1, -5, 2, 6, -2, -24, 12], 2)
                         ])
def test_sum_even_numbers_positive(numbers, expected_result):
    assert sum_even_numbers(numbers) == expected_result


@pytest.mark.parametrize("numbers, expected_result",
                         [
                             ("str", pytest.raises(TypeError)),
                             (12, pytest.raises(TypeError)),
                             (["str", 12, 42, True], pytest.raises(TypeError)),
                             ([23.3, 4, -12.3], pytest.raises(TypeError)),
                             ([10*5, -10 ** 9], pytest.raises(ValueError)),
                             ([i for i in range(2 * 10**5)], pytest.raises(ValueError)),
                             ([], pytest.raises(ValueError))
                         ])
def test_sum_even_numbers_negative(numbers, expected_result):
    with expected_result:
        assert sum_even_numbers(numbers) == expected_result


@pytest.mark.parametrize("numbers, expected_result",
                         [
                             ([-2 * 10**4, 2 * 10**4, 10], 10),
                             ([2] * 10**5, 200000),
                             ([3, 7, 5, 19, 21], 0),
                             ([2], 2),
                         ])
def test_sum_even_numbers_boundary(numbers, expected_result):
    assert sum_even_numbers(numbers) == expected_result
