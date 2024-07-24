from hw_04.src.main_4 import DList
import pytest


@pytest.fixture(scope="function")
def precondition():
    dlist = DList(10)

    base_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in base_list:
        dlist.add(i)

    return dlist


@pytest.mark.hw_04
@pytest.mark.parametrize("index, expected_result",
                         [
                             (5, "0, 1, 2, 3, 4, 6, 7, 8, 9"),
                             (9, "0, 1, 2, 3, 4, 5, 6, 7, 8"),
                             (0, "1, 2, 3, 4, 5, 6, 7, 8, 9"),
                             (1, "0, 2, 3, 4, 5, 6, 7, 8, 9"),
                         ])
def test_dlist_remove_of_index_positive(index, expected_result, precondition):
    precondition.remove_of_index(index)
    assert str(precondition) == expected_result


@pytest.mark.hw_04
@pytest.mark.parametrize("index, expected_result",
                         [
                             (12, pytest.raises(ValueError))
                         ])
def test_dlist_remove_of_index_negative(index, expected_result, precondition):
    with expected_result:
        precondition.remove_of_index(index) == expected_result
