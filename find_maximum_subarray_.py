# -*- encoding: utf-8 -*-


def find_maaximum_subarray(A, low, high):
    """
    暴力求解最大子数组问题
    :param A:
    :param low:
    :param high:
    :return:
    """
    left = 0
    right = 0
    max_sum = - float("inf")
    for i in range(low, high + 1):
        sum = 0.0
        for j in range(i, high + 1):
            sum = sum + A[j]  # 求解i, j之间的和
            if max_sum < sum:
                left = i
                right = j
                max_sum = sum

    return (left, right, max_sum)


A = [4, -2, 5, 8, -7, 18, -14, -4, -7, 12, 4, -8, 6]
low = 0
high = 12
a, b, c = find_maaximum_subarray(A, low, high)
print(a, b, c)
