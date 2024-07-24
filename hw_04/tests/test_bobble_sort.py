from hw_04.src.main_4 import bobble_sort
import pytest


@pytest.mark.hw_04
@pytest.mark.parametrize("array, expected_result",
                         [
                             ([1, 2, 6, 2, 7, 2, 4, 8], [1, 2, 2, 2, 4, 6, 7, 8]),
                             ([1.4, 6.2, 6.1, 8.3], [1.4, 6.1, 6.2, 8.3])
                         ])
def test_bobble_sort_positive_1(array, expected_result):

    assert bobble_sort(array) == expected_result


@pytest.mark.hw_04
@pytest.mark.parametrize("array, order_by, expected_result",
                         [
                             ([1, 2, 6, 2, 7, 2, 4, 8], lambda x, y: x <= y, [8, 7, 6, 4, 2, 2, 2, 1]),
                             ([1, 2, 6, 2, 7, 2, 4, 8], lambda x, y: x >= y, [1, 2, 2, 2, 4, 6, 7, 8]),
                             ([1, 2, 6, 2, 7, 2, 4, 8], lambda x, y: x > y, [1, 2, 2, 2, 4, 6, 7, 8]),
                             ([1, 2, 6, 2, 7, 2, 4, 8], lambda x, y: x < y, [8, 7, 6, 4, 2, 2, 2, 1])
                         ])
def test_bobble_sort_positive_2(array, order_by, expected_result):

    assert bobble_sort(array, order_by=order_by) == expected_result


@pytest.mark.hw_04
@pytest.mark.parametrize("array, order_by, key, expected_result",
                         [
                             ([True, False, False, True], lambda x, y: x > y, lambda x: 1 if x else 0, [False, False, True, True]),
                         ])
def test_bobble_sort_positive_3(array, order_by, key, expected_result):

    assert bobble_sort(array, order_by=order_by, key=key) == expected_result
