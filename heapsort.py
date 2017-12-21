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

def build_max_build(A):
    # 建最大堆
    for i in range(len(A)//2-1, 0, -1):
        max_heapify(A, i)

def heapsort(A):
    heap_size = len(A)
    build_max_build(A)
    for i in range(len(A), 1, -1):
        temp = A[0]
        A[0] = A[i -1]
        A[i -1] = temp
        heap_size = heap_size - 1
        A[0:heap_size] = max_heapify(A[0:heap_size], 1)


A = [1, 14, 10, 8, 7, 9, 3, 2, 4, 16]
heapsort(A)
print(A)
