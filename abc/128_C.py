"""
直積はitertools.productで求められる
"""

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
readline = sys.stdin.readline
KS = [[int(i) for i in readline().split()] for _ in range(m)]
P = [int(i) for i in readline().split()]

import itertools

L = list(itertools.product([0,1], repeat=n))

ans = 0

for l in L:
    for ks, p in zip(KS, P):
        tmp = sum([l[i-1] for i in ks[1:]])
        if tmp%2 == p:
            pass
        else:
            break
    else:
        ans += 1
        
print(ans)