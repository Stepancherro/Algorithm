# -*- encoding: utf-8 -*-

import math


# 中位数索引
def median_index(n):
    if n % 2:  # 奇数情况
        return n // 2
    else:  # 偶数情况
        return n // 2 - 1


def partition(items, element):
    i = 0
    for j in range(len(items)):
        # 不需要先查找到element与最后一个元素交换, 遇到再做交换
        if items[j] == element:
            items[j], items[-1] = items[-1], items[j]

        if items[j] < element:
            items[i], items[j] = items[j], items[i]
            i += 1

    # 最后将element放到i处
    items[i], items[-1] = items[-1], items[i]

    return i + 1


def select(items, n):
    # 如果数组只含1个元素,则返回该元素
    if len(items) <= 1:
        return items[0]

    # 存储中位数
    medians = []

    # 分组,每组5个元素
    for i in range(0, len(items), 5):
        group = sorted(items[i: i + 5])  # 对每组排序
        items[i: i + 5] = group  # 将已经排序好的子数组赋给原数组
        median = group[median_index(len(group))]  # sorted() + median_index()
        medians.append(median)

    pivot = select(medians, median_index(len(medians)) + 1)  # 递归调用select(), 求解中位数的中位数
    index = partition(items, pivot)  # 这里返回的是索引+1

    if n == index:
        return items[index - 1]
    elif n < index:
        return select(items[:index - 1], n)
    else:
        return select(items[index:], n - index)


def quantiles(A, k, Q):
    if k == 1:
        return []
    n = len(A)
    i = k // 2  # 所有组别从中间分开
    x = select(A, math.ceil(i * n / k))  # x即为分位符
    partition(A, x)
    quantiles(A[: math.ceil((i * n) / k)], k // 2, Q)  # 递归调用，求左侧组别的分位符
    Q.append(x)  # 放在此处为了确保Q中元素的次序
    quantiles(A[math.ceil((i * n) / k):], math.ceil(k / 2), Q)  # 递归调用，求右侧组别的分位符


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
k = 7
Q = []
quantiles(A, k, Q)
print(Q)
