# -*- encoding: utf-8 -*-
import random


def partition(A, p, r):
    # 快速排序中的partition过程，实现了对数组A[p, r]的原址重排
    x = A[r - 1]
    i = p - 1
    repetition = 0
    for j in range(p, r):
        # 记录与A[r]相等的数目
        if A[j - 1] == x:
            repetition += 1
        if A[j - 1] <= x:
            i = i + 1
            temp = A[i - 1]
            A[i - 1] = A[j - 1]
            A[j - 1] = temp
    temp = A[i]
    A[i] = A[r - 1]
    A[r - 1] = temp
    return i + 1 - repetition // 2


def randomized_partition(A, p, r):
    # 在A[p, r]中随机抽取一个元素与最后一个元素交换
    i = random.randint(p, r)
    A[r - 1], A[i - 1] = A[i - 1], A[r - 1]
    return partition(A, p, r)  # 即返回一个新的A的partition过程


def randomized_quicksort(A, p, r):
    # 快速排序
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)


A = [5, 3, 2, 6, 7, 1, 8, 4]
randomized_quicksort(A, 1, 8)
print(A)
