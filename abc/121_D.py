"""
keyword: XOR

F(A,B) = F(0,A-1) ^ F(0,B)

任意の整数nについてn^(n+1)=1あることから、
n = n
(n-1)^n = 1
(n-2)^(n-1)^n = 1^n
(n-3)^(n-2)^(n-1)^n = 0
(n-4)^(n-3)^(n-2)^(n-1)^n = n
...
という規則がある

従ってF(0,x)は、
x%4==0のとき、F(0,x)=x
x%4==1のとき、F(0,x)=1
x%4==2のとき、F(0,x)=1^x
x%4==3のとき、F(0,x)=0
となる
"""

import sys
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())

def rep_xor(x):
    if x%4 == 0:
        return x
    elif x%4 == 1:
        return 1
    elif x%4 == 2:
        return 1^x
    else:
        return 0

if a > 0:
    fa = rep_xor(a-1)
    fb = rep_xor(b)
    ans = fa^fb
else:
    fb = rep_xor(b)
    ans = fb

print(ans)