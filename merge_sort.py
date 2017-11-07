#-*- encoding: utf-8 -*-

"""
归并排序伪代码(未设置哨兵)：
MERGE(A, p, q, r)
    n1 = q - p + 1
    n2 = r - q
    let L[1..n₁] and R[1..n₂] be new arrays
    for i = 1 to n1
        L[i] = A[p + i -1]
    for j = 1 to n2
        R[j] = A[q + j]
    i = 1
    j = 1
    for k = p to r
        if i > n
            A[k] = R[j]
            j = j + 1
        else if j > n
            A[k] = L[i]
            i = i + 1
        else if L[i] <= R[j]
            A[k] = L[i]
            i = i + 1
        else
            A[k] = R[j]
            j = j + 1
"""

def merge(a, p, q, r):
"""归并排序"""
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(n1):
        L[i] = a[p + i]
    for j in range(n2):
        R[j] = a[q + j + 1]
    i = 0
    j = 0
    for k in range(p, r + 1):
        if i >= n1:
            a[k] = R[j]
            j = j + 1
        elif j >= n2:
            a[k] = L[i]
            i = i + 1
        elif L[i] <= R[j]:
            a[k] = L[i]
            i = i + 1
        else:
            a[k] = R[j]
            j = j + 1

def merge_sort(a, p, r):
    if p < r:
        q = (p + r) / 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)

a = [5, 2, 4, 7, 1, 3, 2, 6]
merge_sort(a, 0, 7)
print(a)
