"""
 floor(a/b) 
=(a-a%b)/b
上を利用して与えられた式を変形すると
max (A(x%B)-(Ax%B)) / B
ここで
Ax%B = A(x%B)%B
つまり、AxをBで割った余りは、xをBで割った余りにAをかけたものを、Bで割った余り
を利用すると
max (A(x%B)-A(x%B)%B) / B
つまりA(x%B)、さらに言えばx%Bを最大化すれば良い

x%Bを最大化するには
N>=B-1 のときは　x=B-1
N<B-1　のときは x=N
"""

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
A,B,N = [int(i) for i in readline().split()]

if N >= B-1:
    x = B-1
else:
    x = N

ans = A*x//B - A*(x//B)

print(ans)