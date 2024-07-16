def max_in_range(arr: list, start: int, end: int) -> [int or float, int ,int]:
    if not isinstance(arr, list) or not isinstance(start or end, int):
        raise TypeError()

    if not arr:
        raise ValueError("List empty")

    if start < 0 or end < 0:
        raise ValueError("end or start can`be less then 0")

    if len(arr)-1 < end:
        raise ValueError("end > len(arr)!")

    if start > end:
        raise ValueError("start can`b greater then end")

    max_element = arr[start]
    index_max = start

    for i in range(start+1, end+1, 1):
        if not isinstance(arr[i], (int, float)):
            raise TypeError()

        if arr[i] > max_element:
            max_element = arr[i]
            index_max = i

    return [max_element, index_max - start, index_max]


def rotate_and_reverse(arr: list, k: int) -> list:
    if not isinstance(arr, list) or not isinstance(k, int):
        raise TypeError

    if not arr:
        return []

    arr_length = len(arr)

    for i in range(0, k):
        buff = arr[-1]

        for j in range(arr_length-1, 0, -1):
            arr[j] = arr[j-1]

        arr[0] = buff

    for i in range(0, arr_length >> 1, 1):
        arr[i], arr[-i - 1] = arr[-i - 1], arr[i]

    return arr


def reverse_even_elements(arr: list) -> list:
    if not isinstance(arr, list):
        raise TypeError()

    if not arr:
        return []

    even_numbers = []

    for i in arr:
        if not isinstance(i, int):
            raise TypeError

        if i & 1 != 1:
            even_numbers.append(i)

    for i in range(0, len(even_numbers) >> 1, 1):
        even_numbers[i], even_numbers[-i-1] = even_numbers[-i-1], even_numbers[i]

    result = []
    even_index = 0

    for num in arr:
        if num & 1 != 1:
            result.append(even_numbers[even_index])
            even_index += 1
        else:
            result.append(num)

    return result


def increase_large_integer(digits: list) -> list:
    if not isinstance(digits, list):
        raise TypeError()

    len_lst = len(digits)

    if len_lst < 1 or len_lst > 100:
        raise ValueError()

    for i in digits:
        if not isinstance(i, int):
            raise TypeError()
        if i < 0 or i > 9:
            raise ValueError()

    lst = digits.copy()

    lst[-1] += 1

    if lst[-1] != 10:
        return lst

    for i in range(len_lst-1, 0, -1):
        if lst[i] == 10:
            lst[i] = 0
            lst[i - 1] += 1

    if lst[0] == 10:
        lst[0] = 1
        lst.append(0)

    return lst
