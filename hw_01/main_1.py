def sum_even_numbers(numbers: list) -> int:

    if not is_list_correct(numbers, 10**5):
        raise ValueError()

    result = 0

    for number in numbers:
        if not is_number_correct(number, -2 * 10**4, 2 * 10**4):
            raise ValueError()

        if number % 2 == 0:
            result += number

    if result < 0:
        return 1

    return result


def most_frequently_encountered_element(numbers: list):

    if not is_list_correct(numbers, 10 ** 5):
        raise ValueError()

    checked_numbers = []
    result = numbers[1]
    frequency_of_result = 0

    for i in range(0, len(numbers), 1):
        if not is_number_correct(numbers[i], 1, 2 * 10**4):
            raise ValueError()

        if numbers[i] not in checked_numbers:
            frequency = 0
            for j in range(0, len(numbers), 1):
                if numbers[i] == numbers[j]:
                    frequency += 1

            if frequency > frequency_of_result:
                result = numbers[i]
                frequency_of_result = frequency

            if frequency == frequency_of_result:
                if result > numbers[i]:
                    result = numbers[i]
                    frequency_of_result = frequency

            checked_numbers.append(numbers[i])

    return result


def sum_of_target(numbers: list, target: int):
    if not is_list_correct(numbers, 104, 2):
        raise ValueError()

    for i in range(0, len(numbers), 1):
        if not is_number_correct(numbers[i], -109, 109):
            raise ValueError()

        desired_value = target - numbers[i]

        for j in range(0, len(numbers), 1):
            if numbers[j] == desired_value and j != i:
                return [i, j]


def is_list_correct(lst: list, max_count_elements: int, min_count_elements: int = 0) -> bool:
    if not isinstance(lst, list):
        raise TypeError()

    if not lst:
        raise ValueError()

    if len(lst) > max_count_elements or len(lst) < min_count_elements:
        return False

    return True


def is_number_correct(number: int, low_border, high_border) -> bool:
    if not isinstance(number, int):
        raise TypeError()

    if number < low_border or number > high_border:
        return False

    return True


print(sum_even_numbers([5, 3, 1, 6, 4, 10, 12, 54]))

print(most_frequently_encountered_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))

print(sum_of_target([2, 5, 7, 4], 9))
