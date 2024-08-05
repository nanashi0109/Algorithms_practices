import pytest
from hw_05.src.person_list import *


@pytest.fixture(scope="function")
def pre_condition():
    person_list = PersonList()

    return person_list


@pytest.mark.hw_05
@pytest.mark.parametrize("person_card, expected_result, count_person",
                         [
                             (PersonCard("Person_1", 12, "pop"), "Person_1 -> None", 1),
                             (PersonCard("Person_2", 23, "pop"), "Person_2 -> None", 1),
                         ])
def test_add_person_positive_1(person_card, expected_result, count_person, pre_condition):
    pre_condition.add_person(person_card)
    assert str(pre_condition) == expected_result
    assert pre_condition.total_people() == count_person


@pytest.mark.hw_05
@pytest.mark.parametrize("person_cards, expected_result, count_person",
                         [
                             ([
                                PersonCard("Person_1", 12, "pop"),
                                PersonCard("Person_2", 24, "pp"),
                                PersonCard("Person_3", 36, "pp"),
                              ], "Person_3 -> Person_2 -> Person_1 -> None", 3),
                         ])
def test_add_person_positive_2(person_cards, expected_result, count_person, pre_condition):
    for i in person_cards:
        pre_condition.add_person(i)

    assert str(pre_condition) == expected_result
    assert pre_condition.total_people() == count_person
