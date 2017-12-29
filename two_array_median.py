# -*- encoding: utf-8 -*-

import math


# 中位数索引
def median_index(n):
    if n % 2:  # 奇数情况
        return n // 2
    else:  # 偶数情况
        return n // 2 - 1


def two_array_median(X, Y):
    n = len(X)
    if n == 1:  # 如果数组只有一个元素，则取两者最小的为中位数
        return min(X[0], Y[0])
    m = median_index(n)  # 计算每个数组的中位数索引
    if X[m] == Y[m]:  # 如果两个中位数相等，那么新的中位数也是该数
        return X[m]
    if X[m] < Y[m]:  # 此时整体的中位数应该在X的后半部分或者Y的前半部分
        return two_array_median(X[-(m + 1):], Y[: m + 1])
    else:
        return two_array_median(X[: m + 1], Y[-(m + 1):])


A = [1, 2, 3, 4, 5, 6]
B = [5, 6, 7, 8, 9, 10]
print(two_array_median(A, B))
