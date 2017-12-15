# -*- encoding: utf-8 -*-


def find_maximum_subarray(A, low, high):
    """
    非递归的、线性时间的算法求解最大子数组问题
    :param A:
    :param low:
    :param high:
    :return:
    """
    max_sum = 0.0
    left = 0
    right = 0
    # 使用一个数组记录子数组[0, i]的和
    sum_end = [0] * (high - low + 1)
    sum_end_left = 0
    for i in range(low, high + 1):
        # 第一个值直接赋值
        if i == low:
            sum_end[0] = A[i]
            sum_end_left = 0
            max_sum = A[i]
        else:
            # 判断前面的和是否大于0，如果大于0才有必要加到后面
            if sum_end[i - low - 1] > 0:
                sum_end[i - low] = sum_end[i - low - 1] + A[i]
            # 若前面的和小鱼0则没必要加到后面
            else:
                sum_end[i - low] = A[i]
                sum_end_left = i
        # 判断新计算的和是否大于最大值
        if sum_end[i - low] > max_sum:
            max_sum = sum_end[i - low]
            left = sum_end_left
            right = i

    return left, right, max_sum


A = [1, 3, 4, -2, 5, -3, -2, 3, -4, 1, 5, -3, -1]
low = 0
high = 12
a, b, c = find_maximum_subarray(A, low, high)
print(a, b, c)
