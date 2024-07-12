from hw_01.src.main_1 import sum_of_target
import pytest


@pytest.mark.parametrize("numbers, target, expected_result",
                         [
                             ([2, 7, 5, 4], 9, [0, 1]),
                             ([-2, -9, -2, -4, -2], -4, [0, 2]),
                             ([2, -5, 5, 3, 8, -2, -6], 0, [0, 5]),
                             ([2, 2, 2, 2, 2, 2], 4, [0, 1])
                         ])
def test_sum_of_target_positive(numbers, target, expected_result):
    assert sum_of_target(numbers, target) == expected_result


@pytest.mark.parametrize("numbers, target, expected_result",
                         [
                             ("str", 0, pytest.raises(TypeError)),
                             (["str", True], 0, pytest.raises(TypeError)),
                             ([23.3, 12.4, 64.1], 0, pytest.raises(TypeError)),
                             ([], 0, pytest.raises(ValueError)),
                             ([2], 0, pytest.raises(ValueError)),
                             ([-200, 3, 32, 4], 0, pytest.raises(ValueError)),
                             ([200, 20, 32, 4], 0, pytest.raises(ValueError)),
                             ([100, 20, 32, 100], 200, pytest.raises(ValueError)),
                             ([2] * 105, 4, pytest.raises(ValueError)),
                         ])
def test_sum_of_target_negative(numbers, target, expected_result):
    with expected_result:
        assert sum_of_target(numbers, target) == expected_result


@pytest.mark.parametrize("numbers, target, expected_result",
                         [
                             ([1, 2], 3, [0, 1]),
                             ([109, 32, 0], 32, [1, 2]),
                             ([100, 32, 9], 109, [0, 2]),
                             ([2] * 104, 4, [0, 1]),

                         ])
def test_sum_of_target_boundary(numbers, target, expected_result):
    assert sum_of_target(numbers, target) == expected_result
