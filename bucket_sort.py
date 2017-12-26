# -*- encoding: utf-8 -*-


def insertion_sort(a):
    """ 插入排序, 升序"""
    for j in range(1, len(a)):
        key = a[j]  # Insert a[j] into the sorted sequence a[0,...,j-1]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    return a


def bucket_sort(A):
    # 桶排序
    n = len(A)
    B = [[] for x in range(len(A))]
    for i in range(0, n):
        B[int(n * A[i])].append(A[i])
    out = []
    for i in range(n):
        out += insertion_sort(B[i])
    return out


A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print(bucket_sort(A))
