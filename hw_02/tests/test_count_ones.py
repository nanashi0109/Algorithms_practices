from hw_02.src.main_2 import count_ones
import pytest


@pytest.mark.hw_02
@pytest.mark.parametrize("value, expected_result",
                         [
                             (7, 3),
                             (15, 4),
                             (60, 4)
                         ])
def test_count_ones_positive(value, expected_result):
    assert count_ones(value) == expected_result


@pytest.mark.hw_02
@pytest.mark.parametrize("value, expected_result",
                         [
                             ("str", pytest.raises(TypeError)),
                             (1.3, pytest.raises(TypeError)),
                             (-1.3, pytest.raises(TypeError)),
                             (-1, pytest.raises(ValueError)),
                         ])
def test_count_ones_negative(value, expected_result):
    with expected_result:
        assert count_ones(value) == expected_result
