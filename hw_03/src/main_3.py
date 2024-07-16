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

    for i in range(0, arr_length//2, 1):
        arr[i], arr[-i - 1] = arr[-i - 1], arr[i]

    return arr


print(rotate_and_reverse([0, 1, 2, 3, 4, 5], 1))
