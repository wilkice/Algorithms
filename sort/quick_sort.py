import pytest


def quick_sort(alist):
    if len(alist) <= 1:
        return alist
    else:
        pivot = alist[0]
        lower = [i for i in alist[1:] if i <= pivot]
        upper = [i for i in alist[1:] if i > pivot]
        return quick_sort(lower) + [pivot] + quick_sort(upper)


def test_one():
    assert quick_sort([1]) == [1]


def test_two():
    assert quick_sort([2, 1]) == [1, 2]


def test_three():
    assert quick_sort([3, 1, 2]) == [1, 2, 3]
