#-*- encoding: utf-8 -*-

def linear_search(a, v):
"""线性查找，返回给定值v在列表中的位置"""
    for i in range(0, len(a)):
        if a[i] == v:
            return i
        i += 1
    return None
    
a = [1, 2, 3, 4, 5 , 6]
v = 3
index = linear_search(a, v)
print(index)
