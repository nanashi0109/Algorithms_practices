from hw_04.src.main_4 import DList
import pytest


@pytest.fixture(scope="function")
def precondition():
    dlist = DList(10)

    base_list = [0, "str", None, True, 1, 6, 3, "str_1"]

    for i in base_list:
        dlist.add(i)

    return dlist


@pytest.mark.hw_04
@pytest.mark.parametrize("value, index, expected_result",
                         [
                             (1, 2, "0, str, 1, None, True, 1, 6, 3, str_1"),
                             (None, 5, "0, str, None, True, 1, None, 6, 3, str_1"),
                             (False, 3, "0, str, None, False, True, 1, 6, 3, str_1"),
                         ])
def test_dlist_insert_of_index_positive(value, index, expected_result, precondition):
    precondition.insert_of_index(value, index)
    assert str(precondition) == expected_result


@pytest.mark.hw_04
@pytest.mark.parametrize("value, index, expected_result",
                         [
                             (1, 123, pytest.raises(ValueError))
                         ])
def test_dlist_insert_of_index_negative(value, index, expected_result, precondition):
    with expected_result:
        precondition.insert_of_index(value, index) == expected_result
