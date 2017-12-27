# -*- encoding: utf-8 -*-
import math
import random


def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


def partition(A, p, r, key):
    # 快速排序中的partition过程，实现了对数组A[p, r]的原址重排
    A[A.index(key)] = A[r - 1]
    A[r - 1] = key
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


def select(A, p, r, i):
    # 将输入数组的n个元素划分为n/5组，每组5个元素，最后一组可以为n mod 5个元素
    if p == r:
        return A[p - 1]
    n = r - p + 1
    # 分为5组
    groups = []
    num_groups = int(math.ceil(n / 5))
    for j in range(num_groups - 1):
        groups.append(A[(p - 1) + j * 5: (p - 1) + j * 5 + 5])  # 这里要注意区间的选取, p,r不能省略
    groups.append(A[(p - 1) + (num_groups - 1) * 5: r])  #

    # 寻找每组的中位数
    medians = []
    for g in groups:
        medians.append(insertion_sort(g)[(len(g) + 1) // 2 - 1])

    # 寻找中位数的中位数
    x = select(medians, 1, len(medians), (len(medians) + 1) // 2)

    # 利用修改的partition，按中位数对输入数组划分，让k比划分的低区中的元素数目多1，因此x是第k小的元素
    q = partition(A, p, r, x)
    k = q - p + 1

    if i == k:
        return x
    elif i < k:
        return select(A, p, q - 1, i)
    else:
        return select(A, q + 1, r, i - k)


A = [4, 2, 7, 1, 5, 8, 6, 3, 28, 13, 22, 9, 15, 25, 21, 10, 11, 26, 18, 23, 19, 12, 14, 20, 16, 17, 24, 27]
print(select(A, 1, 28, 8))
