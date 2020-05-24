"""
keyword: 二分探索
"""

import sys
sys.setrecursionlimit(10**6)

n,k = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

l = -1; r = n # 二分探索時は探索範囲は取り得る値+-1しておく

while l+1 < r:
    c = (l+r)//2
    if h[c] < k:
        l = c
    else:
        r = c

print(n-(l+1))