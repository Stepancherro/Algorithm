# -*- encoding: utf-8 -*-

import numpy as np


def square_matrix_multiply(A, B):
    """
    矩阵乘法
    :param A:
    :param B:
    :return:
    """
    n = A.shape[0]
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3]])
C = square_matrix_multiply(A, B)
print(C)
