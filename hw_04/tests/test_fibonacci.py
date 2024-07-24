from hw_04.src.main_4 import fibonacci
import pytest


@pytest.mark.hw_04
@pytest.mark.parametrize("value, expected_result",
                         [
                             (5, 5),
                             (0, 0),
                             (1, 1),
                             (2, 1),
                             (3, 2),
                             (16, 987)

                         ])
def test_fibonacci_positive(value, expected_result):
    assert fibonacci(value) == expected_result