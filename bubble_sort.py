#-*- encoding: utf-8 -*-

def bubble_sort(a):
"""冒泡排序"""
    for i in xrange(len(a)):
        for j in xrange(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp

a = [3, 6, 2, 4, 1, 5]
bubble_sort(a)
print(a)
