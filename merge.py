#-*- encoding: utf-8 -*-

def merge_sort(a, p, q, r):
"""分治法排序"""
    n1 = q-p
    n2 = r-q
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    for i in range(n1):   # 可用切片操作代替
        L[i] = a[p+i]
    for j in range(n2):
        R[j] = a[q+j]
    L[n1] = 'inf'
    R[n2] = 'inf'
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            a[k] = L[i]
            i = i + 1
        else:
            a[k] = R[j]
            j = j + 1
    return a[:]

a = [2, 4, 5, 7, 1, 2, 3, 6]
b = merge_sort(a, 0, 4, 8)
print(b)
