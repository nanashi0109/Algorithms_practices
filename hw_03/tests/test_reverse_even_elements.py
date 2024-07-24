from hw_03.src.main_3 import reverse_even_elements
import pytest


@pytest.mark.hw_03
@pytest.mark.parametrize("array, expected_result",
                         [
                             ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 10, 3, 8, 5, 6, 7, 4, 9, 2]),
                             ([], [])
                         ])
def test_reverse_even_elements_positive(array, expected_result):
    assert reverse_even_elements(array) == expected_result


@pytest.mark.hw_03
@pytest.mark.parametrize("array, expected_result",
                         [
                             ("", pytest.raises(TypeError)),
                             (["str"], pytest.raises(TypeError)),
                         ])
def test_reverse_even_elements_negative(array, expected_result):
    with expected_result:
        assert reverse_even_elements(array) == expected_result

