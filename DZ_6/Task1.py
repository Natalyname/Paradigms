from _my_lib.service import Service
from random import randint

"""
Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве.
"""


def binary_search(arr, low, high, num):
  
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == num:
            return mid

        elif arr[mid] > num:
            return binary_search(arr, low, mid - 1, num)

        else:
            return binary_search(arr, mid + 1, high, num)

    else:
        return


if __name__ == "__main__":
    sorted_lst = sorted(Service.get_random_int_list(100, -100, 100))
    element = randint(-100, 100)
    result = binary_search(sorted_lst, 0, len(sorted_lst) - 1, element)

    it = iter(sorted_lst)
    for i in range(10):
        [print(str(next(it)).rjust(4), end=' ') for _ in range(10)]
        print()

    if result:
        print(f'\nЭлемент {element} найден по индексу {str(result)}.')
    else:
        print(f'\nЭлемент {element} не найден.')
