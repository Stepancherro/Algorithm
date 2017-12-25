# -*- encoding: utf-8 -*-

def heap_maximum(A):
    return A[0]


def max_heapify(A, i):
    # 维护最大堆的性质
    l = 2 * i
    r = 2 * i + 1
    if l <= len(A) and A[l - 1] > A[i - 1]:
        largest = l
    else:
        largest = i
    if r <= len(A) and A[r - 1] > A[largest - 1]:
        largest = r
    if largest != i:
        temp = A[i - 1]
        A[i - 1] = A[largest - 1]
        A[largest - 1] = temp
        max_heapify(A, largest)


def heap_extract_max(A):
    if len(A) < 1:
        raise ValueError("heap underflow")
    max = A[0]
    A[0] = A[len(A) - 1]
    A.pop()
    max_heapify(A, 1)
    return max


def heap_increase_key(A, i, key):
    if key < A[i - 1]:
        raise ValueError("new key is smaller than current key")
    A[i - 1] = key
    while i > 1 and A[i // 2 - 1] < key:
        A[i - 1] = A[i // 2 - 1]
        i = i // 2
    A[i - 1] = key


def max_heap_insert(A, key):
    A.append(- float("inf"))
    heap_increase_key(A, len(A), key)


A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
max_heap_insert(A, 15)
print(A)
