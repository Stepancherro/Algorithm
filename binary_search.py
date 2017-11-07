#-*- encoding: utf-8 -*-

"""
二分查找伪代码：
BINARY-SEARCH(A, v):
    low = 1
    high = A.length
    
    while low <= high
        mid = (low + high) / 2
        if A[mid] == v
            return mid
        if A[mid] < v
            low = mid + 1
        else
            high = mid - 1

    return NIL
"""
  
def binary_search(a, length, v):
"""二分查找"""
    low = 0
    high = length
    
    while low <= high:
        mid = (low + high) / 2
        if a[mid] == v:
            return mid
        elif a[mid] < v:
            low = mid + 1
        else:
            high = mid - 1
    return None

a = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary_search(a, 7, 6)
print(index)
