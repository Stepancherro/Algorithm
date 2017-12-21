# -*- encoding: utf-8 -*-


def max_heapify(A, i):
    # 维护最大堆的性质
    l = 2 * i
    r = 2 * i + 1
    if l <= len(A) and A[l-1] > A[i-1]:
        largest = l
    else:
        largest = i
    if r <= len(A) and A[r-1] > A[largest-1]:
        largest = r
    if largest != i:
        temp = A[i-1]
        A[i-1] = A[largest-1]
        A[largest-1] = temp
        max_heapify(A, largest)

def build_max_build(A):
    # 建最大堆
    for i in range(len(A)//2, 0, -1):
        max_heapify(A, i)
    return A

A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
B = build_max_build(A)
print(B)
