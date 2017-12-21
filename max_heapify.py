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

    return A

A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
B = max_heapify(A, 2)
print(B)
