from hw_02.src.main_2 import factorial
import pytest


@pytest.mark.hw_02
@pytest.mark.parametrize("value, expected_result",
                         [
                             (0, 1),
                             (1, 1),
                             (2, 2),
                             (5, 120),
                             (10, 3628800)
                         ])
def test_factorial_positive(value, expected_result):
    assert factorial(value) == expected_result


@pytest.mark.hw_02
@pytest.mark.parametrize("value, expected_result",
                         [
                             (-1, pytest.raises(ValueError)),
                             (1.5, pytest.raises(TypeError)),
                             ("", pytest.raises(TypeError)),
                         ])
def test_factorial_negative(value, expected_result):
    with expected_result:
        assert factorial(value) == expected_result
