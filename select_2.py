# -*- encoding: utf-8 -*-


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
        median = group[median_index(len(group))]  # sorted() + median_index(), 求解中位数索引的“黑箱子”子程序
        medians.append(median)

    pivot = select(medians, median_index(len(medians)) + 1)  # 递归调用select(), 求解中位数的中位数
    index = partition(items, pivot)  # 这里返回的是索引+1

    if n == index:
        return items[index - 1]
    elif n < index:
        return select(items[:index - 1], n)
    else:
        return select(items[index:], n - index)


A = [4, 2, 7, 1, 5, 8, 6, 3, 28, 13, 22, 9, 15, 25, 21, 10, 11, 26, 18, 23, 19, 12, 14, 20, 16, 17, 24, 27]
print(select(A, 22))
