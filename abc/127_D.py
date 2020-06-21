"""
複数回カードを置き換えるのは非効率。置き換えるカードを大きい順に並び替えてから置き換えを行なっていき、一度置き換えたカードは二度置き換えないようにする
"""

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
readline = sys.stdin.readline
A = [int(i) for i in readline().split()]

A.sort()

CB = []
for _ in range(m):
    b, c = [int(i) for i in readline().split()]
    CB.append([c, b])
    
CB.sort(reverse=True)

idx = 0
c = 0
for i in range(n):
    if A[i] < CB[idx][0]:
        A[i] = CB[idx][0]
        c += 1
    if CB[idx][1] <= c:
        idx += 1
        c = 0
    if idx >= m:
        break

print(sum(A))