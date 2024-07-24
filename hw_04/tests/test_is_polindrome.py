from hw_04.src.main_4 import is_palindrome
import pytest


@pytest.mark.hw_04
@pytest.mark.parametrize("string, expected_result",
                         [
                             ("121", True),
                             ("olleh", False),
                             ("OlO", True),
                             ("Garag", False),
                             ("-55", False)
                         ])
def test_is_palindrome_positive(string, expected_result):
    assert is_palindrome(string) == expected_result


@pytest.mark.hw_04
@pytest.mark.parametrize("string, expected_result",
                         [
                             ("", True),
                             ("A", True)
                         ])
def test_is_palindrome_boundary(string, expected_result):
    assert is_palindrome(string) == expected_result
