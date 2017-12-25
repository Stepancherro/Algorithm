# -*- encoding: utf-8 -*-

def partition(A, p, r):
    # 快速排序中的partition过程，实现了对数组A[p, r]的原址重排
    x = A[r - 1]
    i = p - 1
    for j in range(p, r):
        if A[j - 1] <= x:
            i = i + 1
            temp = A[i - 1]
            A[i - 1] = A[j - 1]
            A[j - 1] = temp
    temp = A[i]
    A[i] = A[r - 1]
    A[r - 1] = temp
    return i + 1


def quicksort(A, p, r):
    # 快速排序
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

A = [2, 8, 7, 1, 3, 5, 6, 4]
quicksort(A, 1, 8)
print(A)
