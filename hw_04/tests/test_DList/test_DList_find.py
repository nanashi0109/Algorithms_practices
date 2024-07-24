from hw_04.src.main_4 import DList
import pytest


@pytest.fixture(scope="function")
def precondition():
    dlist = DList(10)

    base_list = [0, 1, 2, 3, 4, 5, 6, 7, True, 9]

    for i in base_list:
        dlist.add(i)

    return dlist


@pytest.mark.hw_04
@pytest.mark.parametrize("value, expected_result",
                         [
                             (0, 0),
                             (9, 9),
                             (None, -1),
                             ("", -1),
                             (True, 8),
                         ])
def test_dlist_find_positive(value, expected_result, precondition):

    assert precondition.find(value) == expected_result

