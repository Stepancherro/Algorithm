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


def median_nearest(A, k):
    """
    确定A中最接近中位数的k个元素
    缺陷：没有处理等距情况，空间复杂性太高
    :param A:
    :return:
    """
    n = len(A)
    median = select(A, math.ceil(n / 2))  # 寻找数组A的中位数,此步之后会对A排序，左侧的全部小于中位数
    distances = []  # 存储A与median之间的距离，不包含中位数
    distances_abs = []  # 距离的绝对值
    for i in range(n):
        if A[i] != median:
            distances.append(A[i] - median)
            distances_abs.append(abs(A[i] - median))
    x = select(distances_abs, k)  # 计算第k小的距离
    result = []
    for distance in distances:  # 保存前k小距离的值
        if abs(distance) <= x:
            result.append(distance + median)

    return result


A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(median_nearest(A, 5))
