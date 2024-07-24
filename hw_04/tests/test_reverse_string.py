from hw_04.src.main_4 import reverse_string
import pytest


@pytest.mark.hw_04
@pytest.mark.parametrize("string, expected_result",
                         [
                             ("121", "121"),
                             ("hello", "olleh"),
                             ("garage", "egarag")
                         ])
def test_reverse_string_positive(string, expected_result):
    assert reverse_string(string) == expected_result


@pytest.mark.hw_04
@pytest.mark.parametrize("string, expected_result",
                         [
                             ("", ""),
                             ("1", "1")
                         ])
def test_reverse_string_boundary(string, expected_result):
    assert reverse_string(string) == expected_result
