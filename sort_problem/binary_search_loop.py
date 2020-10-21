"""
Find the position of a target value within a sorted array
"""
import pytest

def binary_search(original_list, num):
    if not original_list:
        return None
    low = 0
    high = len(original_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if num == original_list[mid]:
            return mid
        elif num > original_list[mid]:
            low = mid + 1
        elif num < original_list[mid]:
            high = mid - 1
    
def test_50():
    assert binary_search(list(range(0, 100)), 50) == 50

def test_3():
    assert binary_search([1,2,3,4,5], 3) == 2
    
def test_two_num():
    assert binary_search([1,2], 1) == 0

def test_two_num_upper():
    assert binary_search([1,2], 2)  == 1

def test_not_in():
    assert binary_search([1,2,4], 3) == None

def test_one_num():
    assert binary_search([1],1) == 0

def test_one_num_not_in():
    assert binary_search([2], 1) == None

def test_blank_list():
    assert binary_search([], 1) == None