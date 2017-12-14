# -*- encoding: utf-8 -*-


def find_max_crossing_subarray(A, low, mid, high):
    """
    接收数组A和下标low, mid和high为输入，返回一个下标元组划定跨越中点的最大子数组的边界，
    并返回最大数组中值的和。
    允许输出为空，和最小为0， 将和大小的判断条件改为0即可。
    """
    left_sum = 0.0
    max_left = 0
    max_right = 0
    sum = 0.0
    for i in range(mid, low - 1, -1):  # 注意python中循环的边界问题，上边界取不到
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = 0.0
    sum = 0.0
    for j in range(mid + 1, high + 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return (max_left, max_right, left_sum + right_sum)


def find_maximum_subarray(A, low, high):
    """
    求解最大子数组问题的分治算法
    :param A:
    :param low:
    :param high:
    :return:
    """
    if high == low and A[low] >= 0:
        return (low, high, A[low])  # 基本情况， 只有一个元素
    elif high == low and A[low] < 0:
        return (None, None, 0.0)
    else:
        mid = int((low + high) / 2)
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)  # 之后几行完成合并工作
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


A = [-1, -1, -2, -3, -4, -5]
low = 0
high = 5
a, b, c = find_maximum_subarray(A, low, high)
print(a, b, c)
