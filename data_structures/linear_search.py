""" Linear search """
from typing import List


def linear_search_v1(array: List, target: int):
    return array.index(target) if target in array else "Element does not exist"


def linear_search_v2(array: List, target: int) -> int:
    for i in range(0, len(array)):
        if array[i] == target:
            return i
    return -1


if __name__ == '__main__':

    l1 = [5, 3, 2, 6, 3, 1, 9]

    # index = linear_search_v1(l1, 7)
    # print(index)

    index = linear_search_v2(l1, 5)
    print(index)

