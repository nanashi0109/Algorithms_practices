from hw_04.src.main_4 import DList
import pytest


@pytest.fixture(scope="function")
def precondition():
    dlist = DList(10)

    return dlist


@pytest.mark.hw_04
@pytest.mark.parametrize("value, expected_result",
                         [
                             (1, "1"),
                             (None, "None"),
                             (False, "False"),
                             ("str", "str"),
                         ])
def test_dlist_add_front_positive_1(value, expected_result, precondition):
    precondition.add_front(value)
    assert str(precondition) == expected_result


@pytest.mark.hw_04
@pytest.mark.parametrize("base_array, value, expected_result",
                         [
                             ([1, 4, "str", None], 5, "5, 1, 4, str, None"),
                             ([1, 4, "str", None], True, "True, 1, 4, str, None"),
                         ])
def test_dlist_add_front_positive_2(base_array, value, expected_result, precondition):
    for i in base_array:
        precondition.add(i)

    precondition.add_front(value)

    assert str(precondition) == expected_result
