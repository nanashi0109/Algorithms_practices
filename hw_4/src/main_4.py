# 1
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


# 2
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

# 3
def recursive_sum(array: list[int or float]) -> float:

    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    return array[0] + recursive_sum(array[1:])

# 4
def recursive_max(array: list[int or float]) -> float:
    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    max_elem = recursive_max(array[1:])

    return array[0] if array[0] > max_elem else max_elem

# 5
def recursive_even_sum(array: list[int or float]) -> float:
    if len(array) == 0:
        return 0

    if array[0] & 1 == 0:
        return array[0] + recursive_even_sum(array[1:])
    else:
        return recursive_even_sum(array[1:])

# 6
def reverse_string(string: str) -> str:
    if len(string) == 0:
        return string
    if len(string) == 1:
        return string

    return string[-1] + reverse_string(string[:-1])

# 7
def is_palindrome(string: str) -> bool:
    if len(string) == 0:
        return True

    return is_palindrome(string[1:-1]) if string[0] == string[-1] else False


# 8
def fibonacci(n: int) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


# 9
def sum_of_digits(n: int) -> int:
    if n == 0:
        return 0

    return (n % 10) + sum_of_digits(n//10)



