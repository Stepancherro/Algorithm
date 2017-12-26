# -*- encoding: utf-8 -*-

def counting_sort(A, B, k):
    # 计数排序, A[1...n]的值均在(0,k)之间
    C = [0] * (k + 1)
    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1  # C[i]存储的是等于i的元素数目
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]  # 此时，C[i]中存储的是小于等于i的元素数目
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]  # 有C[A[j]]个数小于等于A[j],则将A[j]放到B[C[A[j]]-1]处
        C[A[j]] = C[A[j]] - 1


A = [2, 5, 3, 0, 2, 3, 0, 3]
B = [0] * len(A)
k = max(A)
counting_sort(A, B, k)
print(B)
