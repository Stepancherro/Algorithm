#-*- encoding: utf-8 -*-

def insertion_sort(a):
""" 插入排序, 升序"""
    for j in range(1, len(a)):
        key = a[j]   # Insert a[j] into the sorted sequence a[0,...,j-1] 
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key
    return a[:]

a = [5, 2, 4, 6, 1, 3]
b = insertion_sort(a)
print(b)
