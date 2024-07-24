from hw_02.src.main_2 import is_palindrome
import pytest


@pytest.mark.hw_02
@pytest.mark.parametrize("value, expected_result",
                         [
                             (512, False),
                             (121, True),
                             (-121, False),
                             (190, False),
                             (0, True),
                         ])
def test_is_palindrome_positive(value, expected_result):
    assert is_palindrome(value) == expected_result


@pytest.mark.hw_02
@pytest.mark.parametrize("value, expected_result",
                         [
                             ("str", pytest.raises(TypeError)),
                             (1.2, pytest.raises(TypeError)),
                         ])
def test_is_palindrome_negative(value, expected_result):
    with expected_result:
        assert is_palindrome(value) == expected_result
