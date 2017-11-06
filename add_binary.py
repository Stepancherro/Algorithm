#-*- encoding: utf-8 -*-

"""
伪代码:
ADD-BINARY(A, B):
    C = new integer[A.length + 1]
    carry = 0
    for i = 1 to A.length
        C[i] = (A[i] + B[i] + carry) % 2  // remainder
        carry = (A[i] + B[i] + carry) / 2 // quotient
    C[i] = carry
    
    return C
"""

def add_binary(a, b):
    c = [0]*(len(a)+1)
    
    carry = 0
    for i in range(len(a)):
        c[i] = (a[i] + b[i] + carry) % 2   # remainder
        carry = (a[i] + b[i] + carry) / 2  # quotient
    c[i+1] = carry
    
    return c

a = [1, 1, 0, 0, 1]
b = [1, 0, 1, 1, 1]
c = add_binary(a, b)
print(c)
