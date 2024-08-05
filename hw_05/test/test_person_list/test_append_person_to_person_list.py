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
@pytest.mark.person_list
@pytest.mark.parametrize("person_card, expected_result, count_person",
                         [
                             (PersonCard("Nan", 43, "None"), "Name_3 -> Name_2 -> Name_1 -> Nan -> None", 4),
                             (PersonCard("Hah", 143, "None"), "Name_3 -> Name_2 -> Name_1 -> Hah -> None", 4)
                         ])
def test_append_person_positive_1(person_card, expected_result, count_person, pre_condition):
    pre_condition.append_person(person_card)

    assert str(pre_condition) == expected_result

    assert pre_condition.total_people() == count_person


@pytest.mark.hw_05
@pytest.mark.person_list
@pytest.mark.parametrize("person_cards, expected_result, count_person",
                         [
                             ([
                                PersonCard("Nan", 43, "None"),
                                PersonCard("Hah", 143, "None"),
                              ], "Name_3 -> Name_2 -> Name_1 -> Nan -> Hah -> None", 5),
                         ])
def test_append_person_positive_2(person_cards, expected_result, count_person, pre_condition):
    for i in person_cards:
        pre_condition.append_person(i)

    assert str(pre_condition) == expected_result

    assert pre_condition.total_people() == count_person
