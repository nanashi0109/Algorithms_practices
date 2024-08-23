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
@pytest.mark.parametrize("count_removes, expected_result, count_person",
                         [
                             (1, "Name_2 -> Name_1 -> None", 2),
                             (2, "Name_1 -> None", 1),
                             (3, "None", 0),
                         ])
def test_remove_first_person_positive_1(count_removes, expected_result, count_person, pre_condition):
    for i in range(0, count_removes, 1):
        pre_condition.remove_first_person()

    assert str(pre_condition) == expected_result
    assert pre_condition.total_people() == count_person


@pytest.mark.hw_05
@pytest.mark.person_list
@pytest.mark.parametrize("count_removes, expected_result",
                         [
                             (0, "Name_3"),
                             (1, "Name_2"),
                             (2, "Name_1"),
                         ])
def test_remove_first_person_positive_2(count_removes, expected_result, pre_condition):
    for i in range(0, count_removes, 1):
        pre_condition.remove_first_person()

    assert pre_condition.remove_first_person().name == expected_result


@pytest.mark.hw_05
@pytest.mark.person_list
@pytest.mark.parametrize("count_removes, expected_result, count_person",
                         [
                             (5, "None", 0),
                             (10, "None", 0)
                         ])
def test_remove_first_person_negative(count_removes, expected_result, count_person, pre_condition):
    for i in range(0, count_removes, 1):
        pre_condition.remove_first_person()

    assert str(pre_condition) == expected_result
    assert pre_condition.total_people() == count_person

