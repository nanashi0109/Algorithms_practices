
def bobble_sort(array: list, key=lambda x: int(x), order_by=lambda x, y: x > y) -> list:

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


def choice_sort(array: list) -> [list, int, int]:
    length_array = len(array)

    if length_array == 0:
        return array
    if length_array == 1:
        return array

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


def recursive_sum(array: list[int or float], counter=0) -> float:

    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    if counter == len(array)-1:
        return array[counter]

    elem = array[counter]
    counter += 1
    return elem + recursive_sum(array, counter)


print(recursive_sum([1, 5, 2, 7, 21, 5]))


def recursive_max(array: list[int or float], i=0) -> float:
    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    if i == len(array)-1:
        return array[i]

    max_elem = array[i]
    i += 1
    next_elem = recursive_max(array, i)

    if max_elem < next_elem:
        max_elem = next_elem
    return max_elem


def recursive_even_sum(array: list[int or float]) -> float:
    if len(array) == 0:
        return 0

    if len(array) == 1:
        if array[0] & 1 == 0:
            return array[0]

    elem = array.pop(0)
    if elem & 1 == 0:
        return elem + recursive_even_sum(array)
    else:
        return recursive_even_sum(array)


def reverse_string(string: str) -> str:
    if len(string) == 0:
        return string
    if len(string) == 1:
        return string



