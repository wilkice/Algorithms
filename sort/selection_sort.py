import pytest


def selection_sort(alist):
    length = len(alist)
    if length <= 1:
        return alist
    for i in range(length-1):
        tmp_min_index = i
        tmp_min = alist[i]
        for j in range(i+1, length):
            if alist[j] < tmp_min:
                tmp_min_index = j
                tmp_min = alist[j]
        if tmp_min_index != i:
            alist[i], alist[tmp_min_index] = alist[tmp_min_index], alist[i]
    return alist


def test_blank():
    assert selection_sort([]) == []


def test_one():
    assert selection_sort([1]) == [1]


def test_two():
    assert selection_sort([1, 1]) == [1, 1]


def test_two():
    assert selection_sort([2, 1]) == [1, 2]


def test_normal():
    assert selection_sort([3, 2, 1, 4]) == [1, 2, 3, 4]
