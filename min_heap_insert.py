# -*- encoding: utf-8 -*-

def heap_minimum(A):
    return A[0]


def min_heapify(A, i):
    # 维护最小堆的性质
    l = 2 * i
    r = 2 * i + 1
    if l <= len(A) and A[l - 1] < A[i - 1]:
        smallest = l
    else:
        smallest = i
    if r <= len(A) and A[r - 1] < A[smallest - 1]:
        smallest = r
    if smallest != i:
        temp = A[i - 1]
        A[i - 1] = A[smallest - 1]
        A[smallest - 1] = temp
        max_heapify(A, smallest)


def heap_extract_min(A):
    if len(A) < 1:
        raise ValueError("heap underflow")
    min = A[0]
    A[0] = A[len(A) - 1]
    A.pop()
    min_heapify(A, 1)
    return max


def heap_decrease_key(A, i, key):
    if key > A[i - 1]:
        raise ValueError("new key is larger than current key")
    A[i - 1] = key
    while i > 1 and A[i // 2 - 1] > A[i - 1]:
        temp = A[i - 1]
        A[i - 1] = A[i // 2 - 1]
        A[i // 2 - 1] = temp
        i = i // 2


def min_heap_insert(A, key):
    A.append(float("inf"))
    heap_decrease_key(A, len(A), key)


A = [1, 2, 3, 4, 7, 9, 10, 8, 14, 16]
min_heap_insert(A, 5)
print(A)
