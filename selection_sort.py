#-*- encoding: utf-8 -*-

"""
选择算法伪代码：
SELECTION-SORT(A):
    for i = 1 to A.length - 1       // n-1
        min = i                     // n-2
        for j = i + 1 to A.length   // n(n-1)/2
            if A[j] < A[min]        // n(n-1)/2 - 1
                min = j             // n(n-1)/2 - 1(最差)
        temp = A[i]                 // n-2
        A[i] = A[min]               // n-2
        A[min] = temp               // n-2
"""                                 // Θ(n2)

def selection_sort(a):
"""选择排序"""
    for i in range(len(a)-1):   # 由于最后一次对比将最小的放在(n-1)处，自然较大的在最后
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j
        temp = a[i]
        a[i] = a[min]
        a[min] = temp
    return a[:]

a = [4, 2, 6, 5, 1, 3]
b = selection_sort(a)
print(b)
