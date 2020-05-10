import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n,m,x = list(map(int, input().split()))
ca = [[int(i) for i in readline().split()] for _ in range(n)]

from itertools import combinations
import numpy as np

lc = [i for i in range(n)]
ans = 1001001001

for nc in range(1,n+1):
    lc_sub = list(combinations(lc,nc))
    for lc_sub2 in lc_sub:
        tmp_price = 0
        tmp_und = np.array([0]*m)
        for c in lc_sub2:
            tmp_price += ca[c][0]
            tmp_und += np.array(ca[c][1:])
        if all([und >= x for und in tmp_und]):
            ans = min(ans, tmp_price)

if ans == 1001001001:
    print(-1)
else:
    print(ans)