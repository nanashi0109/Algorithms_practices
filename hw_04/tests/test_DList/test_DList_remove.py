from hw_04.src.main_4 import DList
import pytest


@pytest.fixture(scope="function")
def precondition():
    dlist = DList(10)

    base_list = [1, 6, "str1", 3, 7, None, 2, True, "str", False, True, 1, "str", None]

    for i in base_list:
        dlist.add(i)

    return dlist


@pytest.mark.hw_04
@pytest.mark.parametrize("value, expected_result",
                         [
                             (1, "6, str1, 3, 7, None, 2, True, str, False, True, 1, str, None"),
                             (None, "1, 6, str1, 3, 7, 2, True, str, False, True, 1, str, None"),
                             (False, "1, 6, str1, 3, 7, None, 2, True, str, True, 1, str, None"),
                             ("str", "1, 6, str1, 3, 7, None, 2, True, False, True, 1, str, None"),
                             (6, "1, str1, 3, 7, None, 2, True, str, False, True, 1, str, None")
                         ])
def test_dlist_remove_positive(value, expected_result, precondition):
    precondition.remove(value)
    assert str(precondition) == expected_result


@pytest.mark.hw_04
@pytest.mark.parametrize("value, expected_result",
                         [
                             (21, pytest.raises(ValueError)),

                         ])
def test_dlist_remove_negative(value, expected_result, precondition):

    with expected_result:
        precondition.remove(value) == expected_result
