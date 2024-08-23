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
@pytest.mark.parametrize("index, person_card, expected_result, count_person",
                         [
                             (1, PersonCard("Nan", 43, "None"), "Name_3 -> Nan -> Name_2 -> Name_1 -> None", 4),
                             (2, PersonCard("Hah", 143, "None"), "Name_3 -> Name_2 -> Hah -> Name_1 -> None", 4),
                             (0, PersonCard("Hah", 143, "None"), "Hah -> Name_3 -> Name_2 -> Name_1 -> None", 4),
                         ])
def test_insert_person_positive(index, person_card, expected_result, count_person, pre_condition):
    pre_condition.insert_person_at(index, person_card)

    assert str(pre_condition) == expected_result
    assert pre_condition.total_people() == count_person


@pytest.mark.hw_05
@pytest.mark.person_list
@pytest.mark.parametrize("index, person_card, expected_result",
                         [
                             (3, PersonCard("Nan", 43, "None"), pytest.raises(ValueError)),
                             (5, PersonCard("Hah", 143, "None"), pytest.raises(ValueError)),
                             (-2, PersonCard("Hah", 143, "None"), pytest.raises(ValueError))
                         ])
def test_insert_person_negative(index, person_card, expected_result, pre_condition):
    with expected_result:
        assert pre_condition.insert_person_at(index, person_card) == expected_result
