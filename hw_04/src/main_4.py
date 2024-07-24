# 1
def bobble_sort(array: list, key=lambda x: float(x), order_by=lambda x, y: x > y) -> list:
    assert isinstance(array, list), TypeError()

    length_array = len(array)
    if length_array == 0:
        return array

    if length_array == 1:
        return array

    for i in range(0, length_array-1, 1):
        for j in range(0, length_array-i-1, 1):
            if order_by(key(array[j]), key(array[j+1])):
                array[j], array[j+1] = array[j+1], array[j]

    return array


# 2
def choice_sort(array: list) -> [list, int, int]:
    assert isinstance(array, list), TypeError()

    length_array = len(array)

    for i in range(0, length_array, 1):
        assert isinstance(array[i], (int, float)), TypeError

    if length_array == 0:
        return [array, 0, 0]
    if length_array == 1:
        return [array, 0, 0]

    count_exchanges = 0
    count_comparisons = 0

    for i in range(0, length_array-1, 1):
        min_index = i

        for j in range(i+1, length_array, 1):
            if array[min_index] > array[j]:
                min_index = j
            count_comparisons += 1

        array[i], array[min_index] = array[min_index], array[i]
        count_exchanges += 1

    return [array, count_comparisons, count_exchanges]


# 3
def recursive_sum(array: list[int or float]) -> int or float:
    assert isinstance(array, list), TypeError()

    if len(array) == 0:
        return 0

    assert isinstance(array[0], (int, float)), TypeError()

    if len(array) == 1:
        return array[0]

    return array[0] + recursive_sum(array[1:])


# 4
def recursive_max(array: list[int or float]) -> int or float:
    assert isinstance(array, list), TypeError()

    if len(array) == 0:
        return 0

    assert isinstance(array[0], (int, float)), TypeError()

    if len(array) == 1:
        return array[0]

    max_elem = recursive_max(array[1:])

    return array[0] if array[0] > max_elem else max_elem


# 5
def recursive_even_sum(array: list[int or float]) -> int:
    assert isinstance(array, list), TypeError()

    if len(array) == 0:
        return 0

    assert isinstance(array[0], int), TypeError()

    if array[0] & 1 == 0:
        return array[0] + recursive_even_sum(array[1:])
    else:
        return recursive_even_sum(array[1:])


# 6
def reverse_string(string: str) -> str:
    assert isinstance(string, str), TypeError()

    if len(string) == 0:
        return string
    if len(string) == 1:
        return string

    return string[-1] + reverse_string(string[:-1])


# 7
def is_palindrome(string: str) -> bool:
    assert isinstance(string, str), TypeError()

    if len(string) == 0:
        return True

    return is_palindrome(string[1:-1]) if string[0] == string[-1] else False


# 8
def fibonacci(n: int) -> int:
    assert isinstance(n, int), TypeError()

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


# 9
def sum_of_digits(n: int) -> int:
    assert isinstance(n, int), TypeError()

    if n == 0:
        return 0

    return (n % 10) + sum_of_digits(n//10)


# 10
class DList:
    def __init__(self, size: int = 1):
        self.__size = size
        self.__count = 0
        self.__array = []

        if self.__size != 0:
            self.__array = malloc(size)

    def add(self, item: any) -> None:
        self.__is_enough_memory()

        self.__array[self.__count] = item
        self.__count += 1

    def add_front(self, item: any) -> None:
        self.__is_enough_memory()

        for i in range(self.__count, 0, -1):
            self.__array[i] = self.__array[i-1]

        self.__array[0] = item
        self.__count += 1

    def remove(self, item: any) -> None:

        for i in range(0, self.__count, 1):
            if item == self.__array[i]:

                for j in range(i, self.__count-1, 1):
                    self.__array[j] = self.__array[j + 1]

                self.__array[self.__count-1] = None

                self.__count -= 1

                return

        raise ValueError("Element was not found")

    def remove_of_index(self, index: int) -> None:
        if index > self.__count-1:
            raise ValueError("")

        for i in range(index, self.__count-1, 1):
            self.__array[i] = self.__array[i+1]

        self.__array[self.__count-1] = None

        self.__count -= 1

    def find(self, item: any) -> int:
        for i in range(0, self.__count, 1):
            if self.__array[i] == item:
                return i

        return -1

    def insert_of_index(self, item: any, index: int) -> None:
        self.__is_enough_memory()

        for i in range(self.__count, index, -1):
            self.__array[i] = self.__array[i-1]

        self.__array[index] = item
        self.__count += 1

    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

    def __is_enough_memory(self):
        if self.__count >= self.__size:
            self.__realloc()

    def __realloc(self):

        self.__size += self.__size//2

        new_memory = malloc(self.__size)

        for i in range(0, self.__count, 1):
            new_memory[i] = self.__array[i]

        self.__array = new_memory

    def __str__(self):
        array_str = ""

        for i in range(0, self.__count-1, 1):
            array_str += f"{self.__array[i]}, "

        array_str += f"{self.__array[self.__count-1]}"
        return array_str


def malloc(size: int) -> list:
    assert isinstance(size, int), TypeError()
    assert size > 0, ValueError()

    return [None] * size
