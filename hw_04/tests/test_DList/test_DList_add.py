from hw_04.src.main_4 import DList
import pytest


@pytest.fixture(scope="function")
def precondition():
    dlist = DList(10)

    return dlist


@pytest.mark.hw_04
@pytest.mark.parametrize("value, expected_result",
                         [
                             (5, "5"),
                             (True, "True"),
                             ("str", "str"),
                             (None, "None"),
                         ])
def test_dlist_add_positive_1(value, expected_result, precondition):
    precondition.add(value)
    assert str(precondition) == expected_result


@pytest.mark.hw_04
@pytest.mark.parametrize("value, expected_result",
                         [
                             ([2, 5, 6, 2, 8], "2, 5, 6, 2, 8"),
                             ([10, "10", True], "10, 10, True"),
                             ([None, None, None], "None, None, None"),
                         ])
def test_dlist_add_positive_2(value, expected_result, precondition):
    for i in value:
        precondition.add(i)
    assert str(precondition) == expected_result
