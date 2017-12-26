# -*- encoding: utf-8 -*-
import random


def partition(A, p, r):
    # 快速排序中的partition过程，实现了对数组A[p, r]的原址重排
    x = A[r - 1]
    i = p - 1
    repetition = 0
    for j in range(p, r):
        # 记录与A[r]相等的数目
        if A[j - 1] == x:
            repetition += 1
        if A[j - 1] <= x:
            i = i + 1
            temp = A[i - 1]
            A[i - 1] = A[j - 1]
            A[j - 1] = temp
    temp = A[i]
    A[i] = A[r - 1]
    A[r - 1] = temp
    return i + 1 - repetition // 2


def insertion_sort(a):
    """ 插入排序, 升序"""
    for j in range(1, len(a)):
        key = a[j]  # Insert a[j] into the sorted sequence a[0,...,j-1]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key


def limited_quicksort(A, p, r, threshold):
    # 设置K值
    if (r - p > threshold):
        q = partition(A, p, r)
        limited_quicksort(A, p, q - 1, threshold)
        limited_quicksort(A, q + 1, r, threshold)


def modified_quicksort(A, p, r):
    # 先进行快速爱嘘
    limited_quicksort(A, p, r, threshold=550)
    # 再进行插入排序
    insertion_sort(A)


A = [5, 3, 2, 6, 7, 1, 8, 4]
modified_quicksort(A, 1, 8)
print(A)
