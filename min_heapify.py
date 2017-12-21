# -*- encoding: utf-8 -*-


def min_heapify(A, i):
    # 维护最小堆的性质
    l = 2 * i
    r = 2 * i + 1
    if l <= len(A) and A[l-1] < A[i-1]:
        smallest = l
    else:
        smallest = i
    if r <= len(A) and A[r-1] < A[smallest-1]:
        smallest = r
    if smallest != i:
        temp = A[i-1]
        A[i-1] = A[smallest-1]
        A[smallest-1] = temp
        max_heapify(A, smallest)

    return A

A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
B = min_heapify(A, 2)
print(B)
