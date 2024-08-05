from __future__ import annotations


class PersonCard:
    def __init__(self, name, age, occupation):
        self.__name = name
        self.__age = age
        self.__occupation = occupation

    def __get_name(self) -> str:
        return self.__name

    def __get_age(self) -> int:
        return self.__age

    def __get_occupation(self) -> str:
        return self.__occupation

    name = property(__get_name)
    age = property(__get_age)
    occupation = property(__get_occupation)


class PersonList:
    class Node:
        next_node: PersonList.Node or None

        def __init__(self, person_data: PersonCard):
            self.person_data = person_data
            self.next_node = None

    __head: Node or None
    __tail: Node or None

    def __init__(self):
        self.__count = 0
        self.__head = None
        self.__tail = None

    def add_person(self, person: PersonCard) -> None:
        node = PersonList.Node(person)

        if not self.is_empty():
            node.next_node = self.__head
        else:
            self.__tail = node

        self.__head = node
        self.__count += 1

    def append_person(self, person: PersonCard) -> None:
        node = PersonList.Node(person)

        if self.is_empty():
            self.__head = node
        else:
            self.__tail.next_node = node

        self.__tail = node
        self.__count += 1

    def insert_person_at(self, index: int, person: PersonCard) -> None or Exception:
        if self.__count < index or index < 0:
            raise ValueError("Incorrect index")

        if index == 0:
            self.add_person(person)
            return

        node = PersonList.Node(person)

        node_iterator = self.__head
        counter = 0

        while counter < index-1:
            node_iterator = node_iterator.next_node
            counter += 1

        node.next_node = node_iterator.next_node
        node_iterator.next_node = node

        self.__count += 1

    def remove_first_person(self) -> Node or None:
        person = self.__head.person_data

        if self.is_empty():
            return None

        self.__head = self.__head.next_node

        if self.__count == 1:
            self.__tail = self.__head

        self.__count -= 1

        return person

    def remove_last_person(self) -> Node or None:
        person = self.__tail.person_data
        if self.is_empty():
            return None

        iterator = self.__head
        while not (iterator.next_node.next_node is None):
            iterator = iterator.next_node

        self.__tail = iterator
        self.__tail.next_node = None

        self.__count -= 1

        return person

    def remove_person(self, person: PersonCard) -> None:
        if self.is_empty():
            raise Exception("Not found")

        iterator = self.__head
        while not (iterator.next_node.person_data is person):
            if iterator.next_node.next_node is None:
                raise Exception("Not found")

            iterator = iterator.next_node

        iterator.next_node = iterator.next_node.next_node
        self.__count -= 1

    def clear_all(self):
        self.__head = None
        self.__tail = None

    def total_people(self):
        return self.__count

    def is_empty(self):
        return True if self.__count == 0 else False

    def __str__(self):
        result = ""

        iterator = self.__head

        while not (iterator is None):
            result += f"{iterator.person_data.name} -> "
            iterator = iterator.next_node

        result += "None"

        return result


# personList = PersonList()
#
# card1 = PersonCard("Firs", 1, "ss")
# card2 = PersonCard("Sec", 2, "aa")
# card3 = PersonCard("Third", 3, "rr")
# card4 = PersonCard("For", 4, "vv")
#
# personList.add_person(card1)
# personList.add_person(card4)
# personList.append_person(card3)
#
# personList.insert_person_at(0, card2)
#
#
# print(personList)
#
# personList.remove_person(card1)
# print(personList.total_people())
#
# print(personList)
