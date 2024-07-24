from hw_02.src.main_2 import fibonacci
import pytest


@pytest.mark.hw_02
@pytest.mark.parametrize("value, expected_result",
                         [
                             (0, [0]),
                             (1, [0, 1, 1]),
                             (10, [0, 1, 1, 2, 3, 5, 8]),
                             (20, [0, 1, 1, 2, 3, 5, 8, 13]),
                         ])
def test_fibonacci_positive(value, expected_result):
    assert fibonacci(value) == expected_result


@pytest.mark.hw_02
@pytest.mark.parametrize("value, expected_result",
                         [
                             (-5, pytest.raises(ValueError)),
                             (-5.2, pytest.raises(TypeError)),
                             ("str", pytest.raises(TypeError)),
                         ])
def test_fibonacci_negative(value, expected_result):
    with expected_result:
        assert fibonacci(value) == expected_result
