import pytest
from hw_05.src.person_list import *


@pytest.fixture(scope="function")
def pre_condition():
    person_list = PersonList()

    cards = [
        PersonCard("Name_1", 22, "none"),
        PersonCard("Name_2", 22, "none"),
        PersonCard("Name_3", 22, "none")
    ]

    for i in cards:
        person_list.add_person(i)

    return person_list


@pytest.mark.hw_05
@pytest.mark.parametrize("expected_result, count_person",
                         [("None", 0)])
def test_clear_all_positive(expected_result, count_person, pre_condition):
    pre_condition.clear_all()
    assert str(pre_condition) == expected_result
    assert pre_condition.total_people() == count_person
