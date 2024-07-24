from hw_04.src.main_4 import DList
import pytest


@pytest.fixture(scope="function")
def precondition():
    dlist = DList(10)

    return dlist


@pytest.mark.hw_04
@pytest.mark.parametrize("base_array, expected_result",
                         [
                             ([], True),
                             ([1, 2], False),
                             ([False], False)
                         ])
def test_dlist_is_empty_positive(base_array, expected_result, precondition):
    for i in base_array:
        precondition.add(i)

    assert precondition.is_empty() == expected_result

